# 1: Import libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


# 2: Encoding Function
def encode_data(df):

    print("Encoding Started...")

    # 3: Check categorical columns
    categorical_cols = df.select_dtypes(include=["object", "string"]).columns

    print("Categorical Columns:")
    print(categorical_cols)

    # 4: Label Encoding

    # Weather_Condition
    label_encoder = LabelEncoder()

    df["Weather_Label"] = label_encoder.fit_transform(
        df["Weather_Condition"].astype(str)
    )

    print(df[["Weather_Condition", "Weather_Label"]].head())

    # ------------------------------------
    # One-Hot Encoding
    # ------------------------------------

    # 5: Check unique values in Source
    print(df["Source"].unique())

    # One-Hot Encoding for Source
    source_encoded = pd.get_dummies(
        df["Source"],
        prefix="Source"
    )

    # 6: View the encoded columns
    print(source_encoded.head())

    # 7: Add the new columns to the dataset
    df = pd.concat([df, source_encoded], axis=1)

    # 8: Check the final result
    print(df.head())
    print(df.filter(like="Source_").head())

    print("One-Hot Encoding Completed Successfully!")

    # ------------------------------------
    # Frequency Encoding
    # ------------------------------------

    # 9: Create a frequency table

    # Frequency Encoding - State
    state_frequency = df["State"].value_counts()

    print(state_frequency.head())

    # 10: Create the encoded column
    df["State_Frequency_Encoded"] = (
        df["State"].map(state_frequency)
    )

    # 11: Check the result
    print(df[[
        "State",
        "State_Frequency_Encoded"
    ]].head())

    print("Frequency Encoding Completed Successfully!")

    # 12: Return Encoded Dataset
    return df