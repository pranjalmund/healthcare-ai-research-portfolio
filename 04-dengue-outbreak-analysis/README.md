# Project 4: Dengue Outbreak Analysis in India (2021–2025)

## About the Project

Dengue continues to be an important public health concern in India, particularly during periods when mosquito breeding and transmission increase. Understanding how reported dengue cases and deaths vary across different states and over time can help us identify patterns and areas that may need greater public health attention.

For this project, I analysed state-wise dengue surveillance data from India for the years 2021 to 2025. The main aim was to understand how the reported disease burden changed over these five years, identify states with higher numbers of reported cases, and examine the relationship between reported cases and deaths.

This project gave me an opportunity to apply Python-based data analysis to a real public health issue.

## Objectives

- Examine the annual trend in reported dengue cases and deaths in India.
- Compare dengue burden across States and Union Territories.
- Identify the ten States/UTs with the highest cumulative reported cases.
- Calculate and compare the reported Case Fatality Ratio (CFR).
- Visualise dengue trends using charts and graphs.
- Understand how surveillance data can support public health planning.

## Data Source

The dataset was compiled from the official dengue surveillance information published by the **National Centre for Vector Borne Diseases Control (NCVBDC), Government of India**.

**Source:** [Dengue Situation in India – NCVBDC](https://ncvbdc.mohfw.gov.in/index4.php?font=Normal&lang=1&level=0&lid=3715&linkid=431)

The dataset contains state-wise reported dengue cases and deaths for 2021, 2022, 2023, 2024 and 2025.

It includes 37 State/UT entries and 11 columns, including the State/UT name and annual case and death counts.

## Tools and Technologies

- Python
- Google Colab
- GitHub
- Pandas – data handling and analysis
- NumPy – numerical calculations
- Matplotlib – data visualisation

## Methodology

I followed a step-by-step approach to complete the analysis:

1. **Data collection:** Compiled State/UT-wise dengue cases and deaths from the official NCVBDC source.
2. **Data quality assessment:** Checked the dataset structure, missing values and duplicate records.
3. **Data organisation:** Converted the dataset into a year-wise format to make comparisons easier.
4. **Annual analysis:** Calculated yearly totals of reported dengue cases and deaths.
5. **State-wise comparison:** Identified States/UTs with higher cumulative reported case counts.
6. **CFR calculation:** Calculated the reported Case Fatality Ratio using the formula:

   CFR (%) = (Reported deaths / Reported cases) × 100

7. **Visualisation:** Created graphs to understand annual trends, state-wise differences and the distribution of reported cases.

## Key Findings

### 1. Annual dengue trends

The analysis showed the following reported figures:

| Year | Reported Cases | Reported Deaths |
|---|---:|---:|
| 2021 | 193,245 | 346 |
| 2022 | 233,251 | 303 |
| 2023 | 289,235 | 485 |
| 2024 | 233,519 | 297 |
| 2025 | 121,824 | 131 |

The highest number of reported cases and deaths in this dataset occurred in 2023.

Reported cases increased from 2021 to 2023, followed by a decline in 2024 and a lower reported total in 2025.

The 2025 figure needs cautious interpretation because West Bengal's data were not reported in the source table for that year.

### 2. States with higher reported dengue cases

When the reported cases were combined across the five-year period, the following States/UTs appeared among the ten highest:

- Uttar Pradesh
- West Bengal
- Karnataka
- Maharashtra
- Tamil Nadu
- Rajasthan
- Punjab
- Kerala
- Delhi
- Bihar

Uttar Pradesh recorded the highest cumulative reported case count in this dataset.

### 3. Case Fatality Ratio

The Case Fatality Ratio was calculated to understand the proportion of reported dengue cases associated with reported deaths.

Among the ten States/UTs with the highest cumulative reported cases, Kerala had the highest calculated cumulative CFR, at approximately 0.71%.

These figures should be interpreted carefully because differences in disease reporting, case detection and healthcare access can influence comparisons.

## Project Outputs

The `results` folder contains the files generated during the analysis, including:

- Data quality summary
- Annual dengue summary
- State-wise dengue summary
- Top ten State/UT lists for individual years
- Case fatality ratio analysis
- Annual dengue cases and deaths graphs
- Top ten States/UTs visualisation
- State-wise dengue heatmap
- Analysis notes

## Public Health Relevance

Dengue surveillance data can help public health professionals understand where the reported disease burden is higher and how it changes over time.

This analysis highlights the importance of continuous disease surveillance, timely reporting, mosquito control measures, community awareness and preparedness of healthcare services.

From a public health perspective, state-wise comparisons can help identify areas that may require closer monitoring and further investigation.

## Limitations

There are a few important limitations to keep in mind:

- The analysis uses reported dengue cases and deaths, not the actual number of all infections.
- The 2025 State/UT data are incomplete because West Bengal is not reported in the source table.
- Ladakh is recorded as not reported in the dataset.
- The analysis uses absolute case counts and does not calculate population-adjusted incidence rates.
- Differences in surveillance systems and reporting practices may influence comparisons between States/UTs.
- CFR is a descriptive measure and should not be interpreted as an individual's risk of death.
- The findings show patterns in reported data and do not establish cause-and-effect relationships.

## Conclusion

This project helped me understand how routine disease surveillance data can be used to study an important public health problem.

By analysing five years of reported dengue cases and deaths, I was able to identify annual trends, compare the reported burden across States and Union Territories, and explore differences in reported case fatality ratios.

More importantly, the project helped me connect data analysis with practical public health questions, including disease monitoring, outbreak preparedness and the importance of reliable surveillance systems.

**This is an educational and descriptive public health analysis. It is not a clinical prediction model or a diagnostic tool.**
