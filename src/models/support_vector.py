from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

# import project libraries
from constants import *
from utility import *
from base import BaseModel

class SupportVectorModel(BaseModel):
    """Support Vector classifier."""
    def __init__(self):
        self._decision_function_shape = "ovo" # used as a multi-class strategy to train models
        self._kernel = "rbf" # kernel type to be used in the algorithm
        super().__init__(model_type = MODEL_SUPPORT_VECTOR['TYPE'], title = MODEL_SUPPORT_VECTOR['TITLE'])

    # override base method
    def do_pre_build_model_process(self):
        # apply parameter(s) to model
        self._hyperparameter = {
            "decision_function_shape": self._decision_function_shape,
            "kernel": self._kernel
        }
        self.set_params(self._hyperparameter)

