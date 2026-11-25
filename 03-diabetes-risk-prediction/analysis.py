
from pathlib import Path
import warnings

import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

warnings.filterwarnings("ignore")

# --------------------------------------------------
# 1. PROJECT PATHS AND SETTINGS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = (
    BASE_DIR / "data" /
    "diabetes_012_health_indicators_BRFSS2015.csv"
)

RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

TARGET = "Diabetes_012"

CLASS_NAMES = [
    "No Diabetes",
    "Prediabetes",
    "Diabetes"
]

RANDOM_STATE = 42

# --------------------------------------------------
# 2. LOAD DATASET
# --------------------------------------------------

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_PATH}"
    )

df = pd.read_csv(DATA_PATH)

if TARGET not in df.columns:
    raise ValueError(
        f"Target column '{TARGET}' is missing."
    )

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# --------------------------------------------------
# 3. DATA QUALITY ANALYSIS
# --------------------------------------------------

quality_summary = pd.DataFrame({
    "Metric": [
        "Number of records",
        "Number of columns",
        "Missing values",
        "Duplicate rows"
    ],
    "Value": [
        len(df),
        len(df.columns),
        int(df.isnull().sum().sum()),
        int(df.duplicated().sum())
    ]
})

quality_summary.to_csv(
    RESULTS_DIR / "data_quality_summary.csv",
    index=False
)

print("\nData Quality Summary:")
print(quality_summary.to_string(index=False))

# Check expected value ranges
valid_ranges = {
    "Diabetes_012": (0, 2),
    "HighBP": (0, 1),
    "HighChol": (0, 1),
    "CholCheck": (0, 1),
    "BMI": (1, 100),
    "Smoker": (0, 1),
    "Stroke": (0, 1),
    "HeartDiseaseorAttack": (0, 1),
    "PhysActivity": (0, 1),
    "Fruits": (0, 1),
    "Veggies": (0, 1),
    "HvyAlcoholConsump": (0, 1),
    "AnyHealthcare": (0, 1),
    "NoDocbcCost": (0, 1),
    "GenHlth": (1, 5),
    "MentHlth": (0, 30),
    "PhysHlth": (0, 30),
    "DiffWalk": (0, 1),
    "Sex": (0, 1),
    "Age": (1, 13),
    "Education": (1, 6),
    "Income": (1, 8)
}

range_results = []

for column, (minimum, maximum) in valid_ranges.items():
    if column in df.columns:
        invalid_count = (
            (~df[column].between(minimum, maximum))
            & df[column].notna()
        ).sum()

        range_results.append({
            "Column": column,
            "Expected_Minimum": minimum,
            "Expected_Maximum": maximum,
            "Invalid_Values": int(invalid_count)
        })

pd.DataFrame(range_results).to_csv(
    RESULTS_DIR / "value_range_checks.csv",
    index=False
)

# --------------------------------------------------
# 4. DESCRIPTIVE STATISTICS
# --------------------------------------------------

df.describe().round(2).to_csv(
    RESULTS_DIR / "descriptive_statistics.csv"
)

# --------------------------------------------------
# 5. DIABETES CATEGORY DISTRIBUTION
# --------------------------------------------------

df = df.dropna(subset=[TARGET]).copy()

if not set(df[TARGET].unique()).issubset({0, 1, 2}):
    raise ValueError("Unexpected diabetes target categories.")

category_counts = (
    df[TARGET].value_counts().sort_index()
)

category_percentages = (
    df[TARGET].value_counts(normalize=True).sort_index() * 100
)

target_summary = pd.DataFrame({
    "Diabetes_Category": [0, 1, 2],
    "Category_Name": CLASS_NAMES,
    "Respondent_Count": [
        int(category_counts.get(i, 0))
        for i in range(3)
    ],
    "Percentage": [
        round(category_percentages.get(i, 0), 2)
        for i in range(3)
    ]
})

target_summary.to_csv(
    RESULTS_DIR / "diabetes_category_distribution.csv",
    index=False
)

plt.figure(figsize=(8, 5))
plt.bar(CLASS_NAMES, target_summary["Respondent_Count"])
plt.title("Distribution of Diabetes Categories")
plt.xlabel("Diabetes Category")
plt.ylabel("Number of Respondents")
plt.tight_layout()
plt.savefig(
    RESULTS_DIR / "diabetes_category_distribution.png",
    dpi=300
)
plt.close()

# --------------------------------------------------
# 6. HEALTH INDICATOR COMPARISON
# --------------------------------------------------

indicators = [
    "BMI",
    "Age",
    "HighBP",
    "HighChol",
    "GenHlth",
    "PhysActivity",
    "Smoker",
    "Fruits",
    "Veggies",
    "Education",
    "Income"
]

available_indicators = [
    col for col in indicators if col in df.columns
]

group_summary = (
    df.groupby(TARGET)[available_indicators]
    .mean()
    .round(2)
)

group_summary.to_csv(
    RESULTS_DIR / "health_indicators_by_diabetes.csv"
)

# Convert binary indicator means into percentages
binary_indicators = [
    "HighBP",
    "HighChol",
    "PhysActivity",
    "Smoker",
    "Fruits",
    "Veggies"
]

percentage_summary = group_summary.copy()

for column in binary_indicators:
    if column in percentage_summary.columns:
        percentage_summary[column] *= 100

percentage_summary.round(2).to_csv(
    RESULTS_DIR / "health_indicator_percentages.csv"
)

# Create individual comparison graphs
graph_indicators = [
    "HighBP",
    "HighChol",
    "PhysActivity",
    "Smoker",
    "Fruits",
    "Veggies",
    "GenHlth"
]

for column in graph_indicators:
    if column not in df.columns:
        continue

    values = df.groupby(TARGET)[column].mean()

    if column in binary_indicators:
        values = values * 100
        ylabel = "Respondents (%)"
    else:
        ylabel = "Average Rating"

    plt.figure(figsize=(8, 5))
    plt.bar(CLASS_NAMES, values.reindex([0, 1, 2]))
    plt.title(f"{column} by Diabetes Category")
    plt.xlabel("Diabetes Category")
    plt.ylabel(ylabel)
    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / f"{column.lower()}_comparison.png",
        dpi=300
    )
    plt.close()

# --------------------------------------------------
# 7. BMI DISTRIBUTION
# --------------------------------------------------

if "BMI" in df.columns:
    plot_data = [
        df.loc[df[TARGET] == category, "BMI"]
        .sample(
            n=min(10000, (df[TARGET] == category).sum()),
            random_state=RANDOM_STATE
        )
        for category in [0, 1, 2]
    ]

    plt.figure(figsize=(8, 5))
    plt.boxplot(plot_data, labels=CLASS_NAMES)
    plt.title("BMI Distribution Across Diabetes Categories")
    plt.xlabel("Diabetes Category")
    plt.ylabel("BMI")
    plt.tight_layout()
    plt.savefig(
        RESULTS_DIR / "bmi_distribution_by_diabetes.png",
        dpi=300
    )
    plt.close()

# --------------------------------------------------
# 8. CORRELATION ANALYSIS
# --------------------------------------------------

correlation_matrix = df.corr(numeric_only=True)

correlation_matrix.round(3).to_csv(
    RESULTS_DIR / "correlation_matrix.csv"
)

plt.figure(figsize=(14, 11))

plt.imshow(
    correlation_matrix,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    aspect="auto"
)

plt.colorbar(label="Correlation Coefficient")

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=90
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

plt.title("Correlation Matrix of Health Indicators")
plt.tight_layout()
plt.savefig(
    RESULTS_DIR / "correlation_matrix.png",
    dpi=300
)
plt.close()

# --------------------------------------------------
# 9. PREPARE DATA FOR MACHINE LEARNING
# --------------------------------------------------

X = df.drop(columns=[TARGET])
y = df[TARGET].astype(int)

# Use numeric predictors for this baseline model
X = X.select_dtypes(include=np.number)

if X.empty:
    raise ValueError("No numeric predictor columns found.")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=RANDOM_STATE,
    stratify=y
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))

# --------------------------------------------------
# 10. TRAIN LOGISTIC REGRESSION MODEL
# --------------------------------------------------

model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        solver="lbfgs",
        random_state=RANDOM_STATE
    ))
])

print("\nTraining Logistic Regression model...")

model.fit(X_train, y_train)

print("Model training completed!")

# --------------------------------------------------
# 11. MODEL EVALUATION
# --------------------------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

balanced_accuracy = balanced_accuracy_score(
    y_test, y_pred
)

macro_f1 = f1_score(
    y_test, y_pred, average="macro"
)

metrics = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Balanced Accuracy",
        "Macro F1 Score"
    ],
    "Score": [
        accuracy,
        balanced_accuracy,
        macro_f1
    ]
})

metrics["Score"] = metrics["Score"].round(4)

metrics.to_csv(
    RESULTS_DIR / "model_performance_metrics.csv",
    index=False
)

print("\nModel Performance:")
print(metrics.to_string(index=False))

# Classification report
report = classification_report(
    y_test,
    y_pred,
    labels=[0, 1, 2],
    target_names=CLASS_NAMES,
    output_dict=True,
    zero_division=0
)

pd.DataFrame(report).transpose().round(4).to_csv(
    RESULTS_DIR / "classification_report.csv"
)

# --------------------------------------------------
# 12. CONFUSION MATRIX
# --------------------------------------------------

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=[0, 1, 2]
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=CLASS_NAMES
)

fig, ax = plt.subplots(figsize=(8, 6))
disp.plot(ax=ax, cmap="Blues", values_format="d")
plt.title("Diabetes Classification Confusion Matrix")
plt.tight_layout()
plt.savefig(
    RESULTS_DIR / "confusion_matrix.png",
    dpi=300
)
plt.close()

# --------------------------------------------------
# 13. SAVE FEATURE COEFFICIENTS
# --------------------------------------------------

classifier = model.named_steps["classifier"]

coefficients = pd.DataFrame(
    classifier.coef_,
    columns=X.columns,
    index=CLASS_NAMES
)

coefficients.transpose().to_csv(
    RESULTS_DIR / "model_coefficients.csv"
)

# --------------------------------------------------
# 14. SAVE TRAINED MODEL
# --------------------------------------------------

joblib.dump(
    model,
    RESULTS_DIR / "diabetes_logistic_regression_model.joblib"
)

# --------------------------------------------------
# 15. SAVE ANALYSIS NOTES
# --------------------------------------------------

notes = """
PROJECT 3: DIABETES RISK PREDICTION

Dataset:
CDC Behavioral Risk Factor Surveillance System (BRFSS) 2015,
using a Kaggle-hosted copy of the dataset.

Target categories:
0 = No diabetes
1 = Prediabetes
2 = Diabetes

Analysis:
- Data quality assessment
- Descriptive statistics
- Health indicator comparisons
- Correlation analysis
- Three-class Logistic Regression baseline
- Class balancing during model training
- Evaluation using accuracy, balanced accuracy,
  macro F1-score, classification report and confusion matrix

Important limitations:
- The dataset is based on self-reported survey information.
- It represents a US survey from 2015, not the Indian population.
- The target categories are imbalanced.
- Identical rows were not automatically removed.
- Associations do not establish causation.
- The model is an educational research prototype.
- It has not been clinically validated and must not be
  used for diagnosis, screening or treatment decisions.
"""

(RESULTS_DIR / "analysis_notes.txt").write_text(
    notes.strip(),
    encoding="utf-8"
)

print("\n----------------------------------")
print("PROJECT 3 ANALYSIS COMPLETED")
print("----------------------------------")
print("All output files saved in:", RESULTS_DIR)
