# Project: Sales Exploratory Data Analysis (EDA)

## Overview
This project demonstrates a standard end-to-end Exploratory Data Analysis (EDA) pipeline. Using a synthetically generated sales dataset, the script handles data cleaning, statistical profiling, and business-focused trend analysis.

## Business Questions Answered
- **What is the total revenue performance?** Calculation of aggregate top-line revenue.
- **Which products and regions drive growth?** Segmentation analysis to identify high-performing assets and territories.
- **What are the sales trends over time?** Month-over-month (MoM) growth calculations to identify seasonality and momentum.
- **Are there data anomalies?** Using the Interquartile Range (IQR) method to statistically flag outliers that might indicate fraud, entry errors, or massive "whale" transactions.

## Key Features
- **Automated Data Generation**: Generates 1,000+ rows of realistic transaction data using `numpy`.
- **Data Integrity Checks**: Scans for and handles missing values and data type inconsistencies.
- **Revenue Intelligence**: Provides a breakdown of revenue by product, region, and month.
- **Statistical Outlier Detection**: Implementation of IQR to maintain data quality.

## Insights Surfaced
The final report provides a clean, executive-level summary of the business's health, allowing decision-makers to quickly identify which products to scale and which regions require more attention.
