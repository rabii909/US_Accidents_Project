# ============================================================
# US ACCIDENTS ANALYTICS DASHBOARD
# Professional Data Engineering & Analytics Application
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="US Accidents Analytics",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------------------------------------------------- */
    /* MAIN BACKGROUND */
    /* ---------------------------------------------------- */

    .stApp {
        background:
            linear-gradient(
                135deg,
                #f8fafc 0%,
                #eef2f7 100%
            );
    }


    /* ---------------------------------------------------- */
    /* HIDE STREAMLIT DEFAULT ELEMENTS */
    /* ---------------------------------------------------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ---------------------------------------------------- */
    /* SIDEBAR */
    /* ---------------------------------------------------- */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #111827 0%,
                #1f2937 100%
            );
    }

    section[data-testid="stSidebar"] * {
        color: #ffffff;
    }


    /* ---------------------------------------------------- */
    /* HERO SECTION */
    /* ---------------------------------------------------- */

    .hero-container {
        background:
            linear-gradient(
                135deg,
                #111827,
                #2563eb
            );

        padding: 35px 40px;
        border-radius: 20px;

        color: white;

        margin-bottom: 25px;

        box-shadow:
            0 10px 30px
            rgba(0,0,0,0.15);
    }


    .hero-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }


    .hero-subtitle {
        font-size: 18px;
        opacity: 0.85;
    }


    /* ---------------------------------------------------- */
    /* KPI CARDS */
    /* ---------------------------------------------------- */

    .kpi-card {

        background: white;

        padding: 22px;

        border-radius: 18px;

        border:
            1px solid
            rgba(0,0,0,0.06);

        box-shadow:
            0 6px 20px
            rgba(0,0,0,0.06);

        transition:
            0.2s;

        min-height: 120px;
    }


    .kpi-card:hover {

        transform:
            translateY(-4px);

        box-shadow:
            0 12px 25px
            rgba(0,0,0,0.10);
    }


    .kpi-icon {
        font-size: 25px;
    }


    .kpi-label {

        font-size: 14px;

        color:
            #6b7280;

        margin-top:
            8px;
    }


    .kpi-value {

        font-size:
            30px;

        font-weight:
            800;

        color:
            #111827;
    }


    /* ---------------------------------------------------- */
    /* SECTION TITLE */
    /* ---------------------------------------------------- */

    .section-title {

        font-size:
            24px;

        font-weight:
            750;

        color:
            #111827;

        margin-top:
            20px;

        margin-bottom:
            15px;
    }


    /* ---------------------------------------------------- */
    /* INSIGHT CARDS */
    /* ---------------------------------------------------- */

    .insight-card {

        background:
            white;

        padding:
            20px;

        border-radius:
            15px;

        border-left:
            5px solid
            #2563eb;

        box-shadow:
            0 4px 15px
            rgba(0,0,0,0.05);
    }


    /* ---------------------------------------------------- */
    /* DATAFRAME */
    /* ---------------------------------------------------- */

    div[data-testid="stDataFrame"] {

        border-radius:
            12px;

        overflow:
            hidden;
    }


    /* ---------------------------------------------------- */
    /* BUTTON */
    /* ---------------------------------------------------- */

    .stButton > button {

        border-radius:
            10px;

        border:
            none;

        padding:
            10px 20px;

        font-weight:
            600;
    }


    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    file_path = "production_ready_US_Accidents.csv"

    df = pd.read_csv(
        file_path,
        nrows=100000
    )

    # Convert dates safely
    if "Start_Time" in df.columns:

        df["Start_Time"] = pd.to_datetime(
            df["Start_Time"],
            errors="coerce"
        )

    if "End_Time" in df.columns:

        df["End_Time"] = pd.to_datetime(
            df["End_Time"],
            errors="coerce"
        )

    return df


df = load_data()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    # 🚗 US Accidents

    ### Analytics Platform

    Explore real-world accident data
    through interactive analytics.
    """
)

st.sidebar.markdown("---")


page = st.sidebar.radio(
    "NAVIGATION",
    [
        "🏠 Dashboard",
        "🔎 Data Explorer",
        "📊 Project Overview"
    ]
)


st.sidebar.markdown("---")


st.sidebar.markdown(
    """
    ### ⚙️ Data Pipeline

    ✓ Data Cleaning

    ✓ Data Validation

    ✓ Feature Engineering

    ✓ Encoding

    ✓ Scaling
    """
)


st.sidebar.markdown("---")

st.sidebar.caption(
    "Professional Data Engineering Project"
)


# ============================================================
# FILTER FUNCTION
# ============================================================

def apply_filters(data):

    filtered_data = data.copy()

    st.sidebar.markdown("## 🎛️ Filters")

    # --------------------------------------------------------
    # STATE
    # --------------------------------------------------------

    if "State" in filtered_data.columns:

        states = sorted(
            filtered_data["State"]
            .dropna()
            .astype(str)
            .unique()
        )

        selected_states = st.sidebar.multiselect(
            "🗺️ State",
            states
        )

        if selected_states:

            filtered_data = filtered_data[
                filtered_data["State"]
                .astype(str)
                .isin(selected_states)
            ]


    # --------------------------------------------------------
    # SEVERITY
    # --------------------------------------------------------

    if "Severity" in filtered_data.columns:

        severity_options = sorted(
            filtered_data["Severity"]
            .dropna()
            .unique()
        )

        selected_severity = st.sidebar.multiselect(
            "⚠️ Severity",
            severity_options
        )

        if selected_severity:

            filtered_data = filtered_data[
                filtered_data["Severity"]
                .isin(selected_severity)
            ]


    # --------------------------------------------------------
    # YEAR
    # --------------------------------------------------------

    if "Start_Time" in filtered_data.columns:

        years = sorted(
            filtered_data["Start_Time"]
            .dropna()
            .dt.year
            .unique()
        )

        selected_years = st.sidebar.multiselect(
            "📅 Year",
            years
        )

        if selected_years:

            filtered_data = filtered_data[
                filtered_data["Start_Time"]
                .dt.year
                .isin(selected_years)
            ]


    return filtered_data


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    # --------------------------------------------------------
    # HERO
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="hero-container">

        <div class="hero-title">
        🚗 US ACCIDENTS ANALYTICS
        </div>

        <div class="hero-subtitle">
        Real-World Data Engineering Dashboard
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # APPLY FILTERS
    # ========================================================

    filtered_df = apply_filters(df)


    # ========================================================
    # KPI CARDS
    # ========================================================

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-icon">
            🚗
            </div>

            <div class="kpi-label">
            Total Accidents
            </div>

            <div class="kpi-value">
            {len(filtered_df):,}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        avg_severity = (
            filtered_df["Severity"].mean()
            if "Severity" in filtered_df.columns
            else 0
        )

        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-icon">
            ⚠️
            </div>

            <div class="kpi-label">
            Average Severity
            </div>

            <div class="kpi-value">
            {avg_severity:.2f}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        total_states = (
            filtered_df["State"].nunique()
            if "State" in filtered_df.columns
            else 0
        )

        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-icon">
            🗺️
            </div>

            <div class="kpi-label">
            States Covered
            </div>

            <div class="kpi-value">
            {total_states}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col4:

        total_cities = (
            filtered_df["City"].nunique()
            if "City" in filtered_df.columns
            else 0
        )

        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-icon">
            🏙️
            </div>

            <div class="kpi-label">
            Cities
            </div>

            <div class="kpi-value">
            {total_cities:,}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("<br>", unsafe_allow_html=True)


    # ========================================================
    # CHART ROW 1
    # ========================================================

    col1, col2 = st.columns(2)


    # --------------------------------------------------------
    # ACCIDENT TRENDS
    # --------------------------------------------------------

    with col1:

        st.markdown(
            '<div class="section-title">📈 Accident Trends</div>',
            unsafe_allow_html=True
        )

        if "Start_Time" in filtered_df.columns:

            trend_data = (
                filtered_df
                .dropna(subset=["Start_Time"])
                .copy()
            )

            trend_data["Year"] = (
                trend_data["Start_Time"]
                .dt.year
            )

            trend_data = (
                trend_data
                .groupby("Year")
                .size()
                .reset_index(name="Accidents")
            )

            fig = px.line(
                trend_data,
                x="Year",
                y="Accidents",
                markers=True
            )

            fig.update_layout(
                height=350,
                margin=dict(
                    l=20,
                    r=20,
                    t=20,
                    b=20
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # --------------------------------------------------------
    # SEVERITY DISTRIBUTION
    # --------------------------------------------------------

    with col2:

        st.markdown(
            '<div class="section-title">📊 Severity Distribution</div>',
            unsafe_allow_html=True
        )

        if "Severity" in filtered_df.columns:

            severity_data = (
                filtered_df["Severity"]
                .value_counts()
                .sort_index()
                .reset_index()
            )

            severity_data.columns = [
                "Severity",
                "Accidents"
            ]

            fig = px.bar(
                severity_data,
                x="Severity",
                y="Accidents",
                text="Accidents"
            )

            fig.update_layout(
                height=350,
                margin=dict(
                    l=20,
                    r=20,
                    t=20,
                    b=20
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # ========================================================
    # CHART ROW 2
    # ========================================================

    col1, col2 = st.columns(2)


    # --------------------------------------------------------
    # ACCIDENTS BY STATE
    # --------------------------------------------------------

    with col1:

        st.markdown(
            '<div class="section-title">🗺️ Top States</div>',
            unsafe_allow_html=True
        )

        if "State" in filtered_df.columns:

            state_data = (
                filtered_df["State"]
                .value_counts()
                .head(10)
                .reset_index()
            )

            state_data.columns = [
                "State",
                "Accidents"
            ]

            fig = px.bar(
                state_data,
                x="Accidents",
                y="State",
                orientation="h"
            )

            fig.update_layout(
                height=400,
                margin=dict(
                    l=20,
                    r=20,
                    t=20,
                    b=20
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # --------------------------------------------------------
    # WEATHER CONDITIONS
    # --------------------------------------------------------

    with col2:

        st.markdown(
            '<div class="section-title">🌦️ Weather Conditions</div>',
            unsafe_allow_html=True
        )

        if "Weather_Condition" in filtered_df.columns:

            weather_data = (
                filtered_df["Weather_Condition"]
                .value_counts()
                .head(10)
                .reset_index()
            )

            weather_data.columns = [
                "Weather",
                "Accidents"
            ]

            fig = px.pie(
                weather_data,
                names="Weather",
                values="Accidents",
                hole=0.45
            )

            fig.update_layout(
                height=400
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # ========================================================
    # MAP
    # ========================================================

    st.markdown(
        '<div class="section-title">📍 Accident Locations</div>',
        unsafe_allow_html=True
    )

    if (
        "Start_Lat" in filtered_df.columns
        and "Start_Lng" in filtered_df.columns
    ):

        map_data = (
            filtered_df[
                ["Start_Lat", "Start_Lng"]
            ]
            .dropna()
            .head(5000)
        )

        map_data = map_data.rename(
            columns={
                "Start_Lat": "lat",
                "Start_Lng": "lon"
            }
        )

        st.map(map_data)


    # ========================================================
    # RECENT ACCIDENTS
    # ========================================================

    st.markdown(
        '<div class="section-title">📋 Recent Accidents</div>',
        unsafe_allow_html=True
    )

    display_columns = [
        "Start_Time",
        "Severity",
        "State",
        "City",
        "Weather_Condition",
        "Distance(mi)",
        "Description"
    ]

    available_columns = [
        column
        for column in display_columns
        if column in filtered_df.columns
    ]

    recent_df = filtered_df.copy()

    if "Start_Time" in recent_df.columns:

        recent_df = recent_df.sort_values(
            "Start_Time",
            ascending=False
        )

    st.dataframe(
        recent_df[
            available_columns
        ].head(100),
        use_container_width=True,
        height=400
    )


    # ========================================================
    # INSIGHTS
    # ========================================================

    st.markdown(
        '<div class="section-title">💡 Key Insights</div>',
        unsafe_allow_html=True
    )

    insight_col1, insight_col2, insight_col3 = st.columns(3)


    with insight_col1:

        st.markdown(
            f"""
            <div class="insight-card">

            <b>Total Records</b>

            <h2>
            {len(filtered_df):,}
            </h2>

            accidents available for analysis.

            </div>
            """,
            unsafe_allow_html=True
        )


    with insight_col2:

        if "State" in filtered_df.columns:

            top_state = (
                filtered_df["State"]
                .value_counts()
                .idxmax()
            )

            st.markdown(
                f"""
                <div class="insight-card">

                <b>Highest Accident State</b>

                <h2>
                {top_state}
                </h2>

                has the highest number of accidents.

                </div>
                """,
                unsafe_allow_html=True
            )


    with insight_col3:

        if "Severity" in filtered_df.columns:

            highest_severity = (
                filtered_df["Severity"]
                .value_counts()
                .idxmax()
            )

            st.markdown(
                f"""
                <div class="insight-card">

                <b>Most Common Severity</b>

                <h2>
                {highest_severity}
                </h2>

                is the most frequent severity level.

                </div>
                """,
                unsafe_allow_html=True
            )


    st.markdown("---")

    st.caption(
        "🚗 US Accidents Analytics Platform | "
        "Python • Pandas • Streamlit • Plotly"
    )


# ============================================================
# DATA EXPLORER
# ============================================================

elif page == "🔎 Data Explorer":

    st.title("🔎 Data Explorer")

    st.write(
        "Explore and analyze the processed accident dataset."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Rows",
        f"{len(df):,}"
    )

    col2.metric(
        "Columns",
        len(df.columns)
    )

    col3.metric(
        "Missing Values",
        f"{df.isnull().sum().sum():,}"
    )


    st.markdown("---")


    selected_columns = st.multiselect(
        "Select Columns",
        options=df.columns.tolist(),
        default=df.columns.tolist()[:10]
    )


    if selected_columns:

        st.dataframe(
            df[selected_columns],
            use_container_width=True,
            height=500
        )


    st.markdown("---")


    st.download_button(
        "⬇️ Download Data Sample",
        data=df.head(10000).to_csv(index=False),
        file_name="US_Accidents_sample.csv",
        mime="text/csv"
    )


# ============================================================
# PROJECT OVERVIEW
# ============================================================

elif page == "📊 Project Overview":

    st.title("📊 Project Overview")

    st.subheader(
        "🚗 US Accidents Data Engineering Project"
    )

    st.write(
        """
        This project demonstrates a complete data engineering
        workflow using a large real-world US traffic accident
        dataset.
        """
    )


    st.markdown("### 🔄 Data Pipeline")

    st.markdown(
        """
        **1️⃣ Data Quality Analysis**

        ↓

        **2️⃣ Data Cleaning**

        ↓

        **3️⃣ Feature Engineering**

        ↓

        **4️⃣ Categorical Encoding**

        ↓

        **5️⃣ Numerical Scaling**

        ↓

        **6️⃣ Data Validation**

        ↓

        **7️⃣ Production-Ready Dataset**

        ↓

        **8️⃣ Interactive Analytics Dashboard**
        """
    )


    st.markdown("### 🛠️ Technologies")

    tech1, tech2, tech3, tech4 = st.columns(4)

    tech1.info("🐍 Python")
    tech2.info("🐼 Pandas")
    tech3.info("🎈 Streamlit")
    tech4.info("📊 Plotly")


    st.success(
        "🚀 Production-ready data pipeline successfully integrated with an interactive analytics dashboard!"
    )