# 1: Import Libraries
import pandas as pd
import numpy as np


# 2: Feature Engineering Function
def feature_engineering(df):

    print("Feature Engineering Started...")

    # 3: Convert Date Columns
    df["Start_Time"] = pd.to_datetime(
        df["Start_Time"],
        format="ISO8601",
        errors="coerce"
    )

    df["End_Time"] = pd.to_datetime(
        df["End_Time"],
        format="ISO8601",
        errors="coerce"
    )

    # PART A — Time Features

    # Feature 1 — Hour
    df["Hour"] = df["Start_Time"].dt.hour

    # Check:
    print(df[["Start_Time", "Hour"]].head())

    # Feature 2 — Day
    df["Day"] = df["Start_Time"].dt.day

    # Check:
    print(df["Day"].head())

    # Feature 3 — Month
    df["Month"] = df["Start_Time"].dt.month

    # Feature 4 — Quarter
    df["Quarter"] = df["Start_Time"].dt.quarter

    # Feature 5 — Weekday Number
    df["Weekday"] = df["Start_Time"].dt.dayofweek

    # Feature 6 — Weekend Flag
    df["Weekend_Flag"] = df["Weekday"].isin([5, 6]).astype(int)

    # Feature 7 — Rush Hour Indicator

    # Morning:
    # 7–9

    # Evening:
    # 4–6 PM
    df["Rush_Hour"] = (
        ((df["Hour"] >= 7) & (df["Hour"] <= 9)) |
        ((df["Hour"] >= 16) & (df["Hour"] <= 18))
    ).astype(int)

    # Feature 8 — Night Indicator
    df["Night"] = (
        (df["Hour"] < 6) |
        (df["Hour"] >= 20)
    ).astype(int)

    # Feature 9 — Holiday Indicator
    df["Holiday"] = 0

    # Check the features
    print(df[[
        "Hour",
        "Day",
        "Month",
        "Quarter",
        "Weekday",
        "Weekend_Flag",
        "Rush_Hour",
        "Night",
        "Holiday"
    ]].head())

    # Part B – Weather Features

    # Step 1
    # Feature 10 – Temperature Category
    df["Temperature_Category"] = pd.cut(
        df["Temperature(F)"],
        bins=[-100, 32, 60, 80, 150],
        labels=["Freezing", "Cold", "Moderate", "Hot"]
    )

    # Step 2 - Check the output
    print(df[["Temperature(F)", "Temperature_Category"]].head())

    # Feature 11 – Visibility Category
    df["Visibility_Category"] = pd.cut(
        df["Visibility(mi)"],
        bins=[0, 2, 5, 10, 100],
        labels=["Poor", "Low", "Good", "Excellent"]
    )

    # Check
    print(df[["Visibility(mi)", "Visibility_Category"]].head())

    # Feature 12 – Wind Category
    df["Wind_Category"] = pd.cut(
        df["Wind_Speed(mph)"],
        bins=[0, 10, 20, 40, 200],
        labels=["Calm", "Moderate", "Strong", "Very Strong"]
    )

    # Check
    print(df[["Wind_Speed(mph)", "Wind_Category"]].head())

    # Feature 13 – Rain Indicator
    df["Rain_Indicator"] = (
        df["Precipitation(in)"] > 0
    ).astype(int)

    # Check
    print(df[["Precipitation(in)", "Rain_Indicator"]].head())

    # Feature 14 – Severe Weather Indicator
    severe_weather = [
        "Thunderstorm",
        "Heavy Rain",
        "Snow",
        "Fog",
        "Hail",
        "Tornado"
    ]

    df["Severe_Weather"] = (
        df["Weather_Condition"]
        .astype(str)
        .str.contains(
            "|".join(severe_weather),
            case=False,
            na=False
        )
    ).astype(int)

    # Check
    print(df[["Weather_Condition", "Severe_Weather"]].head())

    # Feature 15 – State Frequency

    # Step 1
    state_freq = df["State"].value_counts()

    df["State_Frequency"] = df["State"].map(state_freq)

    # Step 2: Check the output
    print(df[["State", "State_Frequency"]].head())
    
        # Feature 16 – City Frequency

    # Step 1
    city_freq = df["City"].value_counts()

    df["City_Frequency"] = df["City"].map(city_freq)

    # Check
    print(df[["City", "City_Frequency"]].head())

    # Feature 17 – Distance Category

    # Step 1
    df["Distance_Category"] = pd.cut(
        df["Distance(mi)"],
        bins=[0, 1, 5, 10, 1000],
        labels=["Short", "Medium", "Long", "Very Long"]
    )

    # Step 2
    print(df[["Distance(mi)", "Distance_Category"]].head())

    # Feature 18 – Urban/Rural Flag

    # Step 1
    median_city_freq = df["City_Frequency"].median()

    df["Urban_Rural"] = (
        df["City_Frequency"] > median_city_freq
    ).astype(int)

    # Step 2
    print(df[["City", "City_Frequency", "Urban_Rural"]].head())

    # Feature 19 - State Code Length

    # Step 1
    df["State_Code_Length"] = (
        df["State"]
        .astype(str)
        .str.len()
    )

    # Step 2
    print(df[["State", "State_Code_Length"]].head())

    # Feature 20 – Accident Duration (Minutes)

    # Step 1
    df["Accident_Duration_Min"] = (
        df["End_Time"] - df["Start_Time"]
    ).dt.total_seconds() / 60

    # Step 2
    print(df[[
        "Start_Time",
        "End_Time",
        "Accident_Duration_Min"
    ]].head())

    # Feature 21 – Traffic Severity Score

    # Step 1
    df["Traffic_Severity_Score"] = df["Severity"] / 4

    # Step 2
    print(df[[
        "Severity",
        "Traffic_Severity_Score"
    ]].head())

    # Feature 22 – Road Complexity Score

    # Step 1
    road_features = [
        "Crossing",
        "Junction",
        "Railway",
        "Roundabout",
        "Stop"
    ]

    df["Road_Complexity_Score"] = (
        df[road_features]
        .astype(int)
        .sum(axis=1)
    )

    # Step 2
    print(df[
        road_features +
        ["Road_Complexity_Score"]
    ].head())

    # Feature 23 – Traffic Control Score

    # Step 1
    traffic_control = [
        "Traffic_Signal",
        "Traffic_Calming",
        "Stop"
    ]

    df["Traffic_Control_Score"] = (
        df[traffic_control]
        .astype(int)
        .sum(axis=1)
    )

    # Step 2
    print(df[
        traffic_control +
        ["Traffic_Control_Score"]
    ].head())

    # Feature 24 - Road Hazard Score

    # Step 1
    hazard_features = [
        "Bump",
        "Give_Way",
        "No_Exit",
        "Railway"
    ]

    df["Road_Hazard_Score"] = (
        df[hazard_features]
        .astype(int)
        .sum(axis=1)
    )

    # Step 2
    print(df[
        hazard_features +
        ["Road_Hazard_Score"]
    ].head())

    # Part E – Text Features

    # Step 1
    # Feature 25 - Description Length
    df["Description_Length"] = (
        df["Description"]
        .astype(str)
        .str.len()
    )

    # Step 2
    print(df[[
        "Description",
        "Description_Length"
    ]].head())

    # Feature 26 - Word Count

    # Step 1
    df["Word_Count"] = (
        df["Description"]
        .astype(str)
        .str.split()
        .str.len()
    )

    # Step 2
    print(df[[
        "Description",
        "Word_Count"
    ]].head())

    # Feature 27 – Average Word Length

    # Step 1
    df["Average_Word_Length"] = (
        df["Description_Length"] /
        df["Word_Count"]
    ).fillna(0)

    # Step 2
    print(df[[
        "Average_Word_Length"
    ]].head())

    # Feature 28 - Accident Keyword Indicator

    # Step 1
    accident_keywords = [
        "accident",
        "crash",
        "collision",
        "overturned",
        "blocked"
    ]

    df["Accident_Keyword"] = (
        df["Description"]
        .astype(str)
        .str.contains(
            "|".join(accident_keywords),
            case=False,
            na=False
        )
    ).astype(int)

    # Step 2
    print(df[[
        "Description",
        "Accident_Keyword"
    ]].head())

    # Feature 29 - Weather Keyword Indicator

    # Step 1
    weather_keywords = [
        "rain",
        "snow",
        "fog",
        "storm",
        "ice"
    ]

    df["Weather_Keyword"] = (
        df["Description"]
        .astype(str)
        .str.contains(
            "|".join(weather_keywords),
            case=False,
            na=False
        )
    ).astype(int)

    # Step 2
    print(df[[
        "Description",
        "Weather_Keyword"
    ]].head())

    # Feature 30 - Road Closure Keyword Indicator

    # Step 1
    closure_keywords = [
        "closed",
        "blocked",
        "lane",
        "shoulder",
        "detour"
    ]

    df["Road_Closure_Keyword"] = (
        df["Description"]
        .astype(str)
        .str.contains(
            "|".join(closure_keywords),
            case=False,
            na=False
        )
    ).astype(int)

    # Step 2
    print(df[[
        "Description",
        "Road_Closure_Keyword"
    ]].head())

    print("Feature Engineering Completed Successfully!")

    return df

