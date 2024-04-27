# Model Card - Multilayer Perceptron Classifier for Ofsted School Grading Prediction


## Model Description

- **Model Name:** Ofsted School Grading Predictor
- **Model Type:** Multilayer Perceptron Classifier
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

- **Algorithm:** MLPClassifier
- **Activation Function:** ReLU for hidden layers
- **Solver:** Adam optimizer (default)
- **Maximum number of iterations:** `max_iter` set to 500
- **Early Stopping:** `early_stopping` set to True
- **Hyperparameter tuning:** `hidden_layer_sizes` - ith element represents the number of neurons in the ith hidden layer
- **Other Hyperparameter:** Default settings used for other hyperparameters.

## Training Data

- **Source:** Ofsted Inspected School Dataset
- **Data Size:** 20,571 school records
- **Preprocessing:** remove irrevlevant (8) columns, encode categorical variables (rating)
- **Input:** For each school, nine features are provided for the model to be trained and predict its grading.
   <details>
  <summary>Click to view features</summary>
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

- `hidden_layer_sizes` - ith element represents the number of neurons in the ith hidden layer

- **Method:** iteratively tune the `hidden_layer_sizes` parameter by increasing in steps of `2`and find the best performing `hidden_layer_sizes` setting

- The image below show the result of 10 iterations of the model. On each iteration the `hidden_layer_sizes` hyperparameter is increased by `2`.

- The best result is also shown with the `Best accuracy score: 0.8605` and the `Best Hidden layer sizes: [30, 30, 30]`

   <div>
    <img style="width:700px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/mlp_01.png">
   </div>
	 
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
       | **Accuracy score** | &nbsp; | 0.8605 |
       | **Mean squared error** | &nbsp; | 0.2041 |
       | **Recall score** | Outstanding | 0.0668 |
       | &nbsp; | Good | 0.9595 |
       | &nbsp; | Requires Improvement | 0 |
       | &nbsp; | Inadequate | 0.9988 |
       | **F1 score** | Outstanding | 0.1223 |
       | &nbsp; | Good | 0.8615 |
       | &nbsp; | Requires Improvement | 0 |
       | &nbsp; | Inadequate | 0.9762 |

     </div>

   </p>

   </details>

   <details>
  <summary><b>Classification Report:</b></summary>

  <p>

   - The image below show the classification report which provides a comprehensive overview of various evaluation metrics for each class in the dataset, including precision, recall, F1-score, and support.

     <div>
      <img style="width:500px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/mlp_02.png">
     </div>

  </p>

   </details>

## Use Case

- This model is provided for research, educational, and non-commercial purposes <b><u>only</u></b>.

## Version History

- **v1.0:**  Initial release (April 2024)

## References

- **Ofsted:** https://www.gov.uk/government/organisations/ofsted

