import pandas as pd



#data clearing and create a clean data file
path ={
    "maintenance": "data/maintenance.csv",
    "stations": "data/stations.csv",
    "trips": "data/trips.csv",
    "valid_stationsdata":"data/stations_clean.csv",
    "valid_tripsdata":"data/trips_clean.csv"
}

def load_data()-> pd.Dataframe:
        maintenance_df = pd.read_csv(path["maintenance"])
        stations_df = pd.read_csv(path["stations"])
        trips_df = pd.read_csv(path["trips"])

        return maintenance_df, stations_df, trips_df

maintenance_df, stations_df, trips_df = load_data()
# print(f"Data loaded successfully:")
# print(f"check data type (before):\nmaintenance:\n{maintenance_df.dtypes}\n\nstations:\n{stations_df.dtypes}\n\ntrips:\n{trips_df.dtypes}")
#pack 3 variables into a tuple and print the type of the tuple
# print(type(load_data()))

#fix date format ， errors="coerce" will convert invalid parsing to NaT
maintenance_df["date"] = pd.to_datetime(maintenance_df["date"], errors="coerce")
trips_df["start_time"] = pd.to_datetime(trips_df["start_time"], errors="coerce")
trips_df["end_time"] = pd.to_datetime(trips_df["end_time"], errors="coerce")

# print(f"check data type (after):\nmaintenance:\n{maintenance_df.dtypes}\n\nstations:\n{stations_df.dtypes}\n\ntrips:\n{trips_df.dtypes}")

class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()
    
    def drop_nan(self):
        self.df = self.df.dropna()
        return self
    
    def drop_duplicates(self):
        self.df = self.df.drop_duplicates()
        return self
    
    def filter_status(self,status:str):
        self.df = self.df[self.df["status"] == status]
        return self

    def get_cleaned_data(self):
        return self.df
    
data_cleaner_stationdata = DataCleaner(stations_df)
data_cleaner_tripdata =DataCleaner(trips_df)
valid_stationsdata  = data_cleaner_stationdata.drop_nan().drop_duplicates().get_cleaned_data()
valid_tripsdata = data_cleaner_tripdata.drop_nan().drop_duplicates().filter_status("completed").get_cleaned_data()

valid_stationsdata.to_csv("data/stations_clean.csv", index=False)
valid_tripsdata.to_csv("data/trips_clean.csv", index=False)

print(valid_stationsdata.info())
print(valid_tripsdata.info())

# print(f"cleaned data info:\nmaintenance:\n{maintenance_df.info()}\n\nstations:\n{stations_df.info()}\n\ntrips:\n{trips_df.info()}")


    

    
    
              
               


   