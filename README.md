# Bike-Sharing-Operations-Usage-Analytics-Platform

This data Analytics system is for sharing-bick trip records, station usage, fleet maintenance logs, and user activity.

# Function list

utils.py
|- data clean
analyzer.py
|- analysis methods

# Data Model

trips.csv：
trip_id,
user_id,
user_type,
bike_id,
bike_type,
start_station_id,
end_station_id,
start_time,
end_time,
duration_minutes,
distance_km,
status

stations.csv：
station_id,
station_name,
capacity,
latitude,
longitude

maintenance.csv：
record_id,
bike_id,
bike_type,
date,
maintenance_type,
cost,
description
