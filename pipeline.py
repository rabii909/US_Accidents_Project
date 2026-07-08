# 1: Import libraries
import pandas as pd

# 2: Import reusable modules
from sklearn.preprocessing import MaxAbsScaler
from feature_engineering import feature_engineering
from encoding import encode_data

# 3: Create reusable functions

# Function 1 - Load Data
def load_data():

    df = pd.read_csv("cleaned_US_Accidents.csv")

    print("Dataset Loaded Successfully!")

    return df


# Function 2 - Validation
def validate_data(df):

    print("\nValidation Report")
    print("-" * 40)

    print("Rows:", df.shape[0])

    print("Columns:", df.shape[1])

    print("Missing Values:")

    print(df.isnull().sum().sum())

    print("Duplicate Rows:")

    print(df.duplicated().sum())

    return df

# Function 3 - Final Scaling
def final_scaling(df):

    print("Applying Final Max Absolute Scaling...")

    numeric_columns = [
        "Temperature(F)",
        "Visibility(mi)",
        "Wind_Speed(mph)",
        "Distance(mi)"
    ]

    scaler = MaxAbsScaler()

    df[numeric_columns] = scaler.fit_transform(
        df[numeric_columns]
    )

    print("Final Scaling Completed!")

    return df

# Function 3 - Save the Dataset
def save_data(df):

    df.to_csv(
        "production_ready_US_Accidents.csv",
        index=False
    )

    print("Production-ready dataset saved successfully!")


# Function 4 - Main Function
def main():

    # Load Dataset
    df = load_data()

    # Feature Engineering
    df = feature_engineering(df)

    # Encoding
    df = encode_data(df)

    # Scaling
    df = final_scaling(df)

    # Validate Final Dataset
    df = validate_data(df)

    # Save Final Dataset
    save_data(df)


# Run the Pipeline
if __name__ == "__main__":
    main()

