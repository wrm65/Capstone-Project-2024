# Model Card - Gradient Boosting Classifier for Ofsted School Grading Prediction


## Model Description

- **Model Name:** Ofsted School Grading Predictor
- **Model Type:** GradientBoostingClassifier
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

- **Algorithm:** GradientBoostingClassifier
- **Learning Rate:** 0.5
- **Maximum Depth:** 3 (default)
- **Hyperparameter tuning:** `n_estimators` - number of boosting stages to perform
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

- `n_estimators` - number of boosting stages to perform

- **Method:** iteratively tune the `n_estimators` parameter by increasing in steps of `10`and find the best performing `n_estimators` setting

- The image below show the result of 10 iterations of the model. On each iteration the `n_estimators` hyperparameter is increased by `10`.

- The best result is also shown with the `Best accuracy score: 0.8604` and the `Best Number of boosting stages: 20`

   <div>
    <img style="width:700px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/gradient_boosting_01.png">
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
       | **Accuracy score** | &nbsp; | 0.8604 |
       | **Mean squared error** | &nbsp; | 0.2062 |
       | **Recall score** | Outstanding | 0.1483 |
       | &nbsp; | Good | 0.9444 |
       | &nbsp; | Requires Improvement | 0.0100 |
       | &nbsp; | Inadequate | 0.9977 |
       | **F1 score** | Outstanding | 0.2381 |
       | &nbsp; | Good | 0.8600 |
       | &nbsp; | Requires Improvement | 0.0190 |
       | &nbsp; | Inadequate | 0.9762 |

     </div>

   </p>

   </details>

   <details>
  <summary><b>Importance of Features:</b></summary>

  <p>

   - The image below show the importance of each feature to the model, when making the predictions.
   <table>
    <tr>
      <td valign="top"> 
      <img style="width:325px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/gradient_boosting_02.png">
      </td>
      <td valign="top"> 
      <img style="width:500px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/gradient_boosting_03.png">
      </td>
     </tr>
   </table>
  </p>

   </details>

## Use Case

- This model is provided for research, educational, and non-commercial purposes <b><u>only</u></b>.

## Version History

- **v1.0:**  Initial release (April 2024)

## References

- **Ofsted:** https://www.gov.uk/government/organisations/ofsted
