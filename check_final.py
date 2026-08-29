import pandas as pd

print("Checking final dataset...")

missing_total = 0

for chunk in pd.read_csv(
    "production_ready_US_Accidents.csv",
    chunksize=100000
):
    missing = chunk.isnull().sum()

    for column, count in missing.items():
        if count > 0:
            cols_count = f"{column}: {count}"
            print(cols_count)

    missing_total += missing.sum()

print("\nTotal Missing Values:", missing_total)

if missing_total == 0:
    print("SUCCESS: Final dataset has no missing values!")
else:
    print("WARNING: Missing values still exist.")