# import pandas
import pandas as pd

# Load the final dataset
df = pd.read_csv("scaled_US_Accidents.csv")

print("Dataset Loaded Successfully!")
print(df.shape)

# 1. Missing Value Summary
print("\n========== Missing Value Summary ==========")

missing = df.isnull().sum()

missing = missing[missing > 0]

print(missing)

# 2. Duplicate Summary
print("\n========== Duplicate Summary ==========")

duplicates = df.duplicated().sum()

print("Duplicate Records:", duplicates)

# 3. Invalid Records
print("\n========== Invalid Records ==========")

invalid = df[
    (df["Start_Lat"] < -90) |
    (df["Start_Lat"] > 90) |
    (df["Start_Lng"] < -180) |
    (df["Start_Lng"] > 180)
]

print("Invalid Coordinate Records:", len(invalid))

# 4. Memory Usage
print("\n========== Memory Usage ==========")

memory = df.memory_usage(deep=True).sum() / 1024**2

print(f"Memory Usage: {memory:.2f} MB")

# 5. Feature Engineering Summary
print("\n========== Feature Engineering Summary ==========")

print("Total Engineered Features: 30")

print("""
Time Features
Weather Features
Geographic Features
Traffic Features
Text Features
""")

# 6. Final Dataset Statistics
print("\n========== Final Dataset Statistics ==========")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nData Types:")
print(df.dtypes.value_counts())

# 7. Save the report to a text file
with open("Data_Quality_Report.txt", "w") as file:
    file.write("US Accidents Dataset - Data Quality Report\n")
    file.write("=" * 50 + "\n")
    file.write(f"Rows: {df.shape[0]}\n")
    file.write(f"Columns: {df.shape[1]}\n")
    file.write(f"Duplicate Records: {duplicates}\n")
    file.write(f"Invalid Coordinates: {len(invalid)}\n")
    file.write(f"Memory Usage: {memory:.2f} MB\n")
    file.write("Engineered Features: 30\n")

print("\nData Quality Report Saved Successfully!")
 