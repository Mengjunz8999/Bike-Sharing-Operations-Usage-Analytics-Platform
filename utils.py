import pandas as pd
import os

class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()
    
    def drop_nan(self):
        self.df = self.df.dropna()
        return self
    
    def drop_duplicates(self):
        self.df = self.df.drop_duplicates()
        return self
    
    def filter_status(self, status: str):
        self.df = self.df[self.df["status"] == status]
        return self

    def get_cleaned_data(self):
        return self.df

def load_data(path):
    """加载原始数据"""
    maintenance_df = pd.read_csv(path["maintenance"])
    stations_df = pd.read_csv(path["stations"])
    trips_df = pd.read_csv(path["trips"])
    return maintenance_df, stations_df, trips_df


def load_clean_data() -> pd.DataFrame:
    """数据清理函数"""
    path = {
        "maintenance": "data/maintenance.csv",
        "stations": "data/stations.csv",
        "trips": "data/trips.csv",
        "stations_clean":"data/stations_clean.csv",
        "trips_clean":"data/trips_clean.csv"
    }

    maintenance_df, stations_df, trips_df = load_data(path)
    print(f"-------------maintenance Before-----------------------:\n{maintenance_df.dtypes}")
    print(f"-------------trips Before-----------------------:\n{trips_df.dtypes}")
    print(f"-------------station Before-----------------------:\n{stations_df.dtypes}")

    # 修复日期格式
    maintenance_df["date"] = pd.to_datetime(maintenance_df["date"], errors="coerce")
    trips_df["start_time"] = pd.to_datetime(trips_df["start_time"], errors="coerce")
    trips_df["end_time"] = pd.to_datetime(trips_df["end_time"], errors="coerce")

    print(f"-------------maintenance After-----------------------:\n{maintenance_df.dtypes}")
    print(f"-------------trips After-----------------------:\n{trips_df.dtypes}")
    

    # 数据清理
    valid_stationsdata = DataCleaner(stations_df).drop_nan().drop_duplicates().get_cleaned_data()
    valid_tripsdata = DataCleaner(trips_df).drop_nan().drop_duplicates().filter_status("completed").get_cleaned_data()

    valid_stationsdata.to_csv(path["stations_clean"], index=False)
    valid_tripsdata.to_csv(path["trips_clean"], index=False)

    # print(valid_stationsdata.info())
    # print(valid_tripsdata.info())
    return maintenance_df.copy(),valid_stationsdata, valid_tripsdata
# load_clean_data()

# 需要时才调用：load_clean_data()
def check_and_load_clean_data():
    """检查清理后的数据文件是否存在"""
    trips_clean_path = "data/trips_clean.csv"
    stations_clean_path = "data/stations_clean.csv"
    maintenance_data_path = "data/maintenance.csv"
    
    if os.path.exists(trips_clean_path) and os.path.exists(stations_clean_path):
        print("✓ The cleaned data file already exists; just load it directly....")
        valid_stationsdata = pd.read_csv(stations_clean_path)
        valid_tripsdata = pd.read_csv(trips_clean_path)
        maintenance_copy = pd.read_csv(maintenance_data_path)
        # 转换datetime列
        valid_tripsdata["start_time"] = pd.to_datetime(valid_tripsdata["start_time"], errors="coerce")
        valid_tripsdata["end_time"] = pd.to_datetime(valid_tripsdata["end_time"], errors="coerce")
        return maintenance_copy,valid_stationsdata, valid_tripsdata
    else:
        print("✗ The cleaned data file does not exist; data cleaning is now in progress ...")
        return load_clean_data()