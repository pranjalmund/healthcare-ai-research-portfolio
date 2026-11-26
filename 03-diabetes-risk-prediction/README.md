# Project 3: Diabetes Risk Prediction Using Machine Learning

## About the Project

Diabetes is a major public health concern worldwide, and understanding the health and lifestyle factors associated with it is an important part of disease prevention and risk assessment.

For this project, I explored a large health-indicator dataset based on the 2015 Behavioral Risk Factor Surveillance System (BRFSS) survey from the United States.

The project began with exploratory data analysis to understand the distribution of diabetes categories and examine how different health indicators varied across groups. I then took the analysis a step further by building a basic machine learning classification model.

The main aim was to understand how machine learning can be applied to population health data, how model performance is evaluated, and why accuracy alone is not enough when working with imbalanced health datasets.

## Objectives

- Explore a large diabetes-related health-indicator dataset.
- Understand the distribution of diabetes categories.
- Examine relationships between health indicators and diabetes status.
- Compare selected demographic, behavioural and health characteristics across groups.
- Identify data quality issues.
- Develop a baseline machine learning classification model.
- Evaluate the model using multiple performance metrics.
- Understand the challenges of class imbalance in healthcare prediction.

## Dataset Description

The dataset used is the **Diabetes Health Indicators Dataset**, based on the CDC's 2015 BRFSS data and obtained through a Kaggle-hosted copy.

It contains:

- 253,680 observations
- 22 variables
- One target variable with three categories

### Target Variable: Diabetes_012

| Value | Category |
|---|---|
| 0 | No diabetes |
| 1 | Prediabetes |
| 2 | Diabetes |

The dataset includes health indicators such as:
- BMI
- High blood pressure
- High cholesterol
- Physical activity
- Smoking history
- Fruit and vegetable consumption
- General health
- Age group
- Education
- Income

**Data source:** CDC BRFSS 2015, accessed through a Kaggle-hosted dataset copy.

## Tools and Technologies

- Python
- Google Colab
- GitHub
- Pandas – data handling and analysis
- NumPy – numerical operations
- Matplotlib – data visualisation
- Scikit-learn – machine learning and model evaluation
- Joblib – saving the trained model

## Methodology

The project followed a structured data analysis and machine learning workflow.

### 1. Data Loading and Quality Assessment

- Loaded the dataset into Python.
- Examined the number of observations and variables.
- Checked missing values.
- Checked duplicate records.
- Reviewed the distribution and range of variables.

The dataset contained 253,680 observations and 22 variables, with no missing values. There were 23,899 exact duplicate rows.

These records were retained because the dataset does not contain participant identifiers that would allow us to establish whether identical responses represent duplicate individuals.

### 2. Exploratory Data Analysis

The distribution of the target variable was examined:

| Diabetes Category | Observations | Percentage |
|---|---:|---:|
| No diabetes | 213,703 | 84.24% |
| Prediabetes | 4,631 | 1.83% |
| Diabetes | 35,346 | 13.93% |

The analysis also explored differences in BMI, blood pressure, cholesterol, physical activity, smoking history, fruit and vegetable consumption, general health, education and income.

### 3. Machine Learning Model

A Logistic Regression model was developed to classify observations into the three diabetes categories.

The modelling workflow included:

- Stratified 80:20 train-test split.
- Median imputation within a preprocessing pipeline.
- Standardisation of numerical features.
- Class-weight balancing to address the unequal distribution of target categories.
- Model training using Scikit-learn.

The model was saved using Joblib for reproducibility.

### 4. Model Evaluation

The model was evaluated using:
- Accuracy
- Balanced accuracy
- Macro F1-score
- Precision
- Recall
- Classification report
- Confusion matrix

These measures provide a broader understanding of model performance, especially when the target classes are imbalanced.

## Key Findings

### 1. Differences Across Diabetes Categories

Some of the observed group averages were:

| Indicator | No Diabetes | Prediabetes | Diabetes |
|---|---:|---:|---:|
| Average BMI | 27.74 | 30.72 | 31.94 |
| High blood pressure (%) | 37.11 | 62.90 | 75.27 |
| High cholesterol (%) | 37.92 | 62.08 | 67.01 |
| Physical activity (%) | 77.91 | 67.85 | 63.05 |
| Poorer general health score | 2.37 | 2.98 | 3.29 |

The group with diabetes had higher average BMI and higher proportions reporting high blood pressure and high cholesterol than the group without diabetes.

The proportion reporting physical activity was lower in the diabetes group.

These are observed associations in the survey data and should not be interpreted as evidence of causation.

### 2. Model Performance

The Logistic Regression model achieved the following results on the test dataset:

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 64.58% |
| Balanced Accuracy | 52.42% |
| Macro F1-score | 42.69% |

### 3. Classification Report

| Category | Precision | Recall | F1-score |
|---|---:|---:|---:|
| No diabetes | 0.951 | 0.663 | 0.781 |
| Prediabetes | 0.033 | 0.326 | 0.059 |
| Diabetes | 0.353 | 0.583 | 0.440 |

The model performed better for the no-diabetes category than for the other two categories.

Its performance for prediabetes was particularly weak, with an F1-score of 0.059.

This highlights the difficulty of classifying a minority category when the dataset has a highly imbalanced target distribution.

## Understanding the Results

One important learning from this project was that a model with a seemingly reasonable accuracy score may still perform poorly for certain groups.

Although the model achieved 64.58% accuracy, its balanced accuracy and macro F1-score were considerably lower.

In a public health context, this matters because poor identification of minority groups can limit the usefulness of a prediction model.

The results show why model evaluation should consider different performance measures rather than relying only on overall accuracy.

## Project Outputs

The `results` folder contains:
- Analysed diabetes dataset
- Data quality summary
- Descriptive statistics
- Diabetes category distribution
- Group-wise health indicator summaries
- Correlation matrix and visualisation
- Health indicator comparison graphs
- Confusion matrix
- Classification report
- Model coefficients
- Saved Logistic Regression model
- Analysis notes

A detailed project report is also included in the repository.

## Public Health Relevance

Diabetes-related health indicators can provide useful information for population-level research and disease prevention planning.

Analysing factors such as BMI, blood pressure, cholesterol, physical activity and general health can help explore patterns associated with diabetes status.

Machine learning can also be used to study classification problems in healthcare. However, a model must be evaluated carefully, particularly when some health categories are underrepresented.

This project helped me understand both the potential and the limitations of applying machine learning to public health data.

## Limitations

- The dataset is based on US survey data from 2015 and does not represent the Indian population.
- The information is survey-based and includes self-reported health indicators.
- The dataset has a highly imbalanced target variable.
- Exact duplicate responses were retained because participant identities could not be verified.
- The model is a baseline Logistic Regression classifier and has not undergone clinical validation.
- The low prediabetes F1-score indicates limited classification performance for that category.
- The findings describe associations and do not establish causation.
- The model should not be used for individual diagnosis, screening decisions or treatment recommendations.

## Conclusion

This project helped me move from basic healthcare data exploration to applying machine learning techniques to a larger public health dataset.

I learned how to examine health indicators, identify class imbalance, prepare data for modelling and evaluate a classification model using multiple performance metrics.

One of the most important takeaways was that machine learning in healthcare is not simply about achieving a high accuracy score. It is equally important to understand which groups the model identifies correctly, where it makes mistakes and whether its performance is appropriate for the intended purpose.

This project strengthened my understanding of the role of data analysis and machine learning in population health research.

**This is an educational machine learning project. The model is not clinically validated and must not be used as a diagnostic or clinical decision-making tool.**
