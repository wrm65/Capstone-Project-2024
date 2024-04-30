<div>
  <table>
  <tr>
    <td> 
      # Capstone-Project-2024
    </td>
    <td valign="top"> 
      <img src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/imperial_college_logo.png">
    </td>
   </tr>
  </table>
</div>


Imperial College Business School Capstone Project 2024
<div align="center">
	<img style="width:350px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/confusion_matrix.png">
</div>

## Predicting Ofsted School Grading with Machine Learning Models
- Welcome to our repository for predicting Ofsted school grading using machine learning models! 
- This project aims to provide insights into school performance based on various features and criteria. 
- We have developed and evaluated eight different machine learning models to predict Ofsted school grading. 
- Below, you'll find links to detailed documentation for each one.

<div align="right">
  <img style="width:90px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/ofsted-logo.png">
</div>

### Overview
- In the UK, Ofsted (Office for Standards in Education, Children's Services and Skills) evaluates schools based on various criteria to ensure high-quality education. 
- Our project leverages advanced machine learning models to predict Ofsted school grading.
- The models are trained on a dataset consisting of Ofsted school inspection reports.

<div align="right">
  <img style="width:250px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/pie_chart.png">
</div>


### Model Cards and Datasheet
- Before exploring the models, we encourage you to review the Model Cards and Datasheet for more detailed information on each model and the dataset used.

- **Model Cards:** Provides detailed information about each model, including its architecture, training data, evaluation metrics, and ethical considerations.

   <p>
   
     - [View Model Card](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/model_card.md)
   
   </p>

- **Datasheet:** Offers insights into the dataset used for training the models, including its source, size, features, preprocessing steps, and permitted uses.

   <p>
   
     - [View Datasheet for Dataset](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/datasheet.md)
   
   </p>

- **Models Included:** Our repository includes the following machine learning models:

   <p>
    <ol type="1">
    <li>Decision Tree Classifier</li>
    <li>Gradient Boosting Classifier</li>
    <li>K-Nearest Neighbors Classifier</li>
    <li>Logistic Regression</li>
    <li>Multilayer Perceptron Classifier</li>
    <li>Naive Bayes</li>
    <li>Random Forest Classifier</li>
    <li>Support Vector Classifier</li>
    </ol>
   </p>

### Model Evaluation
- The following four comparison reports have been produced to compare and select the best model for predicting Ofsted school grading:
   <p>
    <ol type="1">
    <li><b>Performance Metrics:</b> Evaluate the performance of each model using metrics such as accuracy, F1 score, precision, and recall.</li>
    <li><b>Model Leaderboard:</b> Consider the relative ranking of models across different metrics to gain a comprehensive understanding of their overall performance.</li>
    <li><b>Confusion Matrices:</b> Identify models that exhibit balanced performance across all classes, with minimal misclassification errors.</li>
    <li><b>Importance of Features:</b>Identify models that provide clear insights into the relationship between input features and target variable, aiding in model interpretation and understanding.</li>
    </ol>
   </p>

  <p>
    <img src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/evaluation_04a.png">
  </p>

  - [View Comparison Reports](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/model_card.md#comparison-reports)
   

### Ethical Considerations
- Using machine learning models for predicting Ofsted school grading raises several ethical considerations that must be carefully addressed to ensure fairness, transparency, and accountability. Here are some key ethical considerations:
   <p>
    <ol type="1">
    <li><b>Fairness and Bias:</b> Machine learning models can inadvertently perpetuate or amplify biases present in the data used for training. It's essential to assess and mitigate biases related to race, gender, socioeconomic status, and other protected characteristics to ensure fair and equitable predictions. This may involve carefully selecting features, collecting diverse training data, and applying fairness-aware algorithms to prevent discrimination.</li>
    <li><b>Transparency and Explainability:</b> Machine learning models should be transparent and interpretable, allowing stakeholders to understand how predictions are made and why certain decisions are reached. Providing explanations for model predictions can help build trust and accountability, enabling stakeholders to assess the model's reliability and identify potential sources of bias or error.</li>
    <li><b>Human Oversight and Intervention:</b> While machine learning models can automate certain aspects of decision-making, human oversight and intervention are essential to ensure ethical and responsible use. Human experts should have the ability to review and override model predictions, especially in cases where the stakes are high or the potential for harm is significant.</li>
    </ol>
   </p>

### Conclusion
- Based on the performance metrics, the Multilayer Perceptron Classifier model achieved the highest accuracy of 86.05%, closely followed by the Gradient Boosting Classifier with 86.04% for predicting Ofsted school grading. 
- However, it's essential to consider other factors such as interpretability, computational complexity, and ethical considerations when selecting the best model.
- By considering insights from the four evaluation reports collectively, the model which is best suited for predicting Ofsted school grading is the <b>Decision Tree Classifier</b>.
- Using the [DecisionTreeClassifier model](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/model_card_decision_tree.md) to predict Ofsted school grading offers several advantages that make it preferable in certain scenarios:
   <p>
    <ol type="1">
    <li><b>Interpretability:</b> Decision trees are inherently interpretable models, meaning that the decision-making process is transparent and easy to understand. This is especially important in educational settings where stakeholders such as teachers, administrators, and policymakers need to comprehend the factors driving school grading decisions.</li>
    <li><b>Feature Importance:</b> Decision trees provide insight into the relative importance of different features in predicting school grading. By examining the decision rules and splits in the tree, stakeholders can identify which features have the greatest influence on the classification outcome. This information can inform targeted interventions and improvement strategies.</li>
    <li><b>Natural Representation of Decision-Making:</b> Decision trees mimic human decision-making processes, making them intuitive and easy to relate to for stakeholders. This natural representation can facilitate discussions and collaboration between educators, policymakers, and other stakeholders involved in education quality and improvement efforts.</li>
    </ol>
   </p>


### Future development and recommendations
- The dataset that was used to train the models had a very limited set of features about the schools. It is highly recommendation a more comprehensive set of features be obtained that capture various aspects of school performance, demographics, resources, and other relevant factors. Some potential features that could be used are:
   <p>
    <ol type="1">
    <li>Pupil Outcomes</li>
    <li>Student-teacher ratio</li>
    <li>Trends in performance over time</li>
    <li>Funding levels and resources available</li>
    <li>Parental involvement and engagement</li>
    <li>Demographic and Socioeconomic Factors</li>
    <li>Quality of teacher training and ongoing support</li>
    </ol>
   </p>


### Project Report

  - [Knowledge Gained](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/project_report.md)

    
### Contact

- Winston Menzies
- winston.menzies@grammology.education
<div align="left">
  <img src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/email_logo-01_190x65.png">
</div>
