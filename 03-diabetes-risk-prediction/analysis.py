
# PROJECT 3: DIABETES RISK PREDICTION
# Exploratory Data Analysis and Data Quality Assessment

import os
import pandas as pd
import matplotlib.pyplot as plt

# Create results folder
os.makedirs("results", exist_ok=True)

# Load dataset
file_path = "data/diabetes_binary_health_indicators_BRFSS2015.csv"
df = pd.read_csv(file_path)

print("\nDIABETES HEALTH INDICATORS ANALYSIS")
print("-----------------------------------")

# Basic dataset information
print("\nDataset shape:", df.shape)
print("\nFirst five records:")
print(df.head())

print("\nColumn information:")
print(df.info())

# Data quality assessment
quality_summary = pd.DataFrame({
    "Measure": [
        "Total Records",
        "Total Variables",
        "Missing Values",
        "Duplicate Records",
        "Unique Records",
        "Diabetes Target Values"
    ],
    "Result": [
        len(df),
        len(df.columns),
        int(df.isnull().sum().sum()),
        int(df.duplicated().sum()),
        int(len(df.drop_duplicates())),
        int(df["Diabetes_binary"].nunique())
    ]
})

quality_summary.to_csv(
    "results/data_quality_summary.csv", index=False
)

print("\nData Quality Summary:")
print(quality_summary)

# Descriptive statistics
descriptive_stats = df.describe().T
descriptive_stats.to_csv(
    "results/descriptive_statistics.csv"
)

# Diabetes status distribution
diabetes_counts = df["Diabetes_binary"].value_counts().sort_index()

diabetes_summary = pd.DataFrame({
    "Diabetes_Status": ["No diabetes", "Diabetes"],
    "Number_of_Records": [
        int(diabetes_counts.get(0, 0)),
        int(diabetes_counts.get(1, 0))
    ]
})

diabetes_summary["Percentage"] = (
    diabetes_summary["Number_of_Records"] / len(df) * 100
)

diabetes_summary.to_csv(
    "results/diabetes_status_summary.csv", index=False
)

print("\nDiabetes Status Distribution:")
print(diabetes_summary)

# Average health indicators by diabetes status
health_columns = [
    "BMI", "HighBP", "HighChol", "Smoker",
    "PhysActivity", "GenHlth", "Age"
]

group_analysis = df.groupby("Diabetes_binary")[
    health_columns
].mean()

group_analysis.to_csv(
    "results/health_indicators_by_diabetes_status.csv"
)

print("\nAverage Health Indicators by Diabetes Status:")
print(group_analysis)

# Chart 1: Diabetes status distribution
plt.figure(figsize=(8, 6))
plt.bar(
    ["No Diabetes", "Diabetes"],
    diabetes_summary["Number_of_Records"]
)
plt.title("Distribution of Diabetes Status")
plt.xlabel("Diabetes Status")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("results/diabetes_distribution.png")
plt.close()

# Chart 2: BMI distribution
plt.figure(figsize=(8, 6))
plt.hist(df["BMI"], bins=30, edgecolor="black")
plt.title("Distribution of Body Mass Index")
plt.xlabel("BMI")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("results/bmi_distribution.png")
plt.close()

# Chart 3: Average BMI by diabetes status
plt.figure(figsize=(8, 6))
plt.bar(
    ["No Diabetes", "Diabetes"],
    group_analysis["BMI"]
)
plt.title("Average BMI by Diabetes Status")
plt.xlabel("Diabetes Status")
plt.ylabel("Average BMI")
plt.tight_layout()
plt.savefig("results/average_bmi_comparison.png")
plt.close()

# Chart 4: High blood pressure by diabetes status
plt.figure(figsize=(8, 6))
plt.bar(
    ["No Diabetes", "Diabetes"],
    group_analysis["HighBP"] * 100
)
plt.title("High Blood Pressure by Diabetes Status")
plt.xlabel("Diabetes Status")
plt.ylabel("Percentage of Records (%)")
plt.tight_layout()
plt.savefig("results/high_bp_comparison.png")
plt.close()

# Correlation analysis
correlation = df.corr(numeric_only=True)
correlation.to_csv("results/correlation_matrix.csv")

# Correlation heatmap
plt.figure(figsize=(14, 10))
plt.imshow(correlation, cmap="coolwarm", aspect="auto")
plt.colorbar(label="Correlation")
plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=90
)
plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)
plt.title("Correlation Between Health Indicators")
plt.tight_layout()
plt.savefig("results/correlation_heatmap.png")
plt.close()

# Save analysed dataset
df.to_csv(
    "results/analysed_diabetes_dataset.csv",
    index=False
)

# Analysis notes
with open("results/analysis_notes.txt", "w") as file:
    file.write(
        "PROJECT 3: DIABETES RISK PREDICTION\n\n"
        "Dataset: Diabetes Health Indicators, "
        "based on BRFSS 2015 survey data.\n"
        "Dataset source used: Kaggle-hosted copy.\n\n"
        "Analysis includes data quality assessment, "
        "descriptive statistics, diabetes status distribution, "
        "group comparisons and correlation analysis.\n\n"
        "The dataset contains self-reported survey indicators. "
        "It is not a clinical diagnostic dataset.\n\n"
        "Duplicate records are reported but not automatically "
        "removed. Their handling will be considered during "
        "the modelling stage.\n\n"
        "Findings describe this dataset and should not be "
        "generalised to the Indian population.\n"
    )

print("\nPROJECT 3 EXPLORATORY ANALYSIS COMPLETED!")
print("All outputs have been saved in the results/ folder.")
