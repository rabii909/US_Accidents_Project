# Import Libraries
import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("data/US_Accidents_March23.csv")

# Check Dataset
print(df.head())

# Dataset Shape
print(df.shape)

# Basic Information
print(df.info())

# Task 1: Data Audit

# 1. Missing Values
#code
missing = df.isnull().sum()
print(missing)

# percentage
missing_percent = (df.isnull().sum() / len(df)) * 100
print(missing_percent)

# save
missing.to_csv("missing_values.csv")
 
 # 2. Duplicate Records
 
# find duplicates
duplicates = df.duplicated().sum()
print("Duplicate Rows:", duplicates)

# if needed
duplicate_rows = df[df.duplicated()]
duplicate_rows.to_csv("duplicates.csv", index=False)

# 3. Memory Usage
print(df.memory_usage(deep=True))

# total memory 
memory = df.memory_usage(deep=True).sum()
print("Memory:", memory / 1024**2, "MB")

# 4. Incorrect Data Types
# check
print(df.dtypes)
# convert 
df["Start_Time"] = pd.to_datetime(df["Start_Time"], errors="coerce")
df["End_Time"] = pd.to_datetime(df["End_Time"], errors="coerce")
# check again
print (df.dtypes)

# 5. Invalid Coordinates
# Latitude should be
# -90 to 90
# Longitude
# -180 to 180
# Find invalid values
invalid = df[
    (df["Start_Lat"] < -90) |
    (df["Start_Lat"] > 90) |
    (df["Start_Lng"] < -180) |
    (df["Start_Lng"] > 180)
]

print(invalid.shape)

# save 
invalid.to_csv("invalid_coordinates.csv", index=False)

# 6. Date/Time Inconsistencies
# End time should be after Start time.
# Find wrong rows
wrong_time = df[df["End_Time"] < df["Start_Time"]]
print(wrong_time.shape)
# save
wrong_time.to_csv("wrong_time.csv", index=False)

# 7. High Cardinality Columns
# These are columns having many unique values.
cardinality = df.nunique()
print(cardinality)
#sort 
print(cardinality.sort_values(ascending=False))

# 8. Rare Categories
#Check every categorical column
categorical = df.select_dtypes(include="object")
# loop
for col in categorical.columns:
    print("\n", col)
    print(df[col].value_counts().tail())
    
# 9. Constant Columns
# Columns having only one value.
constant = []

for col in df.columns:
    if df[col].nunique() == 1:
        constant.append(col)

print(constant)

# 10. Low Variance Features
# Mostly for numeric columns.
numeric = df.select_dtypes(include=np.number)
# variance
variance = numeric.var()
print(variance)
# low variance
low_variance = variance[variance < 0.01]
print(low_variance)

# Step 11: Save Audit Report
# Create
report = {
    "Rows": len(df),
    "Columns": len(df.columns),
    "Duplicate Rows": duplicates,
    "Memory (MB)": memory / 1024**2,
    "Invalid Coordinates": len(invalid),
    "Wrong Dates": len(wrong_time)
}

report_df = pd.DataFrame(report.items(), columns=["Metric", "Value"])

report_df.to_csv("audit_report.csv", index=False)