import pandas as pd

# Read only the first 100,000 rows
df = pd.read_csv(
    "production_ready_US_Accidents.csv",
    nrows=100000
)

# Save as a smaller dashboard dataset
df.to_csv(
    "dashboard_data.csv",
    index=False
)

print("Dashboard dataset created successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))