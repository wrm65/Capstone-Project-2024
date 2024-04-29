import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.calibration import CalibrationDisplay

from datetime import timedelta

# import project libraries
from constants import *
from utility import *
from dataset import Dataset
from decision_tree import DecisionTreeModel
from random_forest import RandomForestModel
from k_neighbors import KNeighborsModel
from support_vector import SupportVectorModel
from logistic_regression import LogisticRegressionModel
from naive_bayes import NaiveBayesModel
from gradient_boost import GradientBoostingModel
from multilayer_perceptron import MultiLayerPerceptronModel
from tabulater import *

class RatingModel(object):
    def __init__(self, dataset):
        self._logger = f'::{self.__class__.__name__}::'
        self._dataset = dataset
        self._models = []
        self._create_models()

    def get_model_type(self, model_type):
        return next((model for model in self._models if model.get_model_type() == model_type), None)

    def get_models(self, model_type):
        if model_type is not None:
            model = self.get_model_type(model_type)
            if model is None:
                print(f'{self._logger}get_models:: {COLOR_INVERSE_RED} The model type [{model_type}] does not exist. {COLOR_RESET}')
                return None
            else:
                return model
        
        return self._models

    def get_model_list_title(self):
        list_title = []
        for index, model in enumerate(self._models):
            list_title.append(model.get_title())
        return list_title

    def build_model(self, model_type):
        model = self.get_model_type(model_type)
        if model is None:
            print(f'{self._logger}build_model:: {COLOR_RED} The model type [{model_type}] is not valid. Please check and correct.{COLOR_RESET} ')
        else:
            model.build_model(self._dataset)

    def clear_model(self):
        for index, model in enumerate(self._models):
            model.clear_model()

    def evaluate_model(self):
        def _format_score(scores, index):
            if index < len(scores):
                return f'{scores[index]:0.4f}'
            return '';
            
        model_list_title = self.get_model_list_title()
        # list_size = [None] * len(model_list_title)
        list_size = [None]
        eval_view_1 = pd.DataFrame(columns=['model',
                                            'iterations',
                                            'elapse_time',
                                            'hyperparameter',
                                           ]).set_index('model')
        eval_view_2 = pd.DataFrame(columns=['model',
                                            'accuracy',
                                            'mean_squared_error',
                                           ]).set_index('model')
        eval_view_3 = pd.DataFrame(columns=['model',
                                            'outstanding',
                                            'good',
                                            'requires_improvement',
                                            'inadequate',
                                           ]).set_index('model')
        eval_view_4 = pd.DataFrame(columns=['model',
                                            'outstanding',
                                            'good',
                                            'requires_improvement',
                                            'inadequate',
                                           ]).set_index('model')
                                   
        for index, model in enumerate(self._models):
            if model.get_y_predict() is not None:
                eval_view_1.loc[model.get_title(), 'iterations'] = model.get_score_iteration()
                eval_view_1.loc[model.get_title(), 'elapse_time'] = format_elapse_time(timedelta(seconds=model.get_score_timing()))
                if model.get_score_hyperparameter() is None:
                    eval_view_1.loc[model.get_title(), 'hyperparameter'] = DEFAULT_SETTINGS
                else:
                    eval_view_1.loc[model.get_title(), 'hyperparameter'] = str(model.get_score_hyperparameter())
                if model.get_score_accuracy() is not None:
                    eval_view_2.loc[model.get_title(), 'accuracy'] = f'{model.get_score_accuracy():0.4f}'
                if model.get_score_mse() is not None:
                    eval_view_2.loc[model.get_title(), 'mean_squared_error'] = f'{model.get_score_mse()[0]:0.4f}'
                if model.get_score_recall() is not None:
                    eval_view_3.loc[model.get_title(), 'outstanding'] = _format_score(model.get_score_recall(), 0)
                    eval_view_3.loc[model.get_title(), 'good'] = _format_score(model.get_score_recall(), 1)
                    eval_view_3.loc[model.get_title(), 'requires_improvement'] = _format_score(model.get_score_recall(), 2)
                    eval_view_3.loc[model.get_title(), 'inadequate'] = _format_score(model.get_score_recall(), 3)
                if model.get_score_f1() is not None:
                    eval_view_4.loc[model.get_title(), 'outstanding'] = _format_score(model.get_score_f1(), 0)
                    eval_view_4.loc[model.get_title(), 'good'] = _format_score(model.get_score_f1(), 1)
                    eval_view_4.loc[model.get_title(), 'requires_improvement'] = _format_score(model.get_score_f1(), 2)
                    eval_view_4.loc[model.get_title(), 'inadequate'] = _format_score(model.get_score_f1(), 3)
                # print(f'{model.get_title()}: {model.get_score_iteration()}')
        eval_view_1.sort_index(inplace=True)
        eval_view_2.sort_index(inplace=True)
        eval_view_3.sort_index(inplace=True)
        eval_view_4.sort_index(inplace=True)
        print(f'\n{COLOR_INVERSE} Model Evaluation {COLOR_RESET}')
        # define dict of report column attributes:
        # size, alignment, formatter, datatype
        columns = {'iterations': {'type': 'int', 'size': 10, 'alignment': '<', 'color': COLOR_BLACK},
                   'elapse_time': {'type': 'str', 'size': 12, 'alignment': '<'},
                   'hyperparameter': {'type': 'str', 'size': 0, 'alignment': '>'},
                   }
        print_format_dataset(eval_view_1, eval_view_1.shape[0], eval_view_1.shape[1], print_index=True, highlight_index=True, columns=columns)
        print(f'\n{TAB_SPACE * 1}{COLOR_INVERSE}{COLOR_BLUE} Evaluation Metrics {COLOR_RESET}')
        columns = {'accuracy': {'type': 'float', 'size': 8, 'alignment': '>'},
                   'mean_squared_error': {'type': 'float', 'size': 18, 'alignment': '>'},
                   }
        print_format_dataset(eval_view_2, eval_view_2.shape[0], eval_view_2.shape[1], print_index=True, highlight_index=True, columns=columns)
        print(f'\n{TAB_SPACE * 2}{COLOR_INVERSE}{COLOR_BLUE} Grading Classification: {COLOR_RESET}')
        print(f'\n{TAB_SPACE * 2}{COLOR_INVERSE}{COLOR_YELLOW} Recall Scores {COLOR_RESET}')
        columns = {'outstanding': {'type': 'float', 'size': 11, 'alignment': '>'},
                   'good': {'type': 'float', 'size': 6, 'alignment': '>'},
                   'requires_improvement': {'type': 'float', 'size': 20, 'alignment': '>'},
                   'inadequate': {'type': 'float', 'size': 10, 'alignment': '>'},
                   }
        print_format_dataset(eval_view_3, eval_view_3.shape[0], eval_view_3.shape[1], print_index=True, highlight_index=True, columns=columns)
        print(f'\n{TAB_SPACE * 2}{COLOR_INVERSE}{COLOR_YELLOW} F1 Scores {COLOR_RESET}')
        print_format_dataset(eval_view_4, eval_view_4.shape[0], eval_view_4.shape[1], print_index=True, highlight_index=True, columns=columns)

    # https://stackoverflow.com/questions/61825227/plotting-multiple-confusion-matrix-side-by-side
    def show_confusion_matrix(self):
        print(f'\n{COLOR_INVERSE}{COLOR_BOLD} Model Confusion Matrices: {COLOR_RESET}')
        fig, axes = plt.subplots(2, 4, figsize=(20, 12), sharey='row')
        for index, model in enumerate(self._models):
            row = 0
            col = index
            if index > 3:
                row = 1
                col = index - 4
            axes[row, col].set_title(model.get_title())
            if model.get_y_predict() is not None:
                if DEBUG_LEVEL > 3:
                    print(f'{self._logger}show_confusion_matrix:: {model.get_title()} ...')
                cf_matrix = confusion_matrix(model.get_y_test(), model.get_y_predict())
                disp = ConfusionMatrixDisplay(cf_matrix,
                                              display_labels=[
                                                    GRADING_OUTSTANDING, 
                                                    GRADING_GOOD,
                                                    GRADING_REQUIRES_IMPROVEMENT.replace(' ', '\n'),
                                                    GRADING_INADEQUATE])
                disp.plot(ax=axes[row, col], xticks_rotation=45)
                disp.im_.colorbar.remove()
                disp.ax_.set_xlabel('')
                disp.ax_.title.set_size(14)
                if (index == 0 or
                    index == 4):
                    disp.ax_.set_ylabel('True Grading', fontweight='bold', fontsize=14)
                else:
                    disp.ax_.set_ylabel('')
                
        fig.text(0.4, 0, 'Predicted Grading', ha='left', fontweight='bold', fontsize=20)
        plt.subplots_adjust(wspace=0.40, hspace=0.1)
        fig.colorbar(disp.im_, ax=axes)
        plt.show()

    def show_important_features(self):
        features = pd.DataFrame(columns=['model',
                                         'most_important',
                                         'least_important',
                                        ]).set_index('model')
        for index, model in enumerate(self._models):
            if model.get_score_feature() is not None:
                feature = model.get_important_feature('first')
                features.loc[model.get_title(), 'most_important'] = feature['name']
                feature = model.get_important_feature('last')
                features.loc[model.get_title(), 'least_important'] = feature['name']

        print(f'\n{COLOR_INVERSE} List of Important Features {COLOR_RESET}\n')
        if not features.empty:
            columns = {'most_important': {'type': 'str', 'size': 28,},
                       'least_important': {'type': 'str', 'size': 28,},
                      }
            print_format_dataset(features, features.shape[0], features.shape[1], print_index=True, highlight_index=True, columns=columns)

    def model_leaderboard(self):
        print(f'\n{COLOR_INVERSE} Model Leaderboard {COLOR_RESET}\n')
        self._create_leaderboard()

    def show_models(self):
        print(f'{COLOR_INVERSE} Total models: {COLOR_BLUE} {len(self._models)} {COLOR_RESET}{COLOR_INVERSE} {COLOR_RESET}')
        for index, model in enumerate(self._models):
            print(f'{index+1}.{TAB_SPACE}{COLOR_BLUE}{model.get_model()}{COLOR_RESET}')

    def _create_leaderboard(self):
        def _get_performance_score(scores, index):
            if index < len(scores):
                return scores[index]
            return 0;
            
        def _get_model_position(df, model):
            if index < len(scores):
                return scores[index]
            return 0;
            
        leaderboard_header = [LEADERBOARD_HEADER_MODEL, 
                              LEADERBOARD_HEADER_ACCURACY,
                              LEADERBOARD_HEADER_MSE, 
                              LEADERBOARD_HEADER_RECALL_OUTSTANDING, 
                              LEADERBOARD_HEADER_RECALL_GOOD, 
                              LEADERBOARD_HEADER_RECALL_REQUIRE_IMPROVEMENT, 
                              LEADERBOARD_HEADER_RECALL_INADEQUATE, 
                              LEADERBOARD_HEADER_F1_OUTSTANDING, 
                              LEADERBOARD_HEADER_F1_GOOD, 
                              LEADERBOARD_HEADER_F1_REQUIRE_IMPROVEMENT, 
                              LEADERBOARD_HEADER_F1_INADEQUATE,
                              LEADERBOARD_HEADER_OVERALL_POSITION,
                              LEADERBOARD_HEADER_OVERALL_RANKING]
        scores = pd.DataFrame(columns=leaderboard_header[:len(leaderboard_header)-2]).set_index(LEADERBOARD_HEADER_MODEL)
        for index, model in enumerate(self._models):
            if model.get_y_predict() is not None:
                if model.get_score_accuracy() is not None:
                    scores.loc[model.get_title(), LEADERBOARD_HEADER_ACCURACY] = model.get_score_accuracy()
                if model.get_score_mse() is not None:
                    scores.loc[model.get_title(), LEADERBOARD_HEADER_MSE] = model.get_score_mse()[0]
                if model.get_score_recall() is not None:
                    scores.loc[model.get_title(), LEADERBOARD_HEADER_RECALL_OUTSTANDING] = _get_performance_score(model.get_score_recall(), 0)
                    scores.loc[model.get_title(), LEADERBOARD_HEADER_RECALL_GOOD] = _get_performance_score(model.get_score_recall(), 1)
                    scores.loc[model.get_title(), LEADERBOARD_HEADER_RECALL_REQUIRE_IMPROVEMENT] = _get_performance_score(model.get_score_recall(), 2)
                    scores.loc[model.get_title(), LEADERBOARD_HEADER_RECALL_INADEQUATE] = _get_performance_score(model.get_score_recall(), 3)
                if model.get_score_f1() is not None:
                    scores.loc[model.get_title(), LEADERBOARD_HEADER_F1_OUTSTANDING] = _get_performance_score(model.get_score_f1(), 0)
                    scores.loc[model.get_title(), LEADERBOARD_HEADER_F1_GOOD] = _get_performance_score(model.get_score_f1(), 1)
                    scores.loc[model.get_title(), LEADERBOARD_HEADER_F1_REQUIRE_IMPROVEMENT] = _get_performance_score(model.get_score_f1(), 2)
                    scores.loc[model.get_title(), LEADERBOARD_HEADER_F1_INADEQUATE] = _get_performance_score(model.get_score_f1(), 3)
        scores.sort_index(inplace=True)
        # create table with dimension = [total model] x [total metrics] 
        # with initial rank position = 0
        zero_data = np.zeros(shape=(scores.shape[0], scores.shape[1]), dtype=int)
        leaderboard = pd.DataFrame(zero_data, columns=scores.columns)
        leaderboard['Model'] = scores.index.values
        # set Student_Id column as index
        leaderboard.set_index(LEADERBOARD_HEADER_MODEL, inplace = True)
        for i, column in enumerate(leaderboard.columns):
            model_positions = scores.sort_values([column], ascending=[False]).index.values.tolist()
            for model, data in leaderboard.iterrows():
                leaderboard.loc[model, column] = model_positions.index(model) + 1
        # store overall position
        overall_position = leaderboard.mean(axis=1)
        leaderboard[LEADERBOARD_HEADER_OVERALL_POSITION] = overall_position
        overall_ranking = np.sort(overall_position)
        # calculate overall ranking
        leaderboard[LEADERBOARD_HEADER_OVERALL_RANKING] = np.zeros(shape=(len(leaderboard)), dtype='<U5')
        for model, columns in leaderboard.iterrows():
            index = np.where(overall_ranking == columns[LEADERBOARD_HEADER_OVERALL_POSITION])
            rank = index[0][0] + 1
            leaderboard.loc[leaderboard.loc[model].name, LEADERBOARD_HEADER_OVERALL_RANKING] = f' {rank} ' if len(index[0]) == 1 else f' {rank}*'
        set_preserve_whitespace(True)
        print(tabulater(leaderboard, headers=leaderboard_header, floatfmt="4.1f",
                        colalign=("left", "center", "center", "center",
                                  "center", "center", "center", "center",
                                  "center", "center", "center", "center",
                                  "center"),
                        tablefmt="nospace",
                        preserve_whitespace=True))
        print(f'\n{COLOR_INVERSE}{COLOR_GREEN} {"Grading abbreviation":^26} {COLOR_RESET}')
        print(f'{COLOR_INVERSE}{COLOR_BLUE} O/s - {GRADING_OUTSTANDING:<20} {COLOR_RESET}')
        print(f'{COLOR_INVERSE}{COLOR_BLUE} RI  - {GRADING_REQUIRES_IMPROVEMENT:<20} {COLOR_RESET}')
        print(f'{COLOR_INVERSE}{COLOR_BLUE} I/a - {GRADING_INADEQUATE:<20} {COLOR_RESET}')
            

    def _create_models(self):
        self._models.append(DecisionTreeModel())
        self._models.append(RandomForestModel())
        self._models.append(KNeighborsModel())
        self._models.append(SupportVectorModel())
        self._models.append(LogisticRegressionModel())
        self._models.append(NaiveBayesModel())
        self._models.append(GradientBoostingModel())
        self._models.append(MultiLayerPerceptronModel())

