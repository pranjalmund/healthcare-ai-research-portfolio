# Project 2: Anaemia Data Analysis Across Indian States and Union Territories

## About the Project

Anaemia remains an important public health concern in India, affecting children, women and men. Understanding how its prevalence varies across different States and Union Territories can help highlight the scale of the problem and the need for continued public health attention.

In this project, I analysed State/UT-wise anaemia prevalence data from India's National Family Health Survey (NFHS-5), 2019–21.

Unlike my first project, which used a small synthetic dataset, this project introduced me to working with aggregate government-reported public health data.

The aim was to compare anaemia prevalence among children, women and men, identify States/UTs with higher reported prevalence, and explore patterns using descriptive statistics and visualisations.

## Objectives

- Examine anaemia prevalence among children aged 6–59 months.
- Analyse anaemia prevalence among women aged 15–49 years.
- Analyse anaemia prevalence among men aged 15–49 years.
- Compare prevalence across States and Union Territories.
- Identify States/UTs with higher reported anaemia prevalence.
- Explore relationships between the three population groups.
- Present the findings through tables and visualisations.

## Data Source

The analysis uses State/UT-level anaemia figures based on NFHS-5 (2019–21), as reproduced in the Government of India's Lok Sabha Unstarred Question No. 1953, answered on 2 August 2024.

**Source:** [Government of India – Lok Sabha Question No. 1953](https://sansad.in/getFile/loksabhaquestions/annex/182/AU1953_osmtyG.pdf)

The dataset contains 36 State/UT records and four variables:

| Variable | Description |
|---|---|
| State_UT | Name of State or Union Territory |
| Children_6_59_months_anaemic_pct | Anaemia prevalence among children aged 6–59 months |
| Women_15_49_years_anaemic_pct | Anaemia prevalence among women aged 15–49 years |
| Men_15_49_years_anaemic_pct | Anaemia prevalence among men aged 15–49 years |

## Tools and Technologies

- Python
- Google Colab
- GitHub
- Pandas – data cleaning and analysis
- Matplotlib – data visualisation

## Methodology

The analysis followed these steps:

1. Collected and organised the State/UT-level anaemia data.
2. Loaded the dataset using Pandas.
3. Examined the dataset structure and variable types.
4. Checked for missing values, duplicate records and values outside the expected percentage range.
5. Calculated descriptive statistics for the three population groups.
6. Calculated average prevalence across the available State/UT records.
7. Identified the ten States/UTs with the highest prevalence in each population group.
8. Compared anaemia prevalence across children, women and men.
9. Explored correlations between the three prevalence indicators.
10. Created graphs to communicate State/UT-level differences and patterns.

## Key Findings

The dataset contained 36 State/UT records and 4 variables.

The initial data quality assessment found:
- Missing values: 0
- Duplicate rows: 0
- Values outside the 0–100 percentage range: 0

### Average Anaemia Prevalence

The unweighted average across the 36 State/UT records was:

| Population Group | Average Prevalence |
|---|---:|
| Children aged 6–59 months | 62.13% |
| Women aged 15–49 years | 53.99% |
| Men aged 15–49 years | 22.52% |

Children had the highest average reported prevalence among the three groups, followed by women and men.

**Important:** These are unweighted averages of State/UT percentages. They are not national NFHS estimates and should not be interpreted as such.

### State/UT Comparisons

The project also generated separate rankings for:
- Ten States/UTs with the highest child anaemia prevalence.
- Ten States/UTs with the highest women’s anaemia prevalence.
- Ten States/UTs with the highest men’s anaemia prevalence.

These comparisons helped identify geographic differences in reported anaemia prevalence.

### Correlation Analysis

A correlation matrix was generated to explore how State/UT-level prevalence indicators varied in relation to one another.

Correlation can help identify patterns between indicators, but it does not establish that one condition or population group's prevalence causes another.

## Project Outputs

The `results` folder contains:
- Analysed anaemia dataset
- Data quality summary
- Descriptive statistics
- Average prevalence by population group
- Top ten State/UTs for children, women and men
- Correlation matrix
- Average prevalence comparison graph
- State-wise prevalence graphs
- Children-versus-women scatter plot
- Analysis notes

A detailed project report is also included in the repository.

## Public Health Relevance

Anaemia is an important indicator for maternal and child health and broader population health monitoring.

Comparing State/UT-level prevalence can help identify geographic differences, support discussions around nutrition and health services, and highlight the importance of public health programmes focused on prevention, screening and treatment.

This analysis also demonstrates how government survey data can be organised and used to communicate population-level health patterns.

## Limitations

- The dataset contains aggregate State/UT-level figures, not individual participant records.
- The averages calculated in this project are unweighted averages across States/UTs.
- State/UT-level comparisons do not explain the reasons behind differences in prevalence.
- Correlation does not establish causation.
- The dataset is based on NFHS-5 (2019–21), so it should not be presented as a current 2026 prevalence estimate.
- The values were transcribed from the government annexure and should be checked against the original source before reuse in formal research.
- The analysis does not include confidence intervals or statistical significance testing.

## Conclusion

This project helped me understand how large-scale public health survey findings can be organised and compared across geographical areas.

By examining anaemia prevalence among children, women and men, I was able to explore differences between population groups and States/UTs and understand how descriptive statistics can support public health interpretation.

It also helped me appreciate the importance of data sources, accurate transcription, appropriate interpretation and clear communication when working with government health statistics.

**This is a descriptive public health analysis and is not intended for individual diagnosis or clinical decision-making.**
