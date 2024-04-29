from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# import project libraries
from constants import *
from utility import *
from base import BaseModel

class NaiveBayesModel(BaseModel):
    """Naive Bayes classifier."""
    def __init__(self):
        super().__init__(model_type = MODEL_NAIVE_BAYES['TYPE'], title = MODEL_NAIVE_BAYES['TITLE'])

