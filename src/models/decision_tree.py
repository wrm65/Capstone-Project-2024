import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn import tree

# import project libraries
from constants import *
from utility import *
from base import BaseModel

class DecisionTreeModel(BaseModel):
    """A decision tree classifier."""
    def __init__(self):
        # define hyperparameter to tune
        self._max_depth = 8 # maximum depth of the tree
        self._max_leaf_nodes = 5 # grow tree with maximum number of leaf nodes
        self._leaf_node = None
        self._tree_artists = None
        super().__init__(model_type = MODEL_DECISION_TREE['TYPE'], title = MODEL_DECISION_TREE['TITLE'])
        
    def get_tree_artists_rating(self, node_id):
        node_id = '#' + str(node_id)
        for index, artist in enumerate(self._tree_artists):
            text = artist.get_text().split('\n')
            for i in range(len(text)):
                if text[i] == node_id:
                    return text[len(text)-1]
            
        return None

    def do_pre_build_model_process(self):
        self._hyperparameter = {
            "max_leaf_nodes": self._max_leaf_nodes
        }
        self.set_params(self._hyperparameter)

    # override base method
    def do_build_model(self):
        self._iteration = 0
        accuracy_score = 0
        start = 1
        end = 11
        for i in range(start, end):
            step = i * 5
            params = {
                "max_depth": self._max_depth,
                "max_leaf_nodes": step if step > 0 else None,
            }
            self.set_params(params)
            # print(f'{TAB_SPACE}{self.get_params()}\n')
            self.do_train_n_predict_model()
            self.do_evaluate_model()
            node = step if step > 0 else 'None'
            print(f'{TAB_SPACE * 2}Iteration: {(i):0.0f} of {(end-1):0.0f} {COLOR_BLUE}max_leaf_nodes: {node} accuracy score: {self._accuracy_score:0.4f}{COLOR_RESET}')
            if self._accuracy_score > accuracy_score:
                self._max_leaf_nodes = step 
                accuracy_score = self._accuracy_score
            self._iteration += 1
       
        self._accuracy_score = accuracy_score
        print(f'\n{TAB_SPACE}Best accuracy score: {COLOR_BLUE}{self._accuracy_score:0.4f}{COLOR_RESET}')
        print(f'{TAB_SPACE}Best maximum leaf nodes: {COLOR_BLUE}{self._max_leaf_nodes}{COLOR_RESET}')
 
    # override base method
    def do_post_build_model_process(self):
        self._hyperparameter = {
            "max_depth": self._max_depth,
            "max_leaf_nodes": self._max_leaf_nodes if self._max_leaf_nodes > 0 else None,
        }
        self.show_evaluation_score(self._hyperparameter)
        self.feature_importance_score()
        self.show_feature_importance_score()
        self.show_decision_tree()
        self.store_terminal_nodes()
        self.print_terminal_nodes_summary()
        
    def show_decision_tree(self):
        print(f'\n{COLOR_INVERSE}{COLOR_BLUE} Show Decision Tree: {COLOR_RESET}\n')
        height = 6
        if self._max_leaf_nodes > 10:
            height = 10
        fig = plt.figure(figsize=(14, height))
        self._tree_artists = tree.plot_tree(self._model,
                                            feature_names = SCHOOL_FEATURES,
                                            class_names = CLASSIFICATION,
                                            filled = True,
                                            label = 'none',
                                            node_ids = True,
                                            impurity = False,
                                            rounded = True,
                                            fontsize = 6)
        plt.show()
        
    def store_terminal_nodes(self):
        leaf_index = pd.DataFrame(self._model.apply(self._dataset.get_X_train()),
                                  columns=['leaf_index'],
                                  index=self._dataset.get_y_train().index)
        self._leaf_node = pd.concat([leaf_index, self._dataset.get_y_train()], 
                                    axis=1)\
                                    .groupby('leaf_index')\
                                    .apply(lambda x: x[self._dataset._output_column].unique())\
                                    .to_frame('leaf_values').reset_index()
        self._leaf_node['leaf_size'] = self._leaf_node.leaf_values.apply(len)
        self._leaf_node[self._dataset._output_column] = pd.Series(dtype='object')
        # set grading for leaf node
        for index, data in self._leaf_node.iterrows():
            self._leaf_node.loc[index, self._dataset._output_column] = self.get_tree_artists_rating(data['leaf_index'])
            
    def print_terminal_nodes_summary(self):
        print(f'\n{COLOR_INVERSE}{COLOR_BLUE} Decision Tree Leaf Summary: {COLOR_RESET}\n')
        total_node = 0
        for index, grade in enumerate(CLASSIFICATION):
            total_leaf = (self._leaf_node[self._dataset._output_column] == grade).sum()
            print(f'{index+1}.{TAB_SPACE}{COLOR_BOLD}{COLOR_BLUE}{grade:<25}{total_leaf}{COLOR_RESET}')
            total_node += total_leaf
        print(f'\n{TAB_SPACE}{COLOR_BOLD}{COLOR_BLUE}Total leaf nodes: {total_node}{COLOR_RESET}\n')
