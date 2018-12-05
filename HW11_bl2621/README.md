## Time Series Analysis:

### DATA:
MTA subway fares. It is a complete dataset of rides logged by card swipes for 600 Manhattan stations.

The data was organized by Sina Kashuk at CUSP.

It contains 23 different subway card types (e.g., monthly pass, daily pass, Act for Disability pass…).

### Task 1: Event detection: 

Identified the most prominent event. Used the 3-sigma as the threshold. As a result, there is a drop in the 126th week, around October/20/ 2012. 

According to the news, Hurricane Sandy, the superstorm damaged New York's mass transit system.

### Task 2: Finding Trends:

Calculated the rolling mean of the time series with windows = 10. Identified the trends. 

The steepest increase belongs to the 17th card type. The 13th card type has the sharpest decrease.

### Task 3: Build models that classified the ride type based on the time series characteristics using random forests.

#### The first model: 

created four features:

The first feature is the mean of that time series compared to the mean of any time series in that station.

The second feature is the std of that time series/std of any time series in that station

The third feature is the intercept of the line fit of the time series. (After a serious analysis, not standardized time series is used in this feature)

The fourth feature is the Coefficient of the line.

#### The second model:

used each timestamp as input features (194 features).

For both models:

Plotted the confusion matrix for each model. Compared the models using sklearn. Metrics classification_report. As a result, the model with 194 features predicts slightly better. The confusion matrix of these two models looked similar. 

Find the most essential features in each model: The top 2 crucial feature in the first model is mean and coefficient. The top 2 important feature in the second model is 13th and 34th week.

Changed the size of my legend table in Homework 8/Assignment_1.

Group Work: With Evgeniya