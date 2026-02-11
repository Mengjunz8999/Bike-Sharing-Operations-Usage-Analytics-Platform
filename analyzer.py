import pandas as pd

'''
1. Total number of trips, total distance traveled, and average trip duration
2. What are the top 10 most popular start stations and end stations?
3. What are the peak usage hours during the day?
4. Which day of the week has the highest trip volume?
5. What is the average trip distance by user type (casual vs. member)?
6. What is the bike utilization rate (percentage of time bikes are in use vs. available)?
7. Show the monthly trip trend over time — is ridership growing?
8. Who are the top 15 most active users by trip count?
9. What is the total maintenance cost per bike type (classic vs. electric)?
10. What are the most common station-to-station routes (top 10 origin–destination pairs)?
11. What is the trip completion rate (completed vs. cancelled trips)?
12. What is the average number of trips per user, segmented by user type?
13. Which bikes have the highest maintenance frequency?
14. Identify outlier trips (unusually long/short duration or distance) using statistical methods
'''

data_analysis_results = {}

def tripsdata_analysis(df) -> dict:
    # Total number of trips, total distance traveled, and average trip duration
    total_trips = len(df)
    total_distance = df["distance_km"].sum()
    average_duration = (df["end_time"] - df["start_time"]).mean()

    #  top 10 most popular start stations and end stations
    # value_counts(ascending=True) 总结出现的次数，默认从高到低排列，ascending=True升序排列
    top_start_stations = df["start_station_id"].value_counts().head(10).index.tolist()
    top_end_stations = df["end_station_id"].value_counts().head(10).index.tolist()

    # What are the peak usage hours during the day? -> dataframe series
    # .size() 可以在这里理解成groupby的count方法
    peak_usage_hours = df.groupby(df["start_time"].dt.hour).size().sort_values(ascending=False).head(10)

    # What is the average trip distance by user type (casual vs. member)?
    # casual    7.52
    # member    7.79
    average_distance_by_user_type = df.groupby("user_type")["distance_km"].mean().round(2)
    average_distance_casual = average_distance_by_user_type.loc["casual"]
    average_distance_member = average_distance_by_user_type.loc["member"]   

    # the bike utilization rate (percentage of time bikes are in use vs. available)
    # 一辆自行车，一天24小时的时间，如果用了7小时，那么剩下的17小时就是可用时间，时间利用率就是7/24 = 0.29
    total_usage_minutes = df["duration_minutes"].sum()
    avg_usage_hours_per_bike = (total_usage_minutes / 60) / df["bike_id"].nunique()
    bike_utilization_rate = ((avg_usage_hours_per_bike / 24)*100).round(2)

    # Show the monthly trip trend over time — is ridership growing/////////////////

    # top 15 most active users by trip count?
    active_users_top_15 = df["user_id"].value_counts().head(15).index.tolist()

    # the most common station-to-station routes (top 10 origin–destination pairs)
    station_to_station_top10 = df.groupby(["start_station_id","end_station_id"]).size().sort_values(ascending=False).head(10)

    # trip completion rate (completed vs. cancelled trips)
    # completed / all , cancelled / all -> pass auf, trips_data_all include nan and duplication
    trips_data_all = pd.read_csv("data/trips.csv")
    # return true, ture is 1, so it cann be sum
    trips_cancelled_count = (trips_data_all["status"] == "cancelled").sum()
    trips_completed_count = (trips_data_all["status"] == "completed").sum()
    trips_cancelled_rate = (trips_cancelled_count / len(trips_data_all) * 100).round(2)
    trips_completed_rate = (trips_completed_count / len(trips_data_all) * 100).round(2)
    
    # the average number of trips per user, segmented by user type?
    total_trips = (trips_data_all.groupby("user_type")["user_id"].count())  # 每种 user_type 的总行程数
    avg_trips = (trips_data_all.groupby("user_type")["user_id"].nunique())  # 每种 user_type 的独立用户数
    avg_trips_casual = (total_trips["casual"]/avg_trips["casual"]).round(2) # 总casual骑行数 / casual 类里的独立用户数
    avg_trips_member = (total_trips["member"]/avg_trips["member"]).round(2) # 总member骑行数 / member 类里的独立用户数

    # outlier trips (unusually duration)
    # 把duration 这列的数据按顺序排序，排在25%的某个数值，Q1就是这个数值，如果只用df["duration"].quantile(0.5)，只能检测中间数，不能显示宽度
    Q1 = df["duration_minutes"].quantile(0.25)
    Q3 = df["duration_minutes"].quantile(0.75)
    IQR = Q3 - Q1
    IQR = round(IQR,2)

    #这个是固定的计算方法 Q1: 6.2,Q3: 33.7 ,lower_bound: -35.05,upper_bound: 74.95
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # 找出异常行程 ，df[true] -> dataframe
    outliers_duration = df[(df["duration_minutes"] < lower_bound) | (df["duration_minutes"] > upper_bound)]

    data_analysis_results.update({
        "total_trips": total_trips,
        "total_distance": total_distance,
        "average_duration": average_duration,
        "top_start_stations": top_start_stations,
        "top_end_stations": top_end_stations,
        "peak_usage_hours": peak_usage_hours,
        "average_distance_by_user_type":average_distance_by_user_type,
        "average_distance_casual": average_distance_casual,
        "average_distance_member": average_distance_member,
        "bike_utilization_rate": bike_utilization_rate,
        "active_users_top_15": active_users_top_15,
        "station_to_station_top10":station_to_station_top10,
        "trips_cancelled_rate":trips_cancelled_rate,
        "trips_completed_rate" : trips_completed_rate,
        "total_trips":total_trips,
        "avg_trips":avg_trips,
        "avg_trips_casual":avg_trips_casual,
        "avg_trips_member":avg_trips_member,
        "outliers_duration":outliers_duration # dataframe，first row，original dataframe index
        })
    
    return data_analysis_results



def maintenance_data_analysis(df):
    # total maintenance cost per bike type (classic vs. electric)
    maintenance_cost = round(df.groupby("bike_type")["cost"].sum(),2)
    maintenance_cost_classic = maintenance_cost.loc["classic"]
    maintenance_cost_electric = maintenance_cost.loc["electric"]

    # highest maintenance frequency
    maintenance_frequency = df["maintenance_type"].value_counts()
    highest_maintenance_frequency = maintenance_frequency.index[0]

    data_analysis_results.update(
        {"maintenance_cost_classic": maintenance_cost_classic, #float
        "maintenance_cost_electric":maintenance_cost_electric, #float
        "maintenance_frequency":maintenance_frequency, # count from every maintenance tpye
        "highest_maintenance_frequency":highest_maintenance_frequency, # pandas.Series
        
        }
    )

    return data_analysis_results

