# Model Card - LogisticRegressionClassifier for Ofsted School Grading Prediction


## Model Description

- **Model Name:** Ofsted School Grading Predictor
- **Model Type:** LogisticRegressionClassifier
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

- **Algorithm:** LogisticRegression
- **Maximum Iterations:** Maximum number of iterations taken for the solvers to converge set to 500
- **multi_class:** Maximum number of iterations taken for the solvers to converge set to 500
- **Regularization:** L2 regularization (default)
- **Solver:** lbfgs (default)
- **Other Hyperparameter:** Default settings used for other hyperparameters.

## Training Data

- **Source:** Ofsted Inspected School Dataset
- **Data Size:** 20,571 school records
- **Preprocessing:** remove irrevlevant (8) columns, encode categorical variables (rating)
- **Input:** For each school, nine features are provided for the model to be trained and predict its grading.
   <details>
  <summary>Click to view these features</summary>
    <p>
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
   </details>

- **Output:** The model outputs one of the four Ofsted school grading.

## Performance

   <div>
   <details open>
  <summary><b>Hyperparameter tuning:</b></summary>

- `max_iter` - Maximum number of iterations taken for the solvers to converge set to `500`

- `multi_class` - the loss minimised is the multinomial loss fit across the entire probability distribution set to `multinomial`

   </details>
   </div>

   <details open>
  <summary><b>Metrics:</b></summary>

   <p>

   - `accuracy score` `recall score` `f1 score` `mean squared error`

   - The table below show the metric scores obtained for each classification (grading).

     <div>

       | Metric | Rating | Score |
       | --- | -- | --- |
       | **Accuracy score** | &nbsp; | 0.8557 |
       | **Mean squared error** | &nbsp; | 0.2178 |
       | **Recall score** | Outstanding | 0.0353 |
       | &nbsp; | Good | 0.9532 |
       | &nbsp; | Requires Improvement | 0.9998 |
       | &nbsp; | Inadequate | 0 |
       | **F1 score** | Outstanding | 0.0665 |
       | &nbsp; | Good | 0.8574 |
       | &nbsp; | Requires Improvement | 0.9728 |
       | &nbsp; | Inadequate | 0 |

     </div>

   </p>

   </details>

   <details>
  <summary><b>Importance of Features:</b></summary>

  <p>

   - The image below show the importance of each feature to the model, when making the predictions.
     <div style="display:flex">
       <div style="float:left">
        <img style="width:325px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/logistic_regression_02.png">
       </div>

       <div style="float:right">
        <img style="width:500px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/logistic_regression_03.png">
       </div>
     </div>

  </p>

   </details>

