#Using Random Forest,predict if the flight is going to be cancelled or not, based on data inputs.

#import libraries to run random forest model on data inputs
import sklearn as sk
import pandas as pd
import pymysql  
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=123456)

#connect to mysql database and retrieve cleaned data set (randomforest2) for running model
conn = pymysql.connect(host='localhost',
                       port=3306,  
                       user='root',  
                       passwd='password',  
                       db='flight_delay',  
                       charset='utf8')  
cur = conn.cursor()  
sql = "SELECT * FROM randomforest2"  
dbquery = cur.execute(sql)  
rows = cur.fetchall()
rowlists = [list(x) for x in rows]
y_var = [item[0] for item in rowlists]
x1_var = [item[1] for item in rowlists]
x2_var = [item[2] for item in rowlists]
x3_var =  [item[3] for item in rowlists]
x_vars = [item[1:4] for item in rowlists]

#split into training and testing data sets
X_train, X_test, y_train, y_test = train_test_split(x_vars, y_var, test_size=0.33, random_state=42)

#compute model based on training data sets
rf.fit(X_train, y_train)

#predicted values when model is run on training/testing data sets
predicted_train = rf.predict(X_train)
predicted_test = rf.predict(X_test)

#Accuracy measure
from sklearn.metrics import accuracy_score
accuracy_train = accuracy_score(y_train, predicted_train)
accuracy_test = accuracy_score(y_test, predicted_test)
print(f'Out-of-bag score estimate (train): {rf.oob_score_:.3}')
print(f'Mean accuracy_train score: {accuracy_train:.3}')
print(f'Out-of-bag score estimate (test): {rf.oob_score_:.3}')
print(f'Mean accuracy_test score: {accuracy_test:.3}')

#confusion matrix output to measure recall and precision
cm_train = pd.DataFrame(confusion_matrix(y_train, predicted_train)) 
cm_test = pd.DataFrame(confusion_matrix(y_test, predicted_test)) 
sns.heatmap(cm_test, annot=True)

#close database connection 
cur.close()  
conn.close()

