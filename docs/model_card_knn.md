# Model Card - K-Nearest Neighbors Classifier for Ofsted School Grading Prediction


## Model Description

- **Model Name:** Ofsted School Grading Predictor
- **Model Type:** KNeighborsClassifier
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

- **Algorithm:** KNeighborsClassifier
- **Weights:** Uniform (default)
- **Distance Metric:** Euclidean distance (default)
- **Hyperparameter tuning:** `n_neighbors` - number of neighbors to use by default for kneighbors
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

- `n_neighbors` - number of neighbors to use by default for kneighbors

- **Method:** iteratively tune the `n_neighbors` parameter by increasing in steps of `10`and find the best performing `n_neighbors` setting

- The image below show the result of 10 iterations of the model. On each iteration the `n_neighbors` hyperparameter is increased by `10`.

- The best result is also shown with the `Best accuracy score: 0.8577` and the `Best Number of neighbors: 20`

   <div>
    <img style="width:700px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/knn_01.png">
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
       | **Accuracy score** | &nbsp; | 0.8577 |
       | **Mean squared error** | &nbsp; | 0.2117 |
       | **Recall score** | Outstanding | 0.0904 |
       | &nbsp; | Good | 0.9480 |
       | &nbsp; | Requires Improvement | 0.9995 |
       | &nbsp; | Inadequate | 0 |
       | **F1 score** | Outstanding | 0.1548 |
       | &nbsp; | Good | 0.8581 |
       | &nbsp; | Requires Improvement | 0.9748 |
       | &nbsp; | Inadequate | 0 |

     </div>

   </p>

   </details>

## Use Case

- This model is provided for research, educational, and non-commercial purposes <b><u>only</u></b>.

## Version History

- **v1.0:**  Initial release (April 2024)

## References

- **Ofsted:** https://www.gov.uk/government/organisations/ofsted
