import utils
import analyzer


def main():
    valid_stationsdata,valid_tripsdata = utils.check_and_load_clean_data()
    
    result = analyzer.data_analysis(valid_tripsdata)
    print(f"average_distance_casual Results:{result["average_distance_casual"]}")
    print(f"average_distance_member Results:{result["average_distance_member"]}")
    print(f"bike_utilization_rate:{result["bike_utilization_rate"]}")
    
   


if __name__ == "__main__":
    main()