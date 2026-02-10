import main


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

def data_analysis(df):
    # Total number of trips, total distance traveled, and average trip duration
    total_trips = len(df)
    total_distance = df["distance_km"].sum()
    average_duration = (df["end_time"] - df["start_time"]).mean()

    #  top 10 most popular start stations and end stations
    # value_counts(ascending=True) 总结出现的次数，默认从高到低排列，ascending=True升序排列
    top_start_stations = df["start_station_id"].value_counts().head(10).index.tolist()
    top_end_stations = df["end_station_id"].value_counts().head(10).index.tolist()

    # What are the peak usage hours during the day? -> dataframe series
    peak_usage_hours = df.groupby(df["start_time"].dt.hour).size().sort_values(ascending=False).head(10)

    # What is the average trip distance by user type (casual vs. member)?
    average_distance_by_user_type = round(df.groupby("user_type")["distance_km"].mean(),2)
    average_distance_casual = average_distance_by_user_type.get("casual", 0)
    average_distance_member = average_distance_by_user_type.get("member", 0)   

    # the bike utilization rate (percentage of time bikes are in use vs. available)
    # 一辆自行车，一天24小时的时间，如果用了7小时，那么剩下的17小时就是可用时间，时间利用率就是7/24 = 0.29
    total_usage_minutes = df["duration_minutes"].sum()
    avg_usage_hours_per_bike = (total_usage_minutes / 60) / df["bike_id"].nunique()
    bike_utilization_rate = round((avg_usage_hours_per_bike / 24)*100, 2)7

    # Show the monthly trip trend over time — is ridership growing?


    data_analysis_results = {
        "total_trips": total_trips,
        "total_distance": total_distance,
        "average_duration": average_duration,
        "top_start_stations": top_start_stations,
        "top_end_stations": top_end_stations,
        "peak_usage_hours": peak_usage_hours,
        "average_distance_casual": average_distance_casual,
        "average_distance_member": average_distance_member,
        "bike_utilization_rate": bike_utilization_rate
        }
    
    return data_analysis_results


