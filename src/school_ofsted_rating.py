import sys
sys.path.append("./src/library")
sys.path.append("./src/models")
sys.path.append("./src/tabulate")
from timeit import default_timer as timer
from datetime import timedelta
from matplotlib import pyplot as plt
import numpy as np

# import project libraries
from constants import *
from dataset import Dataset
from rating_model import RatingModel

class SchoolRating(object):
    def __init__(self):
        self._logger = f'::{self.__class__.__name__}::'
        self._dataset = None
        self._rating_model = None
        self._classification = CLASSIFICATION
        # self.get_classification
        self._initialise()
        
    def get_classification(self):
        return self._classification

    def get_dataset(self):
        return self._dataset.get_dataset()

    def get_dataset_features(self):
        return self._dataset.get_dataset_features()

    def get_dataset_inputs(self):
        return self._dataset.get_x_inputs()

    def get_dataset_output(self):
        return self._dataset.get_y_output()

    def get_models(self, model_type = None):
        return self._rating_model.get_models(model_type)

    def get_training_set(self):
        return self._dataset.get_training_set()

    def get_test_set(self):
        return self._dataset.get_test_set()

    def get_y_test(self):
        return self._dataset.get_y_test()

    def build_model(self, model_type):
        self._rating_model.build_model(model_type)

    def convert_object_variables(self):
        self._dataset.convert_object_variables()

    def drop_unwanted_columns(self):
        self._dataset.drop_unwanted_columns()

    def encode_rating_catogory(self):
       self._dataset.encode_rating_catogory()

    def evaluate_model(self):
        self._rating_model.evaluate_model()
        
    def report_dataset_vitals(self, level='all'):
        self._dataset.report_dataset_vitals(level)
        self._print_classification()

    def run_data_balance(self):
        self._dataset.run_data_balance()
        self._rating_model.clear_model()

    def show_confusion_matrix(self):
        self._dataset.reset_process_step()
        # self._dataset.show_summary_rating('test')
        self._rating_model.show_confusion_matrix()

    def show_important_features(self):
        self._rating_model.show_important_features()

    def model_leaderboard(self):
        self._rating_model.model_leaderboard()

    def show_rating_models(self):
        self._rating_model.show_models()

    def show_summary(self, data='all'):
        self._dataset.show_summary(data)

    def split_data(self, data_split):
        self._dataset.split_data(data_split)

    def _initialise(self):
        start = timer()
        print(f'{self._logger}initialisation::...')
        self._load_dataset()
        self._classification = self._dataset.get_unique_values('rating')
        self._create_models()
        print(f'{self._logger}initialisation::Elapse time: {timedelta(seconds=timer()-start)}')
        
    def _load_dataset(self):
        print(f'{self._logger}loading {COLOR_BLUE}Ofsted Inspected School [OIS]{COLOR_RESET} dataset::...')
        self._dataset = Dataset(dataset_filename = DATASET_PATH + DATASET_FILENAME)

    def _print_classification(self):
        print(f'\n{COLOR_INVERSE} {self._dataset.get_next_step()}. Classification: {COLOR_RESET}')
        for i in range(len(self._classification)):
            print(f'{TAB_SPACE}{i+1:<5} {COLOR_BOLD}{COLOR_BLUE}{self._classification[i]}{COLOR_RESET}')

    def _create_models(self):
        # pass (mandatory) dataset 
        self._rating_model = RatingModel(dataset = self._dataset)

