# Model Card - RandomForestClassifier for Ofsted School Grading Prediction


## Model Description

- **Model Name:** Ofsted School Grading Predictor
- **Model Type:** RandomForestClassifier
- **Purpose:** This model is use to predict the likely grade that a school would receive on its next inspection by Ofsted based on various features and criteria. 
   <p>
		There are four Ofsted school gradings that can be classified:
    <ol type="1">
		<li>Outstanding</li>
		<li>Good</li>
		<li>Requires Improvement</li>
		<li>Inadequate</li>
    </ol>
   </p>

## Model Architecture

- **Algorithm:** RandomForestClassifier
- **Number of Trees:** maximum of 500
- **Criterion:** Gini impurity
- **Maximum Depth:** None (default)
- **Hyperparameter:** Default settings used for other hyperparameters.

## Training Data

- **Source:** Ofsted Inspected School Dataset
- **Data Size:** 20,571 school records
- **Preprocessing:** remove irrevlevant (8) columns, encode categorical variables (rating)
- **Input:** For each school, nine features are provided for the model to be trained and predict its grading.
   <p>
    These features are listed below.
    <ol type="1">
		<li>Gender Type - girls, boys, mixed</li>
		<li>Religious Ethos - Church of England, Roman Catholic, Other religion and non-faith</li>
		<li>Percentage of Pupils who are Boys</li>
		<li>Percentage of Pupils who are Girls</li>
		<li>Percentage of Pupils who have Enhance Health Care plan</li>
		<li>Percentage of Pupils who have Special Education Needs</li>
		<li>Percentage of Pupils who receive Free School Meals</li>
		<li>Percentage of Pupils who first language is English</li>
		<li>Percentage of Pupils who first language is not English</li>
    </ol>
   </p>

- **Output:** The model outputs one of the four Ofsted school grading.

## Performance

- **Hyperparameter tuning:** `n_estimators` - grow tree with maximum number of leaf nodes
- **Method:** iteratively tune the `n_estimators` parameter by increasing in steps of `50`and find the best performing `n_estimators` setting

   The image below show the result of 10 iterations of the model. On each iteration the `n_estimators` hyperparameter is increased by 50.

   The best result is also shown with the `Best accuracy score: 0.8560` and the `Best estimators: 350`

   <div>
    <img style="width:700px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/random_forest_01.png">
   </div>
	 
---


