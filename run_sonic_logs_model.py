from src.modules.data_loader import *
from src.modules.data_cleaning import *
from src.modules.data_transform import *
from src.modules.split_data import *
from src.modules.build_model_test import *
from util import *

# create list of wells to be used for analysis
files = ['volve_field_data/15_9-F-11A.LAS', 'volve_field_data/16_5-3.las', 'volve_field_data/25_10-9.las', 'volve_field_data/34_11-1.las', 
         'volve_field_data/35_4-1.las', 'volve_field_data/35_11-10.las', 'volve_field_data/35_11-11.las']

def run_sonic_logs_model (data=files):
    
    # load the dataset
    wells = load_all_wells (data)
    
    # clean the dataset
    trim_list = trim_wells(wells)
    wells = data_cleaning(trim_list, wells)
    
    # data transformation
    total_well = data_transformation(wells)
    
    # data splitting
    train_x, train_y, test_x, test_y = data_splitting(wells, total_well)
    # print (len(train_x))
    # print(len(train_y))
    # print(len(test_x))
    # print(len(test_y))
    
    # build, train and test model
    model = train_model(train_x, train_y)
    
    
    # evaluate model on test data
    test_prediction, metrics = predict_evaluate(model, test_x, test_y)
    
    
    
if __name__ == "__main__":
    run_sonic_logs_model()  
    
    
    
    