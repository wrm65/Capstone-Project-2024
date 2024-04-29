from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

# import project libraries
from constants import *
from utility import *
from base import BaseModel

class LogisticRegressionModel(BaseModel):
    """Logistic Regression classifier."""
    def __init__(self):
        self._max_iter = 500 # maximum number of iterations taken for the solvers to converge
        super().__init__(model_type = MODEL_LOGISTIC_REGRESSION['TYPE'], title = MODEL_LOGISTIC_REGRESSION['TITLE'])

    def do_pre_build_model_process(self):
        self._hyperparameter = {
            "max_iter": self._max_iter
        }
        self.set_params(self._hyperparameter)

    # override base method
    def do_build_model(self):
        self._iteration = 0
        # apply parameter(s) to model
        self._hyperparameter = {
            "max_iter": self._max_iter,
            "multi_class": "multinomial"
        }
        self.set_params(self._hyperparameter)
        self.print_params()
        print(self._pipeline.fit(self._dataset.get_X_train(), self._dataset.get_y_train()))
        self._y_predict = self._pipeline.predict(self._dataset.get_X_test())
        self._accuracy_score = self._pipeline.score(self._dataset.get_X_test(), self._dataset.get_y_test())
        print(f'\n{TAB_SPACE}Best accuracy score: {COLOR_BLUE}{self._accuracy_score:0.4f}{COLOR_RESET}')
        self._iteration += 1

    # override base method
    def do_post_build_model_process(self):
        super().do_post_build_model_process()
        self.feature_importance_coefficients_score()
        self.show_feature_importance_score()
