import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch

from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE, ADASYN, BorderlineSMOTE
import category_encoders as ce

from timeit import default_timer as timer
from datetime import timedelta
from tabulate import tabulate

# import project libraries
from constants import *
from utility import *

class Dataset(object):
    def __init__(self, dataset_filename = None):
        self._logger = f'::{self.__class__.__name__}::'
        self._dataset_filename = dataset_filename
        self._dataset = None
        self._X_resampled = None
        self._y_resampled = None
        self._output_column = DATASET_COLUMN_RATING
        self._process_step = 0
        self.X_inputs = None
        self.y_output = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self._data_split = None
        self._initialise()
        
    def get_dataset(self):
        return self._dataset

    def get_dataset_features(self):
        return self.X_inputs.columns

    def get_next_step(self):
        self._process_step += 1
        return self._process_step

    def get_x_inputs(self):
        return self.X_inputs

    def get_X_test(self):
        return self.X_test

    def get_X_train(self):
        return self.X_train

    def get_y_output(self):
        return self.y_output

    def get_y_test(self):
        return self.y_test

    def get_y_train(self):
        return self.y_train

    def get_training_set(self):
        return {
                "X_train": self.get_X_train().shape,
                "y_train": self.get_y_train().shape
               }

    def get_test_set(self):
        return {
                "X_test": self.get_X_test().shape,
                "y_test": self.get_y_test().shape
               }

    def get_unique_values(self, colname):
        return self._dataset[colname].unique()
    
    def set_x_inputs(self):
        # declare feature vector
        self.X_inputs = self._dataset.drop([self._output_column], axis=1)

    def set_y_output(self):
        # declare target variable
        self.y_output = self._dataset[self._output_column]

    def convert_object_variables(self):
        columns = list(self._dataset.select_dtypes(['object']).columns)
        print(f'Converting columns: {COLOR_BLUE}{len(columns)}{COLOR_RESET}')
        print(f'{TAB_SPACE}{COLOR_BLUE}{columns}{COLOR_RESET}\n')
        for index, column in enumerate(columns):
            self._dataset[column] = self._dataset[column].astype('|S')
        self._print_dataset_columns()

    def drop_unwanted_columns(self):
        self.reset_process_step()
        columns = [DATASET_COLUMN_UNIQUE_REFERENCE_NUMBER, 
                   DATASET_COLUMN_UNIQUE_AUTHORITY_CODE,
                   DATASET_COLUMN_UNIQUE_ESTABLISHMENT_TYPE_CODE,
                   DATASET_COLUMN_UNIQUE_GENDER_CATEGORY,
                   DATASET_COLUMN_UNIQUE_RELIGIOUS_CLASSIFICATION,
                   DATASET_COLUMN_UNIQUE_PUPIL_NUMBER,
                   DATASET_COLUMN_UNIQUE_PUPIL_BOYS,
                   DATASET_COLUMN_UNIQUE_PUPIL_GIRLS]
        print(f'Dropping columns: {COLOR_BLUE}{len(columns)}{COLOR_RESET}')
        print(f'{TAB_SPACE}{COLOR_BLUE}{columns}{COLOR_RESET}\n')
        self._dataset.drop(columns, axis=1, inplace=True)
        self._print_dataset_columns()

    def encode_rating_catogory(self):
        if self.valid_data_action(DATASET_ACTION_ENCODE_DATA):
            self._print_unique_values(self._dataset, self._output_column)
            print(self._dataset[self._output_column])
            print("\n", "Encoding values...", "\n")
            encoder = ce.OrdinalEncoder(cols=[self._output_column])
            self._dataset = encoder.fit_transform(self._dataset)
            self._print_unique_values(self._dataset, self._output_column)
            print(self._dataset[self._output_column])

    def report_dataset_vitals(self, level='all'):
        self.reset_process_step()
        self._print_dataset_size()
        self._print_dataset_columns()
        self._print_dataset_head(nrow = 5, ncol = 3)
        self._print_dataset_null_count()

    def reset_process_step(self):
        self._process_step = 0

    def run_data_balance(self):
        if self.valid_data_action(DATASET_ACTION_BALANCE_DATA):
            if DEBUG_LEVEL > 3:
                print(f'{self._logger}run_data_balance:: {self.get_training_set()} {self.get_test_set()}')
            self._do_run_data_balance()
            self.X_train = None
            self.X_test = None
            self.y_train = None
            self.y_test = None
            self.X_inputs = self._X_resampled
            self.y_output = self._y_resampled
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X_inputs, self.y_output, test_size=self._data_split, random_state=42)
            if DEBUG_LEVEL > 3:
                print(f'{self._logger}run_data_balance:: {self.get_training_set()} {self.get_test_set()}')

    def split_data(self, data_split):
        if self.valid_data_action(DATASET_ACTION_SPLIT_DATA):
            self._data_split = data_split
            self.set_x_inputs()
            self.set_y_output()
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X_inputs, self.y_output, test_size=data_split, random_state=42)
            self._print_dataset_split()

    def show_frequency_distribution(self, dataset, title):
        print(f'\n{COLOR_INVERSE} {self.get_next_step()}. {title} {COLOR_RESET}')
        col_names = ['authority_code', 'gender_type', 'religious_type', 'percent_pupil_boys', 'percent_pupil_girls', 'percent_ehc_plan', 'percent_sen_support', 'percent_english_language', 'percent_not_english_language', 'percent_free_school_meals']
        for col in col_names:
            print(dataset[col].value_counts()) 

    def show_summary(self, data='all'):
        self.reset_process_step()
        dataset = self._dataset
        if data == 'train':
            dataset = self.X_train
        elif data == 'test':
            dataset = self.X_test
        # self.show_frequency_distribution(dataset, 'Frequency Distribution:')
        self._show_school_summary(dataset, 'School Gender Type:', 'gender_category')
        self._show_school_summary(dataset, 'School Religious Ethos:', 'religious_classification')
        self.show_summary_rating(data)

    def show_summary_rating(self, data='all', dataset=None, **kwargs):
        df = dataset
        if data != 'all':
            df = self._convert_school_rating(data, dataset)
        else:
            df = self._dataset
        title = 'School Ofsted Rating:'
        if 'title' in kwargs:
            title = kwargs['title']
        self._show_school_summary(df, title, self._output_column)

    def valid_data_action(self, request):
        if request == DATASET_ACTION_ENCODE_DATA:
            # check data preparation completed
            if DATASET_COLUMN_UNIQUE_REFERENCE_NUMBER in self._dataset.columns:
                print(f'{self._logger}valid_data_action:: {COLOR_INVERSE_RED} Please drop unwanted columns before splitting the dataset. {COLOR_RESET}')
                return False
        elif request == DATASET_ACTION_SPLIT_DATA:
            if self._dataset[DATASET_COLUMN_RATING].dtype != 'int32':
                print(f'{self._logger}valid_data_action:: {COLOR_INVERSE_RED} Please encode the rating category before splitting the dataset. {COLOR_RESET}')
                return False
        elif (request == DATASET_ACTION_BALANCE_DATA or
              request == DATASET_ACTION_BUILD_MODEL):
            # check data has been split
            if self.get_X_train() is None:
                print(f'{self._logger}valid_data_action:: {COLOR_INVERSE_RED} No training data is available. Please check if the dataset has been split. {COLOR_RESET}')
                return False
            
        return True

    def _initialise(self):
        if self._dataset_filename is not None:
            self._load_dataset()

    def _do_run_data_balance(self):
        print('Original dataset shape: ', self.X_inputs.shape, self.y_output.shape)
        self.reset_process_step()
        self.show_summary_rating(data=None, dataset=self.y_output, title='School Ofsted Rating (before oversampling):')
        start = timer()
        ada = SMOTE(sampling_strategy='minority', k_neighbors=45, random_state=42)
        self._X_resampled, self._y_resampled = ada.fit_resample(self.X_inputs, self.y_output)
        print(f'\n{self._logger}_do_run_data_balance::Elapse time: {timedelta(seconds=timer()-start)}')
        print('Resampled dataset shape: ', self._X_resampled.shape, self._y_resampled.shape)
        self.show_summary_rating(data=None, dataset=self._y_resampled, title='School Ofsted Rating (after oversampling):')
 
    def _load_dataset(self):
        self._dataset = pd.read_csv(self._dataset_filename)

    def _convert_school_rating(self, data, dataset=None):
        df = dataset
        if df is None:
            df = self.y_test.to_frame()
            if data == 'train':
                df = self.y_train.to_frame()
        else:
            df = df.to_frame()
        # convert column datatype integer to string
        df[self._output_column] = df[self._output_column].apply(str)
        # replace values in the 'rating' column based on condition
        df.loc[df[self._output_column] == str(GRADING_OUTSTANDING_INT), self._output_column] = GRADING_OUTSTANDING
        df.loc[df[self._output_column] == str(GRADING_GOOD_INT), self._output_column] = GRADING_GOOD
        df.loc[df[self._output_column] == str(GRADING_REQUIRES_IMPROVEMENT_INT), self._output_column] = GRADING_REQUIRES_IMPROVEMENT
        df.loc[df[self._output_column] == str(GRADING_INADEQUATE_INT), self._output_column] = GRADING_INADEQUATE
        return df

    def _show_school_summary(self, dataset, title, colname):
        print(f'\n{COLOR_INVERSE} {self.get_next_step()}. {title} {COLOR_RESET}')
        self._print_unique_values(dataset, colname)
        # create summary total grouped by rating
        summary = dataset.groupby([colname]).size()
        # convert (transpose) from Series (<class 'pandas.core.series.Series'>) to DataFrame 
        summary = pd.DataFrame(summary).transpose().sum(axis=0).to_frame(COLUMN_NAME_TOTAL_SCHOOLS)
        # add percentage column
        summary['Percentage'] = np.round((summary[COLUMN_NAME_TOTAL_SCHOOLS] / summary[COLUMN_NAME_TOTAL_SCHOOLS].sum()) * 100, 2)
        columns = {COLUMN_NAME_TOTAL_SCHOOLS: {'type': 'int', 'size': 13, 'alignment': '>'},
                   }
        print_format_dataset(summary, summary.shape[0], summary.shape[1], print_index=True, columns=columns)
        total = summary[COLUMN_NAME_TOTAL_SCHOOLS].sum()
        print(f'\n{TAB_SPACE * 3}Total: {COLOR_BLUE}{total:,}{COLOR_RESET}')
        if (colname == self._output_column or
            colname == DATASET_COLUMN_UNIQUE_RELIGIOUS_CLASSIFICATION):
            self._show_summary_graph(colname, summary)

    def _show_summary_graph(self, colname, summary):
        explode = (0.1, 0.2, 0.2, 0.0)
        start_angle = 50
        if colname == DATASET_COLUMN_UNIQUE_RELIGIOUS_CLASSIFICATION:
            explode = (0.1, 0.1, 0.1, 0.1)
            start_angle = 180
        wp = {'linewidth': 1, 'edgecolor': "black"}
        colors = ("orange", "cyan", "indigo", "beige")
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.pie(summary[COLUMN_NAME_TOTAL_SCHOOLS],
               labels=summary.index,
               explode=explode,
               startangle=start_angle,
               shadow=True,
               wedgeprops=wp,
               textprops=dict(color="blue"))
        plt.show()

    def _print_unique_values(self, dataset, colname):
        values = dataset[colname].unique()
        print(f'\n{TAB_SPACE}{COLOR_INVERSE}{COLOR_BLUE} List of unique values: {COLOR_BLACK} {len(values)} {COLOR_RESET}{COLOR_INVERSE}{COLOR_BLUE} {COLOR_RESET}')
        print(f'{TAB_SPACE * 2}{COLOR_BLUE}{values}{COLOR_RESET}\n')

    def _print_dataset_columns(self):
        print(f'\n{COLOR_INVERSE} {self.get_next_step()}. Column definition: {COLOR_RESET}')
        for index, column in enumerate(self._dataset.columns):
            datatype_color = get_datatype_color(self._dataset[column].dtypes)
            print(f'{TAB_SPACE}{index+1:<5} {COLOR_BLUE}{column:<35}{COLOR_RESET} {COLOR_BOLD}{datatype_color}{self._dataset[column].dtypes}{COLOR_RESET}')

    def _print_dataset_head(self, nrow = 6, ncol = 4):
        print(f'\n{COLOR_INVERSE} {self.get_next_step()}. Head: first {nrow} rows {COLOR_RESET}')
        print_format_dataset(self._dataset, nrow, ncol)

    def _print_dataset_null_count(self):
        print(f'\n{COLOR_INVERSE} {self.get_next_step()}. Column Null Counts: {COLOR_RESET}')
        index = 0
        null_counts = self._dataset.isnull().sum()
        for column, value in null_counts.items():
            index += 1
            print(f'{TAB_SPACE}{index:<5} {COLOR_BLUE}{column:<35}{COLOR_RESET} {COLOR_BOLD}{COLOR_GREEN}{value}{COLOR_RESET}')

    def _print_dataset_split(self):
        print(f'\n{COLOR_INVERSE}  Confirm Data Split: {COLOR_RESET}\n')
        label = f'Training set ( {COLOR_BLUE}{(self.get_X_train().shape[0] / self._dataset.shape[0] * 100.0):0.0f}%{COLOR_RESET} ):'
        print(f'{TAB_SPACE}{label:>35} {COLOR_BLUE}{self.get_training_set()}{COLOR_RESET}')
        label = f'Testing set ( {COLOR_BLUE}{(self.get_X_test().shape[0] / self._dataset.shape[0] * 100.0):0.0f}%{COLOR_RESET} ):'
        print(f'{TAB_SPACE}{label:>35} {COLOR_BLUE}{self.get_test_set()}{COLOR_RESET}')
        total = f'{self.get_X_train().shape[0]:,} + {self.get_X_test().shape[0]:,} = {self.get_X_train().shape[0]+self.get_X_test().shape[0]:,}'
        print(f'{TAB_SPACE}{"Dataset total ( 100% ):":>24} {COLOR_BLUE}{total}{COLOR_RESET}')

    def _print_dataset_size(self):
        print(f'\n{COLOR_INVERSE} {self.get_next_step()}. Dataset: {COLOR_RESET}')
        label = 'Filename:'
        print(f'{TAB_SPACE}{label:<15} {COLOR_BLUE}{self._dataset_filename}{COLOR_RESET}')
        label = 'Total Rows:'
        print(f'{TAB_SPACE}{label:<15} {COLOR_BLUE}{self._dataset.shape[0]:,}{COLOR_RESET}')
        label = 'Total Columns:'
        print(f'{TAB_SPACE}{label:<15} {COLOR_BLUE}{self._dataset.shape[1]}{COLOR_RESET}')

