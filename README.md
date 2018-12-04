# flight_delays
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/shivaninyc/flight_delays/blob/master/LICENSE)

Modeling Flights Delay and Cancellation Based On Flight Information And Weather Data

## Purpose of this research
As per a study done by researchers in 2010 at University of California, Berkeley, the domestic flight delays cost puts a $33 billion dent into the US economy and about half of that cost is borne by the passengers. With accurate data readily available, I decided to model flight delays using flight and weather data. I tried to predict flight delays, cancellation and length of delay. I hope my research will alleviate some of the costs caused by domestic flight delays. 

## Goals of my study
* Goal 1: Based on flight information (flight, airline, time, origin, destination etc.) and weather features (temp, humidity, rain, precipitation, snow, snow depth, wind speed etc.), I will build a model which will predict if the flight is going to be delayed (more than 15 mins) or not.
* Goal 2: I will also run a regression model to predict by how much the flight will be delayed.
* Goal 3: Finally, I will model and predict whether or not a flight will be cancelled due to weather.

## Input Data Sets
* The US Bureau of Transport Statistics provides departure and arrival statistics (scheduled departure time, actual departure time, scheduled elapsed time, departure delay, wheels-off time and taxi-out time) by airport and airline; airborne time, cancellation and diversion by airport and airline with date-time and flight tagging are also provided.
* The weather data is taken on daily average as well as hourly basis from the nearest possible area from the airport from Local Climatological Data from NOAA. The feature set included temperature, precipitation, snow attribute, snow depth, etc.)

## Structure of this repo

```
.
├── Central Park NYC 2015 weather data.csv [NOAA weather data input]
├── flights_data.csv [US Bureau of Transport Statistics data input]
├── randomforest_delay.py	 [Goal 1 - modeled with random forest python script]
├── naivebayes_delay.py	 [Goal 1 - modeled with naive bayes python script]
├── linreg.py	 [Goal 2 - modeled with regression python script]
├── randomforest_cancel.py	 [Goal 3 - modeled with random forest python script]
├── naivebayes_cancel.py	 [Goal 3 - modeled with naive bayes python script]
   
```
## Steps I took
* In preparing for this study, a literature search was completed.
* Decided project scope: Focusing on flight delays in the 3 airports from Greater New York area (JFK, NWK, LGA) for the month of Jan to March which results in around ~60k instances. Used Central Park weather data. Joined data on date-time features.
* Removed non-contextual and derived variables - zeroed in on 10 features for my modeling purpose. The list of attributes I used are: Precipitation, Temperature Min, Snow, Wind, Schedule_Departure, Day of week, Flight Distance, Flight Number, Air Time, and Weather Delay
* Handled missing features in various columns by replacing them with averages or medians, or dropping them ( ~ 1% of total instances) when the replacing strategy did not make sense.
* Used MySQL to clean and store data set. 
* Randomly split my data (~60k instances) in training and testing sets. 67% was given to training and 33% for testing to evaluate the models.
* Had to ‘down-sample’ data in order to achieve better precision and recall. Thus, my ‘down- sampled’ data set was 50% non cancellations/non delays and 50% cancellations/delays.
* Ran Naive Bayes and Random Forest models for Goals 1 and 3. 
* Ran Multiple Linear Regression model for Goal 2.

## Confusion Matrices and Graphs
### Goal 1 
### Goal 2
### Goal 3

## Conclusion
### Results for Goal 1 
Based on flight information (flight, airline, time, origin, destination etc.) and weather features (temp, humidity, rain, precipitation, snow, snow depth, wind speed etc.), I build a model which will predict if the flight is going to be delayed (more than 15 mins) or not. For this I used naive bayes and random forest. 
The results are shown in the table below:

| Naive Bayes              | Random Forest            | 
| ------------------------ |:------------------------:| 
| Training Accuracy : 70.1 | Training Accuracy : 76.8 |
| Test Accuracy : 71.4     | Test Accuracy : 76.3     |  
| Test Recall : 80.38      | Test Recall : 73.5       |
| Test Precision : 53.1    | Test Precision : 79.3    |

Since my test accuracy, recall, and precision for random forest were significantly higher than 50%, my algorithm fared pretty well. Naive Bayes was used as a benchmark to compare my random forest to.

### Results for Goal 2
### Results for Goal 3
