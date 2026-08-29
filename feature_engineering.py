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

    # Feature 2 — Day
    df["Day"] = df["Start_Time"].dt.day

    # Feature 3 — Month
    df["Month"] = df["Start_Time"].dt.month

    # Feature 4 — Quarter
    df["Quarter"] = df["Start_Time"].dt.quarter

    # Feature 5 — Weekday Number
    df["Weekday"] = df["Start_Time"].dt.dayofweek

    # Feature 6 — Weekend Flag
    df["Weekend_Flag"] = df["Weekday"].isin([5, 6]).astype(int)

    # Feature 7 — Rush Hour Indicator
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

    # PART B — Weather Features

    # Feature 10 — Temperature Category
    df["Temperature_Category"] = pd.cut(
        df["Temperature(F)"],
        bins=[-float("inf"), 32, 60, 80, float("inf")],
        labels=[
        "Freezing",
        "Cold",
        "Moderate",
        "Hot"
    ]
).astype("object").fillna("Unknown")


    # Feature 11 — Visibility Category
    df["Visibility_Category"] = pd.cut(
     df["Visibility(mi)"],
    bins=[-float("inf"), 2, 5, 10, float("inf")],
    labels=[
        "Poor",
        "Low",
        "Good",
        "Excellent"
    ]
).astype("object").fillna("Unknown")


    # Feature 12 — Wind Category
    df["Wind_Category"] = pd.cut(
        df["Wind_Speed(mph)"],
    bins=[-float("inf"), 10, 20, 40, float("inf")],
    labels=[
        "Calm",
        "Moderate",
        "Strong",
        "Very Strong"
    ]
).astype("object").fillna("Unknown")

    # Feature 13 — Rain Indicator
    df["Rain_Indicator"] = (
        df["Precipitation(in)"] > 0
    ).astype(int)

    # Feature 14 — Severe Weather Indicator
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

    # Feature 15 — State Frequency
    state_freq = df["State"].value_counts()

    df["State_Frequency"] = df["State"].map(
        state_freq
    )

    # Feature 16 — City Frequency
    city_freq = df["City"].value_counts()

    df["City_Frequency"] = df["City"].map(
        city_freq
    )

    # Feature 17 — Distance Category
    df["Distance_Category"] = pd.cut(
        df["Distance(mi)"],
        bins=[-1, 1, 5, 10, float("inf")],
        labels=[
            "Short",
            "Medium",
            "Long",
            "Very Long"
        ]
    )

    # Fill missing distance categories
    df["Distance_Category"] = (
        df["Distance_Category"]
        .astype("object")
        .fillna("Unknown")
    )

    # Feature 18 — Urban/Rural Flag
    median_city_freq = df["City_Frequency"].median()

    df["Urban_Rural"] = (
        df["City_Frequency"] > median_city_freq
    ).astype(int)

    # Feature 19 — State Code Length
    df["State_Code_Length"] = (
        df["State"]
        .astype(str)
        .str.len()
    )

    # Feature 20 — Accident Duration (Minutes)
    df["Accident_Duration_Min"] = (
        df["End_Time"] - df["Start_Time"]
    ).dt.total_seconds() / 60

    # Feature 21 — Traffic Severity Score
    df["Traffic_Severity_Score"] = (
        df["Severity"] / 4
    )

    # Feature 22 — Road Complexity Score
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

    # Feature 23 — Traffic Control Score
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

    # Feature 24 — Road Hazard Score
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

    # PART E — Text Features

    # Feature 25 — Description Length
    df["Description_Length"] = (
        df["Description"]
        .astype(str)
        .str.len()
    )

    # Feature 26 — Word Count
    # Memory-efficient word counting
    df["Word_Count"] = (
        df["Description"]
        .astype("string")
        .str.count(r"\S+")
        .fillna(0)
        .astype("int32")
)

    # Feature 27 — Average Word Length
    # Feature 27 — Average Word Length
    df["Average_Word_Length"] = (
        df["Description_Length"] /
        df["Word_Count"].replace(0, np.nan)
).fillna(0)

    # Feature 28 — Accident Keyword Indicator
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

    # Feature 29 — Weather Keyword Indicator
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

    # Feature 30 — Road Closure Keyword Indicator
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

    print("Feature Engineering Completed Successfully!")

    return df