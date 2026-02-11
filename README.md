# Bike-Sharing-Operations-Usage-Analytics-Platform

This data Analytics system is for sharing-bick trip records, station usage, fleet maintenance logs, and user activity.

# Function list

Bike-Sharing-Operations-Usage-Analytics-Platform
├─ analyzer.py #analysis methods, analysis report export to file
├─ data
│ ├─ maintenance.csv #source data
│ ├─ stations.csv #source data
│ ├─ stations_clean.csv # just like file name
│ ├─ trips.csv #source data
│ └─ trips_clean.csv # just like file name
├─ factories.py #create entities
├─ generate_datasets.py # this is where the source data come from
├─ main.py # i think i don`t need to explain this
├─ model.py #OOP classes: Entity, Bike, Station, CasualUser, MemberUser, Trip, MaintenanceRecord
├─ output
│ ├─ figures #data visualization files
│ │ ├─ duration_by_user_type.png
│ │ ├─ duration_histogram.png
│ │ ├─ monthly_trip_counts.png
│ │ └─ trips_per_station.png
│ ├─ summary_report.txt #tons of analysis data
│ ├─ top_stations.csv # juse like file name
│ └─ top_users.csv # juse like file name
├─ README.md
├─ requirements.txt #dependencies
├─ utils.py #data clean
└─ visualization.py #data visualization & export .png files

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
