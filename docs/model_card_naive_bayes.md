# Model Card - NaiveBayesClassifier for Ofsted School Grading Prediction

## Model Description

- **Model Name:** Ofsted School Grading Predictor
- **Model Type:** NaiveBayesClassifier
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

- **Algorithm:** Gaussian Naive Bayes
- **Hyperparameter:** Default settings used for other hyperparameters.

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

- **Metric:** `accuracy score` `recall score` `f1 score` `mean squared error`

   <p>

   - The table below show the metric scores obtained for each classification (grading).

     <div>

       | Metric | Rating | Score |
       | --- | -- | --- |
       | **Accuracy score** | &nbsp; | 0.8466 |
       | **Mean squared error** | &nbsp; | 0.2343 |
       | **Recall score** | Outstanding | 0.1749 |
       | &nbsp; | Good | 0.9050 |
       | &nbsp; | Requires Improvement | 0.0133 |
       | &nbsp; | Inadequate | 1.0 |
       | **F1 score** | Outstanding | 0.2396 |
       | &nbsp; | Good | 0.8447 |
       | &nbsp; | Requires Improvement | 0.0250 |
       | &nbsp; | Inadequate | 0.9724 |

     </div>

   </p>

## Use Case

- This model is provided for research, educational, and non-commercial purposes <b><u>only</u></b>.

## Version History

- **v1.0:**  Initial release (April 2024)

## References

- **Ofsted:** https://www.gov.uk/government/organisations/ofsted
