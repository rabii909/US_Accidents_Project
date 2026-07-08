# 1: Import libraries
import pandas as pd
from sklearn.preprocessing import (
    MinMaxScaler,
    StandardScaler,
    RobustScaler,
    MaxAbsScaler
)


# 2: Scaling Function
def scale_data(df):

    print("Scaling Started...")

    # 3: Choose numeric columns
    numeric_columns = [
        "Temperature(F)",
        "Visibility(mi)",
        "Wind_Speed(mph)",
        "Distance(mi)"
    ]

    # 4: Check the original values
    print(df[numeric_columns].head())

    # 5: Min-Max Scaling
    minmax_scaler = MinMaxScaler()

    df_minmax = df.copy()

    df_minmax[numeric_columns] = minmax_scaler.fit_transform(
        df_minmax[numeric_columns]
    )

    print("Min-Max Scaling")
    print(df_minmax[numeric_columns].head())

    # 6: Standard Scaling
    standard_scaler = StandardScaler()

    df_standard = df.copy()

    df_standard[numeric_columns] = standard_scaler.fit_transform(
        df_standard[numeric_columns]
    )

    print("\nStandard Scaling")
    print(df_standard[numeric_columns].head())

    # 7: Robust Scaling
    robust_scaler = RobustScaler()

    df_robust = df.copy()

    df_robust[numeric_columns] = robust_scaler.fit_transform(
        df_robust[numeric_columns]
    )

    print("\nRobust Scaling")
    print(df_robust[numeric_columns].head())

    # 8: Max Absolute Scaling
    maxabs_scaler = MaxAbsScaler()

    df_maxabs = df.copy()

    df_maxabs[numeric_columns] = maxabs_scaler.fit_transform(
        df_maxabs[numeric_columns]
    )

    print("\nMax Absolute Scaling")
    print(df_maxabs[numeric_columns].head())

    print("\nScaling Completed Successfully!")

    # 9: Return Final Dataset
    return df_maxabs