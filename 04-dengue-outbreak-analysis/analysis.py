
# ============================================================
# PROJECT 4: DENGUE OUTBREAK ANALYSIS IN INDIA (2021–2025)
# ============================================================

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. SET PROJECT PATHS
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "dengue_statewise_cases_deaths_2021_2025.csv"
RESULTS_DIR = BASE_DIR / "results"

RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

df = pd.read_csv(DATA_PATH)

years = [2021, 2022, 2023, 2024, 2025]

print("\nDENGUE OUTBREAK ANALYSIS")
print("=" * 50)
print("Dataset shape:", df.shape)
print("\nFirst five records:")
print(df.head())

# ------------------------------------------------------------
# 3. DATA QUALITY ASSESSMENT
# ------------------------------------------------------------

missing_values = df.isnull().sum()
duplicate_rows = df.duplicated().sum()
duplicate_states = df["State_UT"].duplicated().sum()

quality_summary = pd.DataFrame({
    "Measure": [
        "Number of State/UT records",
        "Number of variables",
        "Missing values",
        "Duplicate rows",
        "Duplicate State/UT names"
    ],
    "Value": [
        len(df),
        len(df.columns),
        int(missing_values.sum()),
        int(duplicate_rows),
        int(duplicate_states)
    ]
})

quality_summary.to_csv(
    RESULTS_DIR / "data_quality_summary.csv", index=False
)

print("\nDATA QUALITY SUMMARY")
print(quality_summary)

# ------------------------------------------------------------
# 4. RESHAPE DATA INTO YEAR-WISE FORMAT
# ------------------------------------------------------------

records = []

for year in years:
    for _, row in df.iterrows():
        records.append({
            "State_UT": row["State_UT"],
            "Year": year,
            "Cases": row[f"Cases_{year}"],
            "Deaths": row[f"Deaths_{year}"]
        })

long_df = pd.DataFrame(records)

# Calculate reported case fatality ratio (CFR)
long_df["CFR_Percent"] = np.where(
    long_df["Cases"] > 0,
    (long_df["Deaths"] / long_df["Cases"]) * 100,
    np.nan
)

long_df.to_csv(
    RESULTS_DIR / "dengue_long_format_dataset.csv",
    index=False
)

# ------------------------------------------------------------
# 5. YEAR-WISE NATIONAL TOTALS
# ------------------------------------------------------------

annual_summary = (
    long_df.groupby("Year")
    .agg(
        Total_Cases=("Cases", "sum"),
        Total_Deaths=("Deaths", "sum"),
        Reporting_State_UTs=("Cases", "count")
    )
    .reset_index()
)

annual_summary["CFR_Percent"] = (
    annual_summary["Total_Deaths"]
    / annual_summary["Total_Cases"] * 100
)

annual_summary.to_csv(
    RESULTS_DIR / "annual_dengue_summary.csv",
    index=False
)

print("\nANNUAL DENGUE SUMMARY")
print(annual_summary.to_string(index=False))

# ------------------------------------------------------------
# 6. STATE/UT-WISE TOTALS FOR 2021–2025
# ------------------------------------------------------------

state_summary = (
    long_df.groupby("State_UT")
    .agg(
        Total_Cases=("Cases", "sum"),
        Total_Deaths=("Deaths", "sum")
    )
    .reset_index()
)

state_summary["CFR_Percent"] = np.where(
    state_summary["Total_Cases"] > 0,
    state_summary["Total_Deaths"]
    / state_summary["Total_Cases"] * 100,
    np.nan
)

state_summary = state_summary.sort_values(
    "Total_Cases", ascending=False
)

state_summary.to_csv(
    RESULTS_DIR / "statewise_dengue_summary.csv",
    index=False
)

print("\nTOP 10 STATES/UTs BY TOTAL REPORTED CASES")
print(state_summary.head(10).to_string(index=False))

# ------------------------------------------------------------
# 7. TOP 10 STATES/UTs FOR EACH YEAR
# ------------------------------------------------------------

for year in years:
    yearly_data = long_df[
        (long_df["Year"] == year) &
        (long_df["Cases"].notna())
    ]

    top_10 = yearly_data.nlargest(10, "Cases")

    top_10.to_csv(
        RESULTS_DIR / f"top_10_states_{year}.csv",
        index=False
    )

# ------------------------------------------------------------
# 8. YEARLY DENGUE CASES GRAPH
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    annual_summary["Year"],
    annual_summary["Total_Cases"],
    marker="o",
    linewidth=2
)

plt.title("Reported Dengue Cases in India (2021–2025)")
plt.xlabel("Year")
plt.ylabel("Reported Cases")
plt.xticks(years)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    RESULTS_DIR / "annual_dengue_cases.png",
    dpi=300
)
plt.close()

# ------------------------------------------------------------
# 9. YEARLY DENGUE DEATHS GRAPH
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    annual_summary["Year"].astype(str),
    annual_summary["Total_Deaths"]
)

plt.title("Reported Dengue Deaths in India (2021–2025)")
plt.xlabel("Year")
plt.ylabel("Reported Deaths")
plt.tight_layout()

plt.savefig(
    RESULTS_DIR / "annual_dengue_deaths.png",
    dpi=300
)
plt.close()

# ------------------------------------------------------------
# 10. TOP 10 STATES/UTs OVER THE FIVE-YEAR PERIOD
# ------------------------------------------------------------

top_states = state_summary.head(10).sort_values(
    "Total_Cases", ascending=True
)

plt.figure(figsize=(11, 7))

plt.barh(
    top_states["State_UT"],
    top_states["Total_Cases"]
)

plt.title("Top 10 States/UTs by Reported Dengue Cases (2021–2025)")
plt.xlabel("Total Reported Cases")
plt.ylabel("State/UT")
plt.tight_layout()

plt.savefig(
    RESULTS_DIR / "top_10_dengue_states.png",
    dpi=300
)
plt.close()

# ------------------------------------------------------------
# 11. STATE-WISE CASE FATALITY RATIO
# ------------------------------------------------------------

cfr_data = state_summary.dropna(
    subset=["CFR_Percent"]
).sort_values("CFR_Percent", ascending=False)

cfr_data.to_csv(
    RESULTS_DIR / "statewise_case_fatality_ratio.csv",
    index=False
)

plt.figure(figsize=(11, 7))

top_cfr = cfr_data.head(10).sort_values(
    "CFR_Percent", ascending=True
)

plt.barh(
    top_cfr["State_UT"],
    top_cfr["CFR_Percent"]
)

plt.title("10 Highest State/UT Reported Dengue CFRs (2021–2025)")
plt.xlabel("Case Fatality Ratio (%)")
plt.ylabel("State/UT")
plt.tight_layout()

plt.savefig(
    RESULTS_DIR / "statewise_cfr_comparison.png",
    dpi=300
)
plt.close()

# ------------------------------------------------------------
# 12. STATE-WISE CASE TREND HEATMAP
# ------------------------------------------------------------

case_columns = [f"Cases_{year}" for year in years]

heatmap_data = df.set_index("State_UT")[case_columns]

plt.figure(figsize=(12, 13))

plt.imshow(
    heatmap_data,
    aspect="auto",
    interpolation="nearest"
)

plt.colorbar(label="Reported Dengue Cases")
plt.xticks(
    range(len(years)),
    years
)
plt.yticks(
    range(len(heatmap_data.index)),
    heatmap_data.index,
    fontsize=7
)

plt.title("State/UT-wise Dengue Cases (2021–2025)")
plt.xlabel("Year")
plt.ylabel("State/UT")
plt.tight_layout()

plt.savefig(
    RESULTS_DIR / "statewise_dengue_heatmap.png",
    dpi=300
)
plt.close()

# ------------------------------------------------------------
# 13. YEAR-TO-YEAR CHANGE IN REPORTED CASES
# ------------------------------------------------------------

annual_summary["Yearly_Change_Percent"] = (
    annual_summary["Total_Cases"].pct_change() * 100
)

annual_summary.to_csv(
    RESULTS_DIR / "annual_dengue_summary.csv",
    index=False
)

# ------------------------------------------------------------
# 14. SAVE ANALYSIS NOTES
# ------------------------------------------------------------

notes = """
PROJECT 4: DENGUE OUTBREAK ANALYSIS IN INDIA

Dataset:
Official state/UT-wise reported dengue cases and deaths,
2021–2025.

Analysis performed:
1. Data quality assessment.
2. Year-wise reported cases and deaths.
3. State/UT-wise case and death totals.
4. Top 10 States/UTs by reported cases.
5. Reported case fatality ratio calculation.
6. Year-to-year change in reported cases.
7. State/UT-wise trend visualisation.

Important limitations:
- These are reported surveillance figures, not estimates
  of all dengue infections.
- Missing values are not treated as zero.
- State/UT totals are not population-adjusted incidence rates.
- CFR is calculated as reported deaths divided by reported
  cases. It is not an infection fatality rate.
- Differences in reporting and surveillance may affect
  comparisons between States/UTs and years.
- The dataset does not establish causation.
- This is a descriptive public health analysis, not a
  clinical prediction or diagnostic tool.
"""

with open(
    RESULTS_DIR / "analysis_notes.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(notes)

# ------------------------------------------------------------
# 15. COMPLETION MESSAGE
# ------------------------------------------------------------

print("\n" + "=" * 50)
print("DENGUE ANALYSIS COMPLETED SUCCESSFULLY!")
print("All output files saved in:", RESULTS_DIR)
print("=" * 50)
