# Project 1: Healthcare Data Exploration

## About the Project

Every healthcare dataset has a story hidden in its numbers. Before applying machine learning or drawing conclusions, it is important to understand what the data actually contains.

This project was my starting point in healthcare data analysis. I worked with a small dataset containing information about individuals, their ages, haemoglobin levels and anaemia status.

The main purpose was to learn how to organise healthcare data, examine its quality, calculate basic statistical measures and identify simple patterns using Python.

It also helped me understand why data cleaning and exploratory data analysis are important first steps in any healthcare research project.

## Objectives

- Understand the structure of a healthcare dataset.
- Examine the distribution of age and haemoglobin levels.
- Identify the number of individuals labelled as anaemic and non-anaemic.
- Calculate descriptive statistics.
- Compare haemoglobin levels across anaemia-status groups.
- Create visualisations to communicate the findings.
- Learn the basic workflow of healthcare data analysis using Python.

## Dataset Description

The dataset contains 10 records and 4 variables:

| Variable | Description |
|---|---|
| Person_ID | Unique record identifier |
| Age | Age of the individual in years |
| Haemoglobin | Haemoglobin level |
| Anaemia_Status | Anaemia label (Yes/No) |

**Important:** This is a small, synthetic dataset created for learning and demonstrating data analysis techniques. It does not represent actual patients or a population survey.

## Tools and Technologies

- Python
- Google Colab
- GitHub
- Pandas – data organisation and analysis
- Matplotlib – data visualisation

## Methodology

I followed a basic exploratory data analysis workflow:

1. Loaded the healthcare dataset into Python.
2. Examined the number of rows, columns and variable types.
3. Checked for missing values and duplicate records.
4. Calculated descriptive statistics for age and haemoglobin.
5. Examined the distribution of anaemia status.
6. Compared average age and haemoglobin levels between the two groups.
7. Created graphs to make the findings easier to understand.
8. Exported the processed data, statistical summaries and visualisations.

## Key Findings

The dataset contained 10 observations and 4 variables.

The data quality assessment found:
- Missing values: 0
- Duplicate rows: 0

### Descriptive Statistics

| Measure | Age | Haemoglobin |
|---|---:|---:|
| Mean | 31.5 years | 11.69 |
| Minimum | 19 | 9.5 |
| Maximum | 50 | 14.0 |
| Standard deviation | 10.61 | 1.59 |

### Anaemia Status

- Anaemia labelled Yes: 5 individuals (50%)
- Anaemia labelled No: 5 individuals (50%)

### Group Comparison

| Group | Average Age | Average Haemoglobin |
|---|---:|---:|
| Anaemia: Yes | 27.6 years | 10.36 |
| Anaemia: No | 35.4 years | 13.02 |

In this small dataset, the group labelled as anaemic had a lower average haemoglobin level than the group labelled as non-anaemic.

These results are descriptive observations from the synthetic dataset and should not be treated as clinical evidence.

## Project Outputs

The `results` folder contains:
- Analysed healthcare dataset
- Descriptive statistics
- Data quality summary
- Anaemia status summary
- Group analysis
- Age distribution graph
- Anaemia distribution graph
- Haemoglobin comparison graph

A project report is also included in the repository.

## Public Health Relevance

Haemoglobin levels are an important indicator in the assessment of anaemia. Understanding how health indicators are distributed and how they differ between groups is a useful starting point for public health data analysis.

This introductory project helped me understand how basic statistical methods can be used to organise and communicate health-related information.

## Limitations

- The dataset contains only 10 observations.
- It is synthetic and does not represent a real population.
- The analysis is descriptive and does not establish causation.
- No clinical diagnosis or population-level conclusion can be drawn from these results.

## Conclusion

This project helped me become familiar with the first steps of working with healthcare data. I learned how to inspect a dataset, check its quality, calculate descriptive statistics, compare groups and create visualisations.

Although it was a small introductory exercise, it gave me a foundation for working on larger and more meaningful public health datasets in the following projects.

**This project is educational and is not intended for clinical diagnosis or decision-making.**
