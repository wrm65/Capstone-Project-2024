from sklearn.ensemble import GradientBoostingClassifier

# import project libraries
from constants import *
from utility import *
from base import BaseModel

class GradientBoostingModel(BaseModel):
    """A Gradient Boosting Classifier."""
    def __init__(self):
        # define hyperparameter to tune
        self._learning_rate = 0.5 # values must be in the range [0.0, inf)
        self._n_estimators = 10 # number of boosting stages to perform
        self._n_iter_no_change = 10 # used to decide if early stopping will be used to terminate training
        super().__init__(model_type = MODEL_GRADIENT_BOOSTING['TYPE'], title = MODEL_GRADIENT_BOOSTING['TITLE'])

    def do_pre_build_model_process(self):
        self._hyperparameter = {
            "learning_rate": self._learning_rate,
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
            step = i * 10
            params = {
                "learning_rate": self._learning_rate,
                "n_estimators": step,
            }
            self.set_params(params)
            self.do_train_n_predict_model() 
            self.do_evaluate_model()
            print(f'{TAB_SPACE * 2}Iteration: {(i):0.0f} of {(end-1):0.0f} {COLOR_BLUE}n_estimators: {step} accuracy score: {self._accuracy_score:0.4f}{COLOR_RESET}')
            if self._accuracy_score > accuracy_score:
                self._n_estimators = step
                accuracy_score = self._accuracy_score
            self._iteration += 1
        
        self._accuracy_score = accuracy_score
        print(f'\n{TAB_SPACE}Best accuracy score: {COLOR_BLUE}{self._accuracy_score:0.4f}{COLOR_RESET}')
        print(f'{TAB_SPACE}Best Number of boosting stages: {COLOR_BLUE}{self._n_estimators}{COLOR_RESET}')

    # override base method
    def do_post_build_model_process(self):
        self._hyperparameter = {
            "learning_rate": self._learning_rate,
            "n_estimators": self._n_estimators
        }
        self.show_evaluation_score(self._hyperparameter)
        self.feature_importance_score()
        self.show_feature_importance_score()

