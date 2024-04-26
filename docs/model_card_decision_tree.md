# Model Card

## Model Description

**Name:** Ofsted School Grading Model

**Version:** 0.1

**Usage:** This model is use to predict the likely grade that a school would receive on its next inspection by [Ofsted](https://www.gov.uk/government/organisations/ofsted). There are four Ofsted school gradings that can be classified:
1. Outstanding
2. Good
3. Requires Improvement
4. Inadequate

**Input:** For each school, nine features are provided for the model to be trained and predict its grading. These features are listed below.
1. Gender Type - girls, boys, mixed
2. Religious Ethos - Church of England, Roman Catholic, Other religion and non-faith
3. Percentage of Pupils who are Boys
4. Percentage of Pupils who are Girls
5. Percentage of Pupils who have Enhance Health Care plan
6. Percentage of Pupils who have Special Education Needs
7. Percentage of Pupils who receive Free School Meals
8. Percentage of Pupils who first language is English
9. Percentage of Pupils who first language is not English


**Output:** The model outputs one of the four Ofsted school grading.

**Model Architecture:** Decision Tree Classifier with a maximum tree depth set to 8.

## Performance

**Hyperparameter tuning:** `max_depth` - maximum depth of the tree `max_leaf_nodes` - grow tree with maximum number of leaf nodes

**Method:** iteratively tune the `max_leaf_nodes` parameter by increasing in steps of `5`and find the best performing `max_leaf_nodes` setting

The image below show the result of 10 iterations of the model. On each iteration the `max_leaf_nodes` hyperparameter is increased by 5.

The best result is also shown with the `Best accuracy score: 0.8599` and the `Best maximum leaf nodes: 35`

 <div>
	<img style="width:800px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/decision_tree_01.png">
 </div>

---


**Metrics:** `accuracy score` `recall score` `f1 score` `mean squared error`

	
| Metric |  Value |
| --- | --- |
| Accuracy score | 0.8599 |
| Mean squared error | 0.2094 |
| Recall score | Outstanding: 0.1130 |
| &nbsp; | Good: 0.9522 |
| &nbsp; | Requires Improvement: 0 |
| &nbsp; | Inadequate: 0.9963 |
| F1 score | Outstanding: 0.1924 |
| &nbsp; | Good: 0.8603 |
| &nbsp; | Requires Improvement: 0 |
| &nbsp; | Inadequate: 0.9743 |


**Importance of Features:** 

## Limitations

Outline the limitations of your model.

## Trade-offs

Outline any trade-offs of your model, such as any circumstances where the model exhibits performance issues. 
