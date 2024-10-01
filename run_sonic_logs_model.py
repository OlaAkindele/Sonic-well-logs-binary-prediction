# import all files

from src.modules.data_loader import *
from src.modules.data_cleaning import *
from src.modules.data_transform import *
from src.modules.split_data import *
from src.modules.build_model_test import *
from util import *

import argparse
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import petrolib  # Petrophysical evaluation package

from petrolib.file_reader import load_las
from petrolib.plots import plotLog, plotLogs
from petrolib.procs import set_alias

# create list of wells to be used for analysis
files = ['volve_field_data/15_9-F-11A.LAS', 'volve_field_data/16_5-3.las', 'volve_field_data/25_10-9.las', 'volve_field_data/34_11-1.las', 
         'volve_field_data/35_4-1.las', 'volve_field_data/35_11-10.las', 'volve_field_data/35_11-11.las']

def parse_arguments():
    """
    Parses command-line arguments.

    Returns:
    - args (Namespace): Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Sonic Logs Models")
    # parser.add_argument('--data', type=str, default= files, help="Path to the dataset las file.")
    # parser.add_argument('--plotLogs', action='store_true', help="Flag to plot the plotLogs results.")
    return parser.parse_args()

def run_sonic_logs_model ():
    
    args = parse_arguments()

    
    # load the dataset
    wells = load_all_wells (files)
    
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
    
    # plot the confusion matrices
    # if args.plotLogs:
    #     plotLogs(wells[6], depth='DEPTH', logs=['GR', 'RT', 'RHOB', 'NPHI', ['DTC', 'Pred DTC'], ['DTS', 'Pred DTS']], 
    #      top=min(wells[6]['DEPTH']), bottom=max(wells[6]['DEPTH']), figsize=(16,16), title='well7 : 35_11-11')
    
    
    
if __name__ == "__main__":
    run_sonic_logs_model()  
    
    
    
    