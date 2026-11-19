
# PROJECT 2: ANAEMIA DATA ANALYSIS
# NFHS-5 (2019-21): State/UT-wise prevalence

import os
import pandas as pd
import matplotlib.pyplot as plt

# Create output folder
os.makedirs("results", exist_ok=True)

# Load the dataset
file_path = "data/nfhs5_statewise_anaemia.csv"
df = pd.read_csv(file_path)

# Define analysis columns
population_columns = [
    "Children_6_59_months_anaemic_pct",
    "Women_15_49_years_anaemic_pct",
    "Men_15_49_years_anaemic_pct"
]

# Check required columns
required_columns = ["State_UT"] + population_columns

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing columns: {missing_columns}")

# Convert prevalence columns to numeric
for col in population_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 1. Basic dataset information
print("\nPROJECT 2: ANAEMIA DATA ANALYSIS")
print("--------------------------------")
print("Dataset shape:", df.shape)
print("\nFirst five records:")
print(df.head())

# 2. Data quality assessment
quality_summary = pd.DataFrame({
    "Measure": [
        "Total Records",
        "Total Variables",
        "Missing Values",
        "Duplicate Records",
        "Unique States/UTs",
        "Values Outside 0-100%"
    ],
    "Result": [
        len(df),
        len(df.columns),
        int(df.isnull().sum().sum()),
        int(df.duplicated().sum()),
        int(df["State_UT"].nunique()),
        int(((df[population_columns] < 0) |
             (df[population_columns] > 100)).sum().sum())
    ]
})

quality_summary.to_csv(
    "results/data_quality_summary.csv", index=False
)

print("\nData quality summary:")
print(quality_summary)

# 3. Descriptive statistics
descriptive_stats = df[population_columns].describe().T
descriptive_stats.to_csv(
    "results/descriptive_statistics.csv"
)

print("\nDescriptive statistics:")
print(descriptive_stats)

# 4. Average prevalence across listed States/UTs
# These are unweighted averages, not national prevalence estimates.
average_prevalence = df[population_columns].mean()

average_summary = average_prevalence.reset_index()
average_summary.columns = [
    "Population_Group", "Average_Prevalence_Percent"
]

average_summary.to_csv(
    "results/average_prevalence_by_group.csv",
    index=False
)

print("\nAverage prevalence across States/UTs:")
print(average_summary)

# 5. Identify the ten highest-prevalence States/UTs
for column, label in [
    (population_columns[0], "children"),
    (population_columns[1], "women"),
    (population_columns[2], "men")
]:
    top_ten = df[["State_UT", column]].sort_values(
        by=column, ascending=False
    ).head(10)

    top_ten.to_csv(
        f"results/top_10_{label}_anaemia.csv",
        index=False
    )

# 6. Create a comparison chart
chart_labels = [
    "Children (6-59 months)",
    "Women (15-49 years)",
    "Men (15-49 years)"
]

plt.figure(figsize=(9, 6))
plt.bar(
    chart_labels,
    average_prevalence.values,
    edgecolor="black"
)
plt.title("Average Anaemia Prevalence Across States/UTs")
plt.ylabel("Average Prevalence (%)")
plt.xlabel("Population Group")
plt.xticks(rotation=10)
plt.tight_layout()
plt.savefig("results/average_prevalence_comparison.png")
plt.close()

# 7. State-wise comparison among children
children_sorted = df.sort_values(
    population_columns[0], ascending=False
)

plt.figure(figsize=(12, 7))
plt.barh(
    children_sorted["State_UT"],
    children_sorted[population_columns[0]]
)
plt.title("Anaemia Prevalence Among Children by State/UT")
plt.xlabel("Prevalence (%)")
plt.ylabel("State/UT")
plt.tight_layout()
plt.savefig("results/children_anaemia_by_state.png")
plt.close()

# 8. State-wise comparison among women
women_sorted = df.sort_values(
    population_columns[1], ascending=False
)

plt.figure(figsize=(12, 7))
plt.barh(
    women_sorted["State_UT"],
    women_sorted[population_columns[1]]
)
plt.title("Anaemia Prevalence Among Women by State/UT")
plt.xlabel("Prevalence (%)")
plt.ylabel("State/UT")
plt.tight_layout()
plt.savefig("results/women_anaemia_by_state.png")
plt.close()

# 9. State-wise comparison among men
men_sorted = df.sort_values(
    population_columns[2], ascending=False
)

plt.figure(figsize=(12, 7))
plt.barh(
    men_sorted["State_UT"],
    men_sorted[population_columns[2]]
)
plt.title("Anaemia Prevalence Among Men by State/UT")
plt.xlabel("Prevalence (%)")
plt.ylabel("State/UT")
plt.tight_layout()
plt.savefig("results/men_anaemia_by_state.png")
plt.close()

# 10. Relationship between child and women prevalence
plt.figure(figsize=(8, 6))
plt.scatter(
    df[population_columns[0]],
    df[population_columns[1]]
)
plt.title(
    "Child and Women Anaemia Prevalence Across States/UTs"
)
plt.xlabel("Children's Anaemia Prevalence (%)")
plt.ylabel("Women's Anaemia Prevalence (%)")
plt.tight_layout()
plt.savefig("results/children_vs_women_scatter.png")
plt.close()

# 11. Correlation analysis (exploratory)
correlation = df[population_columns].corr()
correlation.to_csv("results/correlation_matrix.csv")

print("\nCorrelation matrix:")
print(correlation)

# 12. Save the analysed dataset
df.to_csv(
    "results/analysed_anaemia_dataset.csv",
    index=False
)

# 13. Save source and methodology notes
with open("results/analysis_notes.txt", "w") as file:
    file.write(
        "PROJECT 2: ANAEMIA DATA ANALYSIS\n\n"
        "Dataset: NFHS-5 (2019-21), State/UT-wise "
        "anaemia prevalence.\n"
        "Source: Government of India, Lok Sabha "
        "Unstarred Question No. 1953, answered "
        "on 02 August 2024.\n"
        "Source URL: https://sansad.in/getFile/"
        "loksabhaquestions/annex/182/AU1953_osmtyG.pdf\n\n"
        "Analysis includes descriptive statistics, "
        "data quality checks, state-wise comparisons, "
        "visualisations and exploratory correlations.\n\n"
        "The average across States/UTs is unweighted "
        "and should not be interpreted as national "
        "prevalence.\n\n"
        "This is an ecological descriptive analysis. "
        "It does not establish causation or provide "
        "individual diagnosis or clinical advice.\n"
    )

print("\nPROJECT 2 ANALYSIS COMPLETED!")
print("All summaries and charts saved in results/.")
