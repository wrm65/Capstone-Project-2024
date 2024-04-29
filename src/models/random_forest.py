import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report

# import project libraries
from base import BaseModel
from constants import *

class RandomForestModel(BaseModel):
    """A random forest classifier."""
    def __init__(self):
        # define hyperparameter to tune
        self._n_estimators = 50 #number of trees in the forest
        self._classification_report = None
        super().__init__(model_type = MODEL_RANDOM_FOREST['TYPE'], title = MODEL_RANDOM_FOREST['TITLE'])

    def do_pre_build_model_process(self):
        self._hyperparameter = {
            "n_estimators": self._n_estimators
        }
        self.set_params(self._hyperparameter)

    # override base method
    def do_build_model(self):
        self._iteration = 0
        accuracy_score = 0
        start = 1
        end = 11
        for i in range(start, end):
            step = i * 50
            params = {
                "n_estimators": step
            }
            self.set_params(params)
            # print(f'{TAB_SPACE}{self.get_params()}\n')
            self.do_train_n_predict_model()
            self.do_evaluate_model()
            print(f'{TAB_SPACE * 2}Iteration: {(i):0.0f} of {(end-1):0.0f} {COLOR_BLUE}n_estimators: {step} accuracy score: {self._accuracy_score:0.4f}{COLOR_RESET}')
            if self._accuracy_score > accuracy_score:
                self._n_estimators = step
                accuracy_score = self._accuracy_score
            self._iteration += 1
        
        self._accuracy_score = accuracy_score
        print(f'\n{TAB_SPACE}Best accuracy score: {COLOR_BLUE}{self._accuracy_score:0.4f}{COLOR_RESET}')
        print(f'{TAB_SPACE}Best estimators: {COLOR_BLUE}{self._n_estimators}{COLOR_RESET}')


    # override base method
    def do_post_build_model_process(self):
        self._hyperparameter = {
            "n_estimators": self._n_estimators
        }
        self.show_evaluation_score(self._hyperparameter)
        self.feature_importance_score()
        self.show_feature_importance_score()
        self.classification_report()
        self.show_classification_report()

