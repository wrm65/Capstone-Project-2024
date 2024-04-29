from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier

# import project libraries
from constants import *
from utility import *
from base import BaseModel

class MultiLayerPerceptronModel(BaseModel):
    """A Multilayer Perceptron classifier."""
    def __init__(self):
        # define hyperparameter to tune
        self._hidden_layer_sizes = [12, 12, 12] # ith element represents the number of neurons in the ith hidden layer
        self._max_iter = 500 # maximum number of iterations
        self._early_stopping = True #terminate training when validation score is not improving
        super().__init__(model_type = MODEL_MULTILAYER_PERCEPTRON['TYPE'], title = MODEL_MULTILAYER_PERCEPTRON['TITLE'])

    def do_pre_build_model_process(self):
        self._hyperparameter = {
            "hidden_layer_sizes": self._hidden_layer_sizes,
            "max_iter": self._max_iter,
            "early_stopping": self._early_stopping,
        }
        self.set_params(self._hyperparameter)

    # override base method
    def do_build_model(self):
        self._iteration = 0
        accuracy_score = 0
        start = 1
        end = 11
        for i in range(start, end):
            step = 10 + (i * 2)
            params = {
                "hidden_layer_sizes": [step, step, step],
                "max_iter": self._max_iter,
                "early_stopping": self._early_stopping,
            }
            self.set_params(params)
            # print(f'{TAB_SPACE}{self.get_params()}\n')
            self.do_train_n_predict()
            self.do_evaluate_model()
            print(f'{TAB_SPACE * 2}Iteration: {(i):0.0f} of {(end-1):0.0f} {COLOR_BLUE}hidden_layer_sizes: {step} accuracy score: {self._accuracy_score:0.4f}{COLOR_RESET}')
            if self._accuracy_score > accuracy_score:
                self._hidden_layer_sizes = [step, step, step]
                accuracy_score = self._accuracy_score
            self._iteration += 1
        
        self._accuracy_score = accuracy_score
        print(f'\n{TAB_SPACE}Best accuracy score: {COLOR_BLUE}{self._accuracy_score:0.4f}{COLOR_RESET}')
        print(f'{TAB_SPACE}Best Hidden layer sizes: {COLOR_BLUE}{self._hidden_layer_sizes}{COLOR_RESET}')

    # override base method
    def do_post_build_model_process(self):
        self._hyperparameter = {
            "hidden_layer_sizes": self._hidden_layer_sizes,
            "max_iter": self._max_iter,
            "early_stopping": self._early_stopping,
        }
        self.show_evaluation_score(self._hyperparameter)
        self.classification_report()
        self.show_classification_report()

