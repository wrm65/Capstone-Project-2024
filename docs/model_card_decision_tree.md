# Model Card - DecisionTreeClassifier for Ofsted School Grading Prediction


## Model Description

- **Model Name:** Ofsted School Grading Predictor
- **Model Type:** DecisionTreeClassifier
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

- **Algorithm:** DecisionTreeClassifier
- **Criterion:** Gini impurity
- **Maximum Depth:** Tree depth set to 8
- **Hyperparameter:** Maximum number of leaf nodes

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
   <details>
  <summary><b>Hyperparameter tuning:</b></summary>
  
- `max_leaf_nodes` - grow tree with maximum number of leaf nodes
   
- **Method:** iteratively tune the `max_leaf_nodes` parameter by increasing in steps of `5`and find the best performing `max_leaf_nodes` setting

- The image below show the result of 10 iterations of the model. On each iteration the `max_leaf_nodes` hyperparameter is increased by 5.

- The best result is also shown with the `Best accuracy score: 0.8599` and the `Best maximum leaf nodes: 35`

   <div>
    <img style="width:700px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/decision_tree_01.png">
   </div>

   </details>
   </div>

   <div>
   <details>
  <summary><b>Metrics:</b></summary>

   <p>
  
   - `accuracy score` `recall score` `f1 score` `mean squared error`

   - The table below show the metric scores obtained for each classification (grading).
   </p>
  
  <div>
  
    <p>

   | Metric | Rating | Score |
   | --- | -- | --- |
   | **Accuracy score** | &nbsp; | 0.8599 |
   | **Mean squared error** | &nbsp; | 0.2094 |
   | **Recall score** | Outstanding | 0.1130 |
   | &nbsp; | Good | 0.9522 |
   | &nbsp; | Requires Improvement | 0 |
   | &nbsp; | Inadequate | 0.9963 |
   | **F1 score** | Outstanding | 0.1924 |
   | &nbsp; | Good | 0.8603 |
   | &nbsp; | Requires Improvement | 0 |
   | &nbsp; | Inadequate | 0.9743 |

   </p>

  </div>

   </details>
   </div>

   <details>
  <summary><b>Importance of Features:</b></summary>
  
   <p>
  
   - The image below show the importance of each feature to the model, when making the predictions.
   </p>
  
   <div>
   <img style="width:325px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/decision_tree_02.png">
   </div>

   </details>

   <details>
  <summary><b>Decision Tree Leaf Summary:</b></summary>

   <p>
  
   - With the maximum tree depth set to 8, the model produced 35 leaf nodes. The image below show the classification prediction for the 35 leaf nodes.
   </p>
  
    <img style="width:250px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/decision_tree_03.png">

   </details>

## Limitations

<p>
  <div>
    There are two distinct limitations in the implementation of the model:
    <ul>
    <li><b>Tree depth:</b> the tree depth is set to a maximum of 8</li>
    <li><b>Leaf Nodes:</b> the maximum leaf nodes is 50</li>
    </ul>
  <div>
    This limitation was implemented to control the complexity of the model and improve both its interpretability and the examination of the tree structure to understand the decision rules used for classification.
  </div>
  <div>
</p>

## Ethical Considerations

- When using machine learning models to predict Ofsted school grading or any other educational outcome, it's crucial to consider several ethical considerations to ensure fairness, transparency, and accountability.

- Decision trees are highly interpretable models, making it easy to understand and explain how predictions are made. The decision rules learned by the model can be visualised as a tree structure, allowing stakeholders to see the sequence of criteria used to classify schools into different grades.

## Use Case

- This model is provided for research, educational, and non-commercial purposes <b><u>only</u></b>.

## Version History

- **v1.0:**  Initial release (April 2024)

## References

- **Ofsted:** https://www.gov.uk/government/organisations/ofsted
