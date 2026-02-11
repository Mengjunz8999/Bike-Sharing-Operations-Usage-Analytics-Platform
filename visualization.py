"""
Matplotlib visualizations for the CityBike platform.

Students should create at least 4 charts:
    1. Bar chart — trips per station or revenue by user type
    2. Line chart — monthly trip trend over time
    3. Histogram — trip duration or distance distribution
    4. Box plot — duration by user type or bike type

All charts must have: title, axis labels, legend (where applicable).
Export each chart as PNG to output/figures/.
"""

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# __file__当前文件，- .resolve() → 转成绝对路径
FIGURES_DIR = Path(__file__).resolve().parent / "output" / "figures"

# resolve() → 转成绝对路径， parent → 当前文件所在的文件夹
def _save_figure(fig: plt.Figure, filename: str) -> None:
    """Save a Matplotlib figure to the figures directory."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    filepath = FIGURES_DIR / filename
    fig.savefig(filepath, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {filepath}")


# ---------------------------------------------------------------------------
# 1. Bar chart (provided as example)
# ---------------------------------------------------------------------------

def plot_trips_per_station(trips: pd.DataFrame, stations: pd.DataFrame) -> None:
    """Bar chart showing the number of trips starting at each station.

    Args:
        trips: Cleaned trips DataFrame.
        stations: Stations DataFrame (for station names).
    """
    counts = (
        trips["start_station_id"]
        .value_counts()
        .head(10)
        .rename_axis("station_id")
        .reset_index(name="trip_count")
    )
    merged = counts.merge(
        stations[["station_id", "station_name"]],
        on="station_id",
        how="left",
    )

    #fig, 即代表整张图像，整图的大小，布局，保存，ax，真正画图的地方，x/y轴，标题，刻度，颜色..
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(merged["station_name"], merged["trip_count"], color="steelblue")
    ax.set_xlabel("Number of Trips")
    ax.set_ylabel("Station")
    ax.set_title("Top 10 Start Stations by Trip Count")
    ax.invert_yaxis()
    _save_figure(fig, "trips_per_station.png")


# ---------------------------------------------------------------------------
# 2. Line chart — monthly trend
# ---------------------------------------------------------------------------

def plot_monthly_trend(trips: pd.DataFrame) -> None:
    """Line chart of monthly trip counts.

    TODO:
        - Extract year-month from start_time
        - Group and count
        - Plot a line chart
        - Save as 'monthly_trend.png'
    """
    # Period 类型不能直接用于 Matplotlib 的 x 轴, index 是value_counts的列，所以这里是时间
    #  peak_usage_hours = peak_df.reset_index(name = "counts") 这里改过名，回头在研究一下吧
    monthly_counts = (
    trips["start_time"]
        .dt.to_period("M")
        .value_counts()
        .sort_index()
        .reset_index()
        .rename(columns={"start_time": "year_month", "count": "trip_count"})
)
    
    monthly_counts["year_month"] = monthly_counts["year_month"].astype(str)

    fig, ax = plt.subplots(figsize=(10, 5))
    # marker="o" 在页面加点
    ax.plot(monthly_counts["year_month"], monthly_counts["trip_count"], marker="o",color="blue")
    ax.set_title("Monthly Trip Count in 2024")
    ax.set_xlabel("Year - Month")
    ax.set_ylabel("Trip Counts")
    
    _save_figure(fig, "monthly_trip_counts.png")
    
    # for test
    # return monthly_counts  

  

# ---------------------------------------------------------------------------
# 3. Histogram — trip duration distribution
# ---------------------------------------------------------------------------

def plot_duration_histogram(trips: pd.DataFrame) -> None:
    """Histogram of trip durations.

    TODO:
        - Use trips["duration_minutes"]
        - Choose an appropriate number of bins bins:区间数量
        - Add title, axis labels
        - Save as 'duration_histogram.png'
    """
    durations = trips["duration_minutes"]

    fig, ax = plt.subplots(figsize=(10, 5))

    # bins = (max - min)/30 ,在这里（200 -0）/30
    ax.hist(durations, bins=30, color="steelblue", edgecolor="white")
    ax.set_title("Distribution of Trip Durations")
    ax.set_xlabel("Duration - Minutes")
    ax.set_ylabel("Number of Trips")
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    _save_figure(fig, "duration_histogram.png")



# ---------------------------------------------------------------------------
# 4. Box plot — duration by user type
# ---------------------------------------------------------------------------

def plot_duration_by_user_type(trips: pd.DataFrame) -> None:
    """Box plot comparing trip durations across user types.

    TODO:
        - Group data by user_type
        - Create side-by-side box plots
        - Add title, axis labels
        - Save as 'duration_by_user_type.png'
    """

    fig, ax = plt.subplots(figsize=(10, 5))

    # - patch_artist=True → 允许填充颜色,- boxprops → 设置箱子的颜色,ax -> 用我的ax，不是新建
    # 
    trips.boxplot(
        column="duration_minutes",
        by="user_type",
        ax=ax,
        grid=False,
        patch_artist=True,
        boxprops=dict(facecolor="lightsteelblue")
    )

    ax.set_title("Trip Duration by User Type")
    ax.set_xlabel("User Type")
    ax.set_ylabel("Duration (minutes)")

    # 去掉 pandas 自动加的副标题
    plt.suptitle("")

    _save_figure(fig, "duration_by_user_type.png")

  