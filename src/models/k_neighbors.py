from sklearn.neighbors import KNeighborsClassifier

# import project libraries
from constants import *
from utility import *
from base import BaseModel

class KNeighborsModel(BaseModel):
    """A k nearest neighbors classifier."""
    def __init__(self):
        # define hyperparameter to tune
        self._n_neighbors = 10 # number of neighbors to use by default for kneighbors queries
        super().__init__(model_type = MODEL_KNN['TYPE'], title = MODEL_KNN['TITLE'])

    def do_pre_build_model_process(self):
        self._hyperparameter = {
            "n_neighbors": self._n_neighbors
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
                "n_neighbors": step,
            }
            self.set_params(params)
            # print(f'{TAB_SPACE}{self.get_params()}\n')
            self.do_train_n_predict()
            self.do_evaluate_model()
            print(f'{TAB_SPACE * 2}Iteration: {(i):0.0f} of {(end-1):0.0f} {COLOR_BLUE}n_neighbors: {step} accuracy score: {self._accuracy_score:0.4f}{COLOR_RESET}')
            if self._accuracy_score > accuracy_score:
                self._n_neighbors = step
                accuracy_score = self._accuracy_score
            self._iteration += 1
        
        self._accuracy_score = accuracy_score
        print(f'\n{TAB_SPACE}Best accuracy score: {COLOR_BLUE}{self._accuracy_score:0.4f}{COLOR_RESET}')
        print(f'{TAB_SPACE}Best Number of neighbors: {COLOR_BLUE}{self._n_neighbors}{COLOR_RESET}')
 
    # override base method
    def do_post_build_model_process(self):
        self._hyperparameter = {
            "n_neighbors": self._n_neighbors
        }
        self.show_evaluation_score(self._hyperparameter)
