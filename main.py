import utils
import analyzer


def main():
    maintenance_data_copy,valid_stationsdata,valid_tripsdata = utils.check_and_load_clean_data()
    
    # Analysis result
    analyzer.maintenance_data_analysis(maintenance_data_copy)
    analyzer.tripsdata_analysis(valid_tripsdata)
    analyzer.data_analysis_report(analyzer.data_analysis_results)

  

if __name__ == "__main__":
    main()  