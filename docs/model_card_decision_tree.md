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

**Model Architecture:** Decision Tree Classifier

## Performance

Give a summary graph or metrics of how the model performs. Remember to include how you are measuring the performance and what data you analysed it on. 

## Limitations

Outline the limitations of your model.

## Trade-offs

Outline any trade-offs of your model, such as any circumstances where the model exhibits performance issues. 