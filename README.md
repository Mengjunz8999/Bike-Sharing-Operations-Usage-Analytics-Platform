# Bike-Sharing-Operations-Usage-Analytics-Platform

This data Analytics system is for sharing-bick trip records, station usage, fleet maintenance logs, and user activity.

# Function list

'''
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
'''

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

# Bike Sharing Operations & Usage Analytics Platform — Frontend

Admin dashboard built with React, TypeScript, Vite, and Tailwind CSS. Corresponds to the Factory Pattern backend (`factories.py`).

## Project Structure

```
frontend/
├── src/
│   ├── main.tsx              # Entry point
│   ├── App.tsx               # Main page with filter logic
│   ├── types.ts              # TypeScript types (mirrors backend model.py)
│   ├── index.css             # Global styles + Tailwind directives
│   ├── components/
│   │   ├── BikeCard.tsx      # Bike card (ClassicBike / ElectricBike)
│   │   ├── UserCard.tsx      # User card (CasualUser / MemberUser)
│   │   └── StatsBar.tsx      # Top statistics bar
│   └── data/
│       └── mockData.ts       # Mock data — replace with API calls later
├── index.html
├── package.json
├── vite.config.ts
├── tailwind.config.js
├── postcss.config.js
└── tsconfig.app.json
```

## Features

- 🚲 **Bikes tab** — View all bikes, filter by type (classic / electric) and status (available / rented / maintenance)
- 👤 **Users tab** — View all users, filter by type (casual / member); members show tier and membership start date
- 📊 **Stats bar** — Total bikes, available bikes, total users, member count
- 🔍 **Search** — Search by bike ID or user name / email

## Getting Started

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

## Tech Stack

- [React 18](https://react.dev/)
- [TypeScript](https://www.typescriptlang.org/)
- [Vite 7](https://vite.dev/)
- [Tailwind CSS v3](https://tailwindcss.com/)

## React modules call direction

index.html -> main.tsx -> app.tsx ...

## Connecting to the Backend

Data currently comes from `src/data/mockData.ts`. Once `create_user()` in `factories.py` is implemented, replace the mock data with real `fetch` calls to your API.
