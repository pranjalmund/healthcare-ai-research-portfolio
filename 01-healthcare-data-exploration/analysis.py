
# PROJECT 1: HEALTHCARE DATA EXPLORATION

# Import required libraries
import os
import pandas as pd
import matplotlib.pyplot as plt

# Create project folders
os.makedirs("data", exist_ok=True)
os.makedirs("results", exist_ok=True)

# ------------------------------------------------
# 1. CREATE THE HEALTHCARE DATASET
# ------------------------------------------------

data = {
    "Person_ID": range(1, 11),
    "Age": [22, 25, 30, 19, 45, 35, 28, 50, 21, 40],
    "Haemoglobin": [12.5, 10.2, 13.1, 9.8, 11.5,
                    14.0, 10.8, 12.0, 9.5, 13.5],
    "Anaemia_Status": [
        "No", "Yes", "No", "Yes", "Yes",
        "No", "Yes", "No", "Yes", "No"
    ]
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("data/healthcare_dataset.csv", index=False)

print("Dataset created successfully!")

# ------------------------------------------------
# 2. EXPLORE THE DATASET
# ------------------------------------------------

print("\nFirst five records:")
print(df.head())

print("\nDataset dimensions:")
print(df.shape)

print("\nColumn information:")
print(df.info())

# ------------------------------------------------
# 3. CHECK DATA QUALITY
# ------------------------------------------------

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate records:")
print(df.duplicated().sum())

quality = pd.DataFrame({
    "Measure": [
        "Total Records",
        "Total Variables",
        "Missing Values",
        "Duplicate Records"
    ],
    "Result": [
        len(df),
        len(df.columns),
        df.isnull().sum().sum(),
        df.duplicated().sum()
    ]
})

quality.to_csv("results/data_quality_summary.csv", index=False)

# ------------------------------------------------
# 4. DESCRIPTIVE STATISTICS
# ------------------------------------------------

print("\nDescriptive Statistics:")
print(df[["Age", "Haemoglobin"]].describe())

statistics = df[["Age", "Haemoglobin"]].describe()

statistics.to_csv(
    "results/descriptive_statistics.csv"
)

# ------------------------------------------------
# 5. ANAEMIA STATUS DISTRIBUTION
# ------------------------------------------------

status_count = df["Anaemia_Status"].value_counts()

print("\nAnaemia Status Distribution:")
print(status_count)

status_percentage = (
    df["Anaemia_Status"].value_counts(normalize=True) * 100
)

print("\nAnaemia Status Percentage:")
print(status_percentage)

status_summary = pd.DataFrame({
    "Count": status_count,
    "Percentage": status_percentage
})

status_summary.to_csv(
    "results/anaemia_status_summary.csv"
)

# ------------------------------------------------
# 6. GROUP ANALYSIS
# ------------------------------------------------

group_analysis = df.groupby(
    "Anaemia_Status"
)[["Age", "Haemoglobin"]].mean()

print("\nGroup Analysis:")
print(group_analysis)

group_analysis.to_csv(
    "results/group_analysis.csv"
)

# ------------------------------------------------
# 7. AGE DISTRIBUTION GRAPH
# ------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(df["Age"], bins=6, edgecolor="black")

plt.title("Age Distribution")
plt.xlabel("Age (Years)")
plt.ylabel("Number of Individuals")

plt.tight_layout()

plt.savefig("results/age_distribution.png")
plt.show()

# ------------------------------------------------
# 8. ANAEMIA DISTRIBUTION GRAPH
# ------------------------------------------------

plt.figure(figsize=(7, 5))

status_count.reindex(["No", "Yes"]).plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Anaemia Status Distribution")
plt.xlabel("Anaemia Status")
plt.ylabel("Number of Individuals")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("results/anaemia_distribution.png")
plt.show()

# ------------------------------------------------
# 9. HAEMOGLOBIN COMPARISON GRAPH
# ------------------------------------------------

plt.figure(figsize=(7, 5))

df.boxplot(
    column="Haemoglobin",
    by="Anaemia_Status"
)

plt.title("Haemoglobin Comparison by Anaemia Status")
plt.suptitle("")
plt.xlabel("Anaemia Status")
plt.ylabel("Haemoglobin Value")

plt.tight_layout()

plt.savefig("results/haemoglobin_comparison.png")
plt.show()

# ------------------------------------------------
# 10. SAVE ANALYSED DATASET
# ------------------------------------------------

df.to_csv(
    "results/analysed_healthcare_dataset.csv",
    index=False
)

print("\n--------------------------------")
print("PROJECT 1 ANALYSIS COMPLETED")
print("--------------------------------")

print("\nAll datasets, summaries and graphs")
print("have been saved in the project folders.")

print("\nIMPORTANT:")
print("This project uses synthetic data.")
print("It is not a diagnostic or clinical tool.")
