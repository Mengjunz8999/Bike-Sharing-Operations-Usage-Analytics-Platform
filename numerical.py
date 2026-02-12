"""
NumPy-based numerical computations for the CityBike platform.

Students should implement:
    - Station distance matrix using Euclidean distance
    - Vectorized trip statistics (mean, median, std, percentiles)
    - Outlier detection using z-scores
    - Vectorized fare calculation across all trips
"""

import numpy as np
import pandas as pd
 
# ---------------------------------------------------------------------------
# Distance calculations
# ---------------------------------------------------------------------------

def station_distance_matrix(latitudes: np.ndarray, longitudes: np.ndarray) -> np.ndarray:

    """ 计算两站之间的距离
    formula: np.sqrt(lat_diff**2 + lon_diff**2)
    """
    # Step 1: compute pairwise latitude differences
    # lat_diff = latitudes[:, np.newaxis] - latitudes[np.newaxis, :]

    # Step 2: compute pairwise longitude differences
    # lon_diff = ...

    # Step 3: combine with Euclidean formula
    # np.sqrt(lat_diff**2 + lon_diff**2)
    if len(latitudes) != len(longitudes):
        raise ValueError("Latitude and longitude counts do not match and will lead to incorrect data calculations.")
    
    latitudes = np.array(latitudes)
    longitudes = np.array(latitudes)

    # reshape 成列向量，: 切片选取，这里是所有的index，newaxis [1,2,3] ->[[1],[2],[3]]
    lat_col = latitudes[:, np.newaxis]  # (n,1)
    lon_col = longitudes[:, np.newaxis] # (n,1)

    # pairwise 差值
    lat_diff = lat_col - latitudes      # shape (n,n)
    lon_diff = lon_col - longitudes     # shape (n,n)

    # 欧氏距离
    dist_matrix = np.sqrt(lat_diff**2 + lon_diff**2)

    return dist_matrix

# ---------------------------------------------------------------------------
#  Distance calculations Test
# ---------------------------------------------------------------------------
# dist_matrix_ST100_ST103 = station_distance_matrix([48.892607,48.839528,48.818887],[9.259799,9.216875,9.200056])
# print("------------test result--------------")
# print(f"dist_matrix_ST100_ST103:\n {dist_matrix_ST100_ST103}")
# print("-------------end test result----------")
'''
------------test result--------------
dist_matrix_ST100_ST103:
 [[0.         0.07506504 0.10425582]
 [0.07506504 0.         0.02919078]
 [0.10425582 0.02919078 0.        ]]
-------------end test result----------
'''
# latitudes: np.ndarray, longitudes: np.ndarray
def min_max_distance() -> np.ndarray:
    # return dataframe
    station_df = pd.read_csv("data/stations_clean.csv")
    latitude = station_df["latitude"]
    longitude = station_df["longitude"]

    stations_matrix = station_distance_matrix(latitude,longitude)

    # 把 n 维变成 1 维， return np.array, 所以可以做向量比较
    flat = stations_matrix.flatten()
    flat_nonzero = flat[flat > 0]
    
    # 找最小和最大值
    min_dist = flat_nonzero.min()
    max_dist = flat_nonzero.max()

    # 原矩阵中的位置: 计算公式，比如min的index在flat是 5，而 matrix：3x3，那么它在matrix是5//3=1，5%3=2，matrix的index（1，2）
    # np.array 没有index，需要list找
    min_index = flat.tolist().index(min_dist)
    max_index = flat.tolist().index(max_dist)

    # 转回二维坐标 (i, j)，i行号，j列号，e.g arr(i,j) ,divmod(a, b) -> (a // b, a % b)
    n = stations_matrix.shape[0]
    min_i, min_j = divmod(min_index, n)
    max_i, max_j = divmod(max_index, n)

    # min_i df中的行号，再取此行的列名就可以找到某值
    print("-----------------------------------------------------")
    print("min_dist:", min_dist)
    print("min_dist_stations:", station_df.iloc[min_i]["station_id"], station_df.iloc[min_j]["station_id"])

    print("max_dist:", max_dist)
    print("max_dist_stations:", station_df.iloc[max_i]["station_id"], station_df.iloc[max_j]["station_id"])
    print("-----------------------------------------------------")

    print(stations_matrix)

min_max_distance()


# ---------------------------------------------------------------------------
# Trip statistics
# ---------------------------------------------------------------------------

def trip_duration_stats(durations: np.ndarray) -> dict[str, float]:
    """Compute summary statistics for trip durations.

    Args:
        durations: 1-D array of trip durations in minutes.

    Returns:
        Dict with keys: mean, median, std, p25, p75, p90.

    TODO: use NumPy functions (np.mean, np.median, np.std, np.percentile).
    """
    # Example (partially done):
    return {
        "mean": float(np.mean(durations)),
        "median": float(np.median(durations)),
        "std": float(np.std(durations)),
        # TODO: add p25, p75, p90 using np.percentile
    }


# ---------------------------------------------------------------------------
# Outlier detection
# ---------------------------------------------------------------------------

def detect_outliers_zscore(
    values: np.ndarray, threshold: float = 3.0
) -> np.ndarray:
    """Identify outlier indices using the z-score method.

    An observation is an outlier if |z| > threshold.

    Args:
        values: 1-D array of numeric values.
        threshold: Z-score cutoff (default 3.0).

    Returns:
        Boolean array — True where the value is an outlier.

    TODO: compute z-scores and return the boolean mask.

    Hints:
        1. Compute the mean:  mean = np.mean(values)
        2. Compute the std:   std  = np.std(values)
        3. Guard against std == 0 (return all-False array)
        4. Compute z-scores:  z = (values - mean) / std
        5. Return boolean:    np.abs(z) > threshold
    """

    raise NotImplementedError("detect_outliers_zscore")


# ---------------------------------------------------------------------------
# Vectorized fare calculation
# ---------------------------------------------------------------------------

def calculate_fares(
    durations: np.ndarray,
    distances: np.ndarray,
    per_minute: float,
    per_km: float,
    unlock_fee: float = 0.0,
) -> np.ndarray:
    """Calculate fares for many trips at once using NumPy.

    Args:
        durations: 1-D array of trip durations (minutes).
        distances: 1-D array of trip distances (km).
        per_minute: Cost per minute.
        per_km: Cost per km.
        unlock_fee: Flat unlock fee (default 0).

    Returns:
        1-D array of trip fares.

    TODO: implement a single vectorized expression (no loops).

    Hints:
        The fare for a single trip is:
            fare = unlock_fee + (per_minute * duration) + (per_km * distance)

        With NumPy, you can compute this for ALL trips at once because
        arithmetic on arrays is element-wise:
            fares = unlock_fee + per_minute * durations + per_km * distances

        This single line replaces a Python for-loop over every trip.

    Example:
        >>> durations = np.array([10, 20, 30])
        >>> distances = np.array([2.0, 5.0, 8.0])
        >>> calculate_fares(durations, distances, per_minute=0.15, per_km=0.10, unlock_fee=1.0)
        array([2.7, 4.5, 6.3])
        # trip 1: 1.0 + 0.15*10 + 0.10*2.0 = 2.70
        # trip 2: 1.0 + 0.15*20 + 0.10*5.0 = 4.50
        # trip 3: 1.0 + 0.15*30 + 0.10*8.0 = 6.30
    """

    raise NotImplementedError("calculate_fares")