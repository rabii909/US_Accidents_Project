# 1. Import Libraries
import pandas as pd
import numpy as np


# 2. Cleaning Function
def clean_data(df):

    print("Cleaning Started...")

    # 3. Make a Backup
    df_clean = df.copy()

    # 4. Handle Missing Values (Multiple Strategies)

    # A. Numerical columns → Fill with median
    numeric_cols = df_clean.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())

    # B. Categorical columns → Fill with mode
    categorical_cols = df_clean.select_dtypes(include=["object", "string"]).columns

    for col in categorical_cols:
        if not df_clean[col].mode().empty:
            df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

    # C. Datetime columns
    df_clean["Start_Time"] = pd.to_datetime(
        df_clean["Start_Time"],
        format="ISO8601",
        errors="coerce"
    )

    df_clean["End_Time"] = pd.to_datetime(
        df_clean["End_Time"],
        format="ISO8601",
        errors="coerce"
    )

    df_clean["Start_Time"] = df_clean["Start_Time"].ffill()
    df_clean["End_Time"] = df_clean["End_Time"].ffill()

    # 5. Remove Duplicates
    before = len(df_clean)
    # Remove duplicate accident IDs
    df_clean = df_clean.drop_duplicates(subset="ID")
    after = len(df_clean)
    print("Duplicates Removed:", before - after)

    # 6. Datetime Conversion
    print(df_clean.dtypes)

    # 7. Timezone Handling
    print("Start_Time Timezone:", df_clean["Start_Time"].dt.tz)
    print("End_Time Timezone:", df_clean["End_Time"].dt.tz)

    # 8. Coordinate Validation
    df_clean = df_clean[
        (df_clean["Start_Lat"] >= -90) &
        (df_clean["Start_Lat"] <= 90) &
        (df_clean["Start_Lng"] >= -180) &
        (df_clean["Start_Lng"] <= 180)
    ]

    # 9. Text Normalization
    text_cols = ["City", "County", "State"]

    for col in text_cols:
        df_clean[col] = (
            df_clean[col]
            .astype(str)
            .str.strip()
            .str.title()
        )

    # 10. Category Standardization
    # Display all column names
    print(df_clean.columns.tolist())

    # 11. Outlier Detection
    Q1 = df_clean["Distance(mi)"].quantile(0.25)
    Q3 = df_clean["Distance(mi)"].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df_clean = df_clean[
        (df_clean["Distance(mi)"] >= lower) &
        (df_clean["Distance(mi)"] <= upper)
    ]

    # 12. Remove Impossible Values
    df_clean = df_clean[df_clean["Distance(mi)"] >= 0]

    df_clean = df_clean[df_clean["Severity"].between(1, 4)]

    df_clean = df_clean[
        df_clean["End_Time"] >= df_clean["Start_Time"]
    ]

    print("Cleaning Completed Successfully!")

    # 13. Return Clean Dataset
    return df_clean