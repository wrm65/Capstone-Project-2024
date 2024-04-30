# Model Card

   - A diverse set of machine learning models was used to enhances the robustness, generalisation, interpretability, and performance of predictive models for predicting Ofsted school grading, ultimately leading to more accurate and reliable predictions.

   - The list of models, together with links to detailed documentation, are provided below.
   
   - Comparison reports showing the models' performance metrics, leaderboard and confusion matrices are also provided below.


## List of Models

1. **Decision Tree**

   - Simple and interpretable model, providing insights into decision-making process.

   <p>
   
     - [View model card](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/model_card_decision_tree.md)
   
   </p>

2. **Gaussian Naive Bayes**

   - Simple and computationally efficient.

   <p>
   
     - [View model card](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/model_card_naive_bayes.md)
   
   </p>

3. **Gradient Boosting** 

   - Ensemble method that combines the strength of multiple weak learners (decision trees) to produce a strong learner.
   - Provides feature importance scores and supports custom loss functions, allowing for flexible optimisation.

   <p>
   
     - [View model card](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/model_card_gradient_boosting.md)
   
   </p>

4. **K-Nearest Neighbors**

   - Simple and intuitive algorithm, easy to understand and implement.

   <p>
   
     - [View model card](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/model_card_knn.md)
   
   </p>

5. **Logistic Regression**

   - Simple and interpretable model, providing clear insights into the relationship between features and target variable.

   <p>
   
     - [View model card](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/model_card_logistic_regression.md)
   
   </p>

6. **Multilayer Perceptron**

   - Deep learning model capable of learning complex patterns in high-dimensional data.

   <p>
   
     - [View model card](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/model_card_multilayer_perceptron.md)
   
   </p>

7. **Random Forest**

   - Ensemble of decision trees, offering high predictive accuracy and robustness to overfitting.
   - Provides feature importance scores, aiding in feature selection and interpretation.

   <p>
   
     - [View model card](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/model_card_random_forest.md)
   
   </p>

8. **Support Vector**

   - Robust to high-dimensional data and can handle complex decision boundaries.

   <p>
   
     - [View model card](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/model_card_support_vector.md)
   
   </p>

## Comparison Reports

### Performance Metrics

   - A comparison summary report based on the performance metrics of the 8 machine learning models used to predict Ofsted school grading is provided below.
   - Based on the performance metrics, the <code>Multilayer Perceptron Classifier</code> model achieved the highest accuracy of 86.05%, closely followed by the <code>Gradient Boosting Classifier</code> with 86.04%

   <div>
    <img src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/evaluation_01.png">
   </div>

### Model Leaderboard

   - A leaderboard is provided to showcase the ranking of machine learning models based on their performance metrics, enhancing transparency and facilitates benchmarking which helps identify the best performing models. It also aids in understanding model variability and guides model selection.

   <div>
    <img src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/evaluation_04.png">
   </div>

### Confusion Matrices

   - Confusion Matrix is a performance measurement for the model classification showing the different combinations of predicted and actual values. It is extremely useful for measuring `Recall` `Precision` `Specificity` and `Accuracy` scores.
   
   <div>
    <img src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/evaluation_03.png">
   </div>

### Importance of Features

   - This additional report provides insights into the importance of features for the different machine learning models used for predicting Ofsted school grading, enhancing the understanding of how each model makes predictions and which features are most influential in the process.


   <div>
    <img style="width:700px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/evaluation_02.png">
   </div>

