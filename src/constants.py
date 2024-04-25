# ========= Dataset ===============
DATASET_PATH = './dataset/'
DATASET_FILENAME = 'school_ofsted_rating.csv'
COLUMN_INPUTS_START = 0
COLUMN_INPUTS_END = 17
COLUMN_OUTPUT = 18

# ========= School Features ===============
FEATURE_GENDER_TYPE = "Gender Type"
FEATURE_RELIGIOUS_TYPE = "Religious Type"
FEATURE_PERCENT_PUPIL_BOYS = "Pupil Boys %"
FEATURE_PERCENT_PUPIL_GIRLS = "Pupil Girls %"
FEATURE_PERCENT_EHC_PLAN = "ehc_plan %"
FEATURE_PERCENT_SEN_SUPPORT = "Sen Support %"
FEATURE_PERCENT_ENGLISH_LANGUAGE = "English Language %"
FEATURE_PERCENT_NOT_ENGLISH_LANGUAGE = "Not English Language %"
FEATURE_PERCENT_FREE_SCHOOL_MEALS = "Free School Meals %"

SCHOOL_FEATURES = [FEATURE_GENDER_TYPE, FEATURE_RELIGIOUS_TYPE, 
                   FEATURE_PERCENT_PUPIL_BOYS, FEATURE_PERCENT_PUPIL_GIRLS,
                   FEATURE_PERCENT_EHC_PLAN, FEATURE_PERCENT_SEN_SUPPORT,
                   FEATURE_PERCENT_ENGLISH_LANGUAGE, 
                   FEATURE_PERCENT_NOT_ENGLISH_LANGUAGE,
                   FEATURE_PERCENT_FREE_SCHOOL_MEALS]

# ========= Classification ===============
GRADING_OUTSTANDING = "Outstanding"
GRADING_SERIOUS_WEAKNESSES = "Serious Weaknesses"
GRADING_INADEQUATE = "Inadequate"
GRADING_GOOD = "Good"
GRADING_SPECIAL_MEASURES = "Special Measures"
GRADING_REQUIRES_IMPROVEMENT = "Requires Improvement"

CLASSIFICATION = [GRADING_OUTSTANDING, GRADING_GOOD, 
				  GRADING_REQUIRES_IMPROVEMENT, GRADING_INADEQUATE]

# ========= Rating Models =============
MODEL_DECISION_TREE = {
    "TYPE": 1,
    "TITLE": "Decision Tree"
}
MODEL_RANDOM_FOREST = {
    "TYPE": 2,
    "TITLE": "Random Forest"
}
MODEL_KNN = {
    "TYPE": 3,
    "TITLE": "KNearest"
}
MODEL_SUPPORT_VECTOR = {
    "TYPE": 4,
    "TITLE": "Support Vector Classifier"
}
MODEL_LOGISTIC_REGRESSION = {
    "TYPE": 5,
    "TITLE": "Logistic Regression"
}
MODEL_NAIVE_BAYES = {
    "TYPE": 6,
    "TITLE": "Naive Bayes"
}
MODEL_GRADIENT_BOOSTING = {
    "TYPE": 7,
    "TITLE": "Gradient Boosting"
}
MODEL_MULTILAYER_PERCEPTRON = {
    "TYPE": 8,
    "TITLE": "Multi Layer Perceptron"
}

# ========= Embedded Print Code =============
BG_RED = '\033[1;30;41m'

COLOR_BLACK = '\033[1;30m'
COLOR_RESET = '\033[0m'

COLOR_BOLD = '\033[1m'
COLOR_MAGENTA = '\033[95m'
COLOR_CYAN = '\033[96m'
COLOR_DARKCYAN = '\033[36m'
COLOR_GREEN = '\033[92m'
COLOR_GRAY = '\033[37m'
COLOR_PURPLE = '\033[95m'
COLOR_UNDERLINE = '\033[4m'
COLOR_YELLOW = '\033[93m'

CHECKPOINT_FILE_EXT = '.pt'

#  inverse codes
COLOR_RED = '\033[1;31m'
COLOR_BLUE = '\033[1;34m'
COLOR_GREEN = '\033[1;92m'
COLOR_YELLOW = '\033[1;33m'
COLOR_INVERSE = '\033[7;21m'
COLOR_INVERSE_RED = '\033[7;31m'

# ========= Miscellaneous values =============
LOG_PATH = './log/'
LOG_FILENAME = 'capstone'
LOG_FILE_EXT = '.log'
TAB_SPACE = ' '*2
DEBUG_LEVEL = 0
DEFAULT_SETTINGS = '<default settings>'

COLUMN_NAME_PERCENTAGE = 'Percentage'

