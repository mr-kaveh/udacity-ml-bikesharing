# Report: Predict Bike Sharing Demand with AutoGluon Solution
#### Hossein Davoodi

## Initial Training
### What did you realize when you tried to submit your predictions? What changes were needed to the output of the predictor to submit your results?
I realized that kaggle won't accept my prediction results if the values are negative. so i had to detect negative values in my predictions and set them to 0.

### What was the top ranked model that performed?
Model with hyperparameters's higher mean could indicate better performance in terms of predicting the target variable, but the presence of negative values and higher variability suggests it may also have made more erroneous predictions, but i  would say it still performed better among the 3.

## Exploratory data analysis and feature creation
### What did the exploratory analysis find and how did you add additional features?
exploratory analysis aims to uncover patterns, relationships, and insights within a dataset. When applied to a model, explanatory analysis helps to understand various aspects of the model's performance, behavior, and underlying data. the added feature **hour** has been extracted from the datetime
and added to the data.
    # creating a new feature
    train["hour"] = train["datetime"].dt.hour
    test["hour"] = test["datetime"].dt.hour 

### How much better did your model preform after adding additional features and why do you think that is?
less STD of the model with additional features, and higher Quartiles (25th, 50th, 75th percentiles) values suggest the model with additional features performed better, but if that's the case the model did not yield significantly better performance.

## Hyper parameter tuning
### How much better did your model preform after trying different hyper parameters?
here is how it worked for me:

**Mean**: Model with Hyper parameter tuning has a significantly higher mean compared to other 2 Models.

**Standard Deviation**: Models 1 and 2 have similar standard deviations, while Model with Hyper parameter tuning has a higher standard deviation.

**Minimum and Maximum**: my Model has a negative minimum value, which suggests some predictions may be unrealistic or incorrect.

**Quartiles (25th, 50th, 75th percentiles)**: Model with Hyper parameter tuning has notably higher quartile values compared to Models 1 and 2.

### If you were given more time with this dataset, where do you think you would spend more time?
first of all, i would have added more additional features and afterwards , i would have tried to manipulate Hyper parameters to find the best performance

### Create a table with the models you ran, the hyperparameters modified, and the kaggle score.
|model|hpo1|hpo2|hpo3|score|
|--|--|--|--|--|
|initial|0.05|252|85|1.74418|
|add_features|0.05|240|88|0.72097|
|hpo|0.03|297|1|1.34103|

### Create a line plot showing the top model score for the three (or more) training runs during the project.

![model_train_score.png](dataSets/model_train_score.png)

### Create a line plot showing the top kaggle score for the three (or more) prediction submissions during the project.

![model_test_score.png](model_test_score.png)

## Summary
the model i was given, i first tarined and did a prediction of then , i have added the additional features and trained it, and afterwards by tuning hyperparameters i could get a relatively better performance at the end.