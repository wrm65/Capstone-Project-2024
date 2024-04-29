import numpy as np
import pandas as pd
import warnings
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
from sklearn.ensemble import RandomForestClassifier

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import accuracy_score, mean_squared_error, recall_score, f1_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.calibration import CalibrationDisplay

from timeit import default_timer as timer
from datetime import timedelta

# import project libraries
from constants import *
from utility import *

class BaseModel(object):
    def __init__(self, model_type = None, title = ""):
        self._logger = f'::{self.__class__.__name__}::'
        self._title = title
        self._model_type = model_type
        self._model = None
        self._dataset = None
        self._pipeline = None
        self._classification = None
        self._hyperparameter = None
        self._param_distributions = {}
        self._y_predict = None
        self._iteration = None
        self._timing = None
        self._search_result = None
        self._accuracy_score = None
        self._feature_scores = None
        self._recall_score = None
        self._f1_score = None
        self._mse_score = None
        self._classification_score = None
        self._classification_report = None
        self._process_step = 0
        self._create_model()

    def get_model(self):
        return self._model

    def get_model_type(self):
        return self._model_type

    def get_score_accuracy(self):
        return self._accuracy_score

    def get_score_classification(self):
        return self._classification_score

    def get_score_f1(self):
        return self._f1_score

    def get_score_hyperparameter(self):
        return self._hyperparameter

    def get_score_feature(self):
        return self._feature_scores

    def get_score_mse(self):
        return self._mse_score

    def get_score_recall(self):
        return self._recall_score

    def get_important_feature(self, position):
        feature = {
            'name': '',
            'value': 0
        }
        if self._feature_scores is not None:
            if position == 'first':
                feature['name'] = self._feature_scores.index[0]
                feature['value'] = self._feature_scores.iloc[0]
            elif position == 'last':
                feature['name'] = self._feature_scores.index[len(self._feature_scores.index)-1]
                feature['value'] = self._feature_scores.iloc[-1]
        return feature

    def get_score_iteration(self):
        return self._iteration

    def get_score_timing(self):
        #format timing h:mm:ss.ms
        return self._timing

    def get_next_step(self):
        self._process_step += 1
        return self._process_step

    def get_params(self):
        if self._model is not None:
            return self._model.get_params()

    def get_title(self):
        return self._title

    def get_y_predict(self):
        return self._y_predict

    def get_y_test(self):
        return self._dataset.get_y_test()

    def set_params(self, params = None):
        if params is not None:
            self._model.set_params(**params)

    def build_model(self, dataset):
        def _format_status_info(state, info):
            return f'\n{COLOR_INVERSE} {self._logger}build_model::{COLOR_GREEN} {state} {COLOR_RESET}{COLOR_INVERSE} {info} {COLOR_RESET}\n'
        
        if dataset.valid_data_action(DATASET_ACTION_BUILD_MODEL):
            self._dataset = dataset
            self._process_step = 0
            self.do_pre_build_model_process()
            print(_format_status_info('starting...', f'{self._model}'))
            if DEBUG_LEVEL > 3:
                print(f'{self._logger}build_model:: {self._dataset.get_training_set()} {self._dataset.get_test_set()}')
            self.make_pipeline()
            if self._pipeline is None:
                print(f'{self._logger}build_model:: {COLOR_INVERSE_RED} The model pipeline has not been created. Please check and correct. {COLOR_RESET}')
            else:
                self._iteration = 0
                self._timing = None
                start = timer()
                self.do_build_model()
                self._timing = timer()-start
                self.do_post_build_model_process()
                print(_format_status_info('completed', f'Elapse time: {timedelta(seconds=self._timing)}'))

    def clear_model(self):
        self._create_model()
        self._pipeline = None
        self._classification = None
        self._param_distributions = {}
        self._hyperparameter = None
        self._y_predict = None
        self._iteration = None
        self._timing = None
        self._search_result = None
        self._accuracy_score = None
        self._feature_scores = None
        self._recall_score = None
        self._f1_score = None
        self._mse_score = None
        self._classification_score = None
        self._process_step = 0

    def do_evaluate_model(self):
        if self._y_predict is None:
            print(f'{self._logger}do_evaluate_model:: {COLOR_INVERSE_RED} The model prediction has not been executed. Please check and correct. {COLOR_RESET}')
        else:
            self.evaluate_accuracy_score()
            self.evaluate_f1_score()
            self.evaluate_recall_score()
            self.evaluate_mse_score()

    def do_pre_build_model_process(self):
        pass

    def do_post_build_model_process(self):
        print(f'\n{COLOR_INVERSE}{COLOR_BLUE} Additional evaluation... {COLOR_RESET}')
        self.do_evaluate_model()
        self.print_evaluation_score()

    def do_train_n_predict(self):
        self.train()
        self.predict()

    def do_train_n_predict_model(self):
        self._model.fit(self._dataset.get_X_train(), self._dataset.get_y_train())
        self._y_predict = self._model.predict(self._dataset.get_X_test())

    def do_build_model(self):
        self._iteration += 1
        self.print_params()
        print(f'{TAB_SPACE}{self.get_next_step()}. {COLOR_BLUE}Training model with X_train and y_train data...{COLOR_RESET}\n')
        self.train()
        print(f'{TAB_SPACE}{self.get_next_step()}. {COLOR_BLUE}Predicting model with X_test data...{COLOR_RESET}\n')
        self.predict()
        print(f'{TAB_SPACE}{self.get_next_step()}. {COLOR_BLUE}Checking accuracy against y_test data...{COLOR_RESET}\n')
        self.do_evaluate_model()
        self.print_accuracy_score()

    def classification_report(self):
        self._classification_score = classification_report(self._dataset.get_y_test(), self._y_predict, digits=4, zero_division=0.0, target_names=CLASSIFICATION, output_dict=True)
        self._classification_report = classification_report(self._dataset.get_y_test(), self._y_predict, digits=4, zero_division=0.0, target_names=CLASSIFICATION, output_dict=False)

    def evaluate_accuracy_score(self):
        self._accuracy_score = accuracy_score(self._dataset.get_y_test(), self._y_predict)

    def evaluate_f1_score(self):
        # must sets the value to return when there is a zero division, i.e. when all predictions and labels are negative.
        # must set "average" one of [None, 'micro', 'macro', 'weighted'] 
        # as it default to 'binary' which will cause ValueError
        # https://stackoverflow.com/questions/52269187/facing-valueerror-target-is-multiclass-but-average-binary
        with warnings.catch_warnings(action="ignore"):
            self._f1_score = f1_score(self._dataset.get_y_test(), self._y_predict, average=None, zero_division=0, labels=np.unique(self._y_predict))

    def evaluate_recall_score(self):
        # must set "average" one of [None, 'micro', 'macro', 'weighted'] 
        # as it default to 'binary' which will cause ValueError
        # https://stackoverflow.com/questions/52269187/facing-valueerror-target-is-multiclass-but-average-binary
        with warnings.catch_warnings(action="ignore"):
            self._recall_score = recall_score(self._dataset.get_y_test(), self._y_predict, average=None, zero_division=0, labels=np.unique(self._y_predict))

    def evaluate_mse_score(self):
        self._mse_score = mean_squared_error(self._dataset.get_y_test(), self._y_predict, multioutput='raw_values')

    def feature_importance_score(self):
        # evaluate the importance of features
        self._feature_scores = pd.Series(self._model.feature_importances_, 
                                         index=self._dataset.get_X_train().columns)\
                                         .sort_values(ascending=False)

    def feature_importance_coefficients_score(self):
        # evaluate the importance of features
        self._feature_scores = pd.Series(self._model.coef_[0], 
                                         index=self._dataset.get_X_train().columns)\
                                         .sort_values(ascending=False)

    def make_pipeline(self):
        self._pipeline = Pipeline([
            ('scaler', StandardScaler()), 
            ('model', self._model)
        ])

    def predict(self):
        self._y_predict = self._classification.predict(self._dataset.get_X_test())

    def train(self):
        self._classification = GridSearchCV(self._pipeline, 
                                            self._param_distributions)
        self._search_result = self._classification.fit(self._dataset.get_X_train(), 
                                                       self._dataset.get_y_train())

    # def train(self):
        # self._classification = RandomizedSearchCV(self._pipeline, 
                                                  # self._param_distributions,
                                                  # random_state = 42)
        # self._search_result = self._classification.fit(self._dataset.get_X_train(), 
                                                       # self._dataset.get_y_train())

    def print_params(self):
        print(f'{COLOR_BLUE}Model Parameters:{COLOR_RESET}\n{TAB_SPACE}{self.get_params()}\n')

    def print_accuracy_score(self):
        print(f'{TAB_SPACE * 2}{COLOR_BLUE}Model accuracy score: {self._accuracy_score:0.4f}{COLOR_RESET}\n')

    def print_evaluation_score(self):
        print(f'\n{TAB_SPACE * 2}{COLOR_BOLD}Accuracy score: {COLOR_BLUE}{self._accuracy_score}{COLOR_RESET}')
        print(f'{TAB_SPACE * 2}{COLOR_BOLD}Recall score: {COLOR_BLUE}{self._recall_score}{COLOR_RESET}')
        print(f'{TAB_SPACE * 2}{COLOR_BOLD}F1 score: {COLOR_BLUE}{self._f1_score}{COLOR_RESET}')
        print(f'{TAB_SPACE * 2}{COLOR_BOLD}Mean squared error: {COLOR_BLUE}{self._mse_score}{COLOR_RESET}')

    def show_classification_report(self):
        print(f'\n{COLOR_INVERSE}{COLOR_BLUE} Show classification report: {COLOR_RESET}\n')
        print(self._classification_report)

    def show_confusion_matrix(self, fig_axs):
        if self._y_predict is not None:
            ConfusionMatrixDisplay(confusion_matrix(self._dataset.get_y_test(), self._y_predict)).plot()
            fig_axs.grid(False)
            fig_axs.title(self._title + " Confusion Matrix")
        
    def show_evaluation_score(self, params = None):
        print(f'\n{COLOR_INVERSE}{COLOR_BLUE} Additional evaluation... {COLOR_RESET}\n')
        if params is not None:
            self.set_params(params)
        print(f'{TAB_SPACE}{self.get_params()}\n')
        # check if using SearchCV classification
        if self._classification is None:
            self.do_train_n_predict_model()
        else:
            self.do_train_n_predict()
        self.do_evaluate_model()
        self.print_evaluation_score()

    def show_feature_importance_score(self):
        print(f'\n{COLOR_INVERSE}{COLOR_BLUE} Visualise importance of features: {COLOR_RESET}\n')
        print(self._feature_scores)
        fig = plt.figure(figsize=(6, 4))
        sns.barplot(x=self._feature_scores, y=self._feature_scores.index)
        plt.xlabel('Feature Importance Score')
        plt.ylabel('Features')
        plt.title("Visualising Important Features")
        plt.show()
        
    def _create_model(self):
        if self._model_type == MODEL_NAIVE_BAYES['TYPE']:
            self._model = GaussianNB()
        elif self._model_type == MODEL_RANDOM_FOREST['TYPE']:
            self._model = RandomForestClassifier(random_state=42)
        elif self._model_type == MODEL_SUPPORT_VECTOR['TYPE']:
            self._model = SVC(random_state=42)
        elif self._model_type == MODEL_KNN['TYPE']:
            self._model = KNeighborsClassifier()
        elif self._model_type == MODEL_LOGISTIC_REGRESSION['TYPE']:
            self._model = LogisticRegression(random_state=42)
        elif self._model_type == MODEL_GRADIENT_BOOSTING['TYPE']:
            self._model = GradientBoostingClassifier(random_state=42)
        elif self._model_type == MODEL_MULTILAYER_PERCEPTRON['TYPE']:
            self._model = MLPClassifier(random_state=42)
        else:
            self._model = DecisionTreeClassifier(random_state=42)
