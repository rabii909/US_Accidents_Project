# US Accidents Dataset - Real-World Data Engineering Challenge

## Project Overview

This project focuses on preprocessing and feature engineering using the US Accidents Dataset. The objective is to transform a large, noisy, real-world dataset into a clean, analysis-ready dataset using professional data engineering techniques.

No machine learning model is used in this project. The main focus is on data preprocessing, feature engineering, encoding, scaling, validation, and pipeline development.

---

## Dataset

Dataset Used:

**US Accidents (March 2023)**

The dataset contains millions of accident records collected across the United States.

---

## Project Tasks

### Task 1 – Data Audit

* Missing value analysis
* Duplicate record detection
* Invalid coordinate detection
* Data type checking
* Memory usage analysis
* Data quality assessment

### Task 2 – Data Cleaning

* Missing value handling
* Duplicate removal
* Datetime conversion
* Coordinate validation
* Text normalization
* Outlier removal
* Impossible value removal

### Task 3 – Feature Engineering

Created more than 25 engineered features including:

* Time Features
* Weather Features
* Geographic Features
* Traffic Features
* Text Features

### Task 4 – Encoding

Implemented:

* Label Encoding
* One-Hot Encoding
* Frequency Encoding

Also discussed:

* Target Encoding
* Hash Encoding

### Task 5 – Scaling

Compared:

* Min-Max Scaling
* Standard Scaling
* Robust Scaling
* Max Absolute Scaling

The final preprocessing pipeline uses Max Absolute Scaling.

### Task 6 – Data Quality Report

Generated a report containing:

* Missing value summary
* Duplicate summary
* Invalid records
* Memory optimization
* Feature engineering summary
* Final dataset statistics

### Task 7 – Pipeline Development

Developed a reusable preprocessing pipeline that:

* Loads raw data
* Cleans the dataset
* Performs feature engineering
* Encodes categorical variables
* Scales numerical features
* Validates the processed dataset
* Exports a production-ready CSV file

---

# Project Structure

```
US_Accidents_Project/
│
├── data/
│   └── US_Accidents_March23.csv
│
├── audit.py
├── clean_data.py
├── feature_engineering.py
├── encoding.py
├── scaling.py
├── pipeline.py
│
├── cleaned_US_Accidents.csv
├── feature_engineered_US_Accidents.csv
├── encoded_US_Accidents.csv
├── scaled_US_Accidents.csv
├── production_ready_US_Accidents.csv
│
├── audit_report.csv
├── missing_values.csv
├── duplicates.csv
├── invalid_coordinates.csv
├── wrong_time.csv
│
└── README.md
```

---

# Python Libraries Used

* pandas
* numpy
* scikit-learn

---

# How to Run

1. Create and activate a virtual environment.
2. Install the required libraries.
3. Place the dataset in the `data` folder.
4. Run:

```
python pipeline.py
```

---

# Output Files

The project generates:

* cleaned_US_Accidents.csv
* feature_engineered_US_Accidents.csv
* encoded_US_Accidents.csv
* scaled_US_Accidents.csv
* production_ready_US_Accidents.csv

---

# Project Outcome

The project successfully transforms the raw US Accidents dataset into a clean, feature-engineered, encoded, scaled, validated, and production-ready dataset using a reusable preprocessing pipeline.
