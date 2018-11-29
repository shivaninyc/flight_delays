#Using Linear Regression, predict how much the flight will be delayed, based on data inputs.

#import libraries to run linear regression of data inputs
import sklearn as sk
import pymysql  
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
clf = linear_model.LinearRegression()

poly = PolynomialFeatures(degree=1)

#connect to mysql database and retrieve cleaned data set (linregdata8) for running model
conn = pymysql.connect(host='localhost',  
                       port=3306,  
                       user='root',  
                       passwd='password',  
                       db='flight_delay',  
                       charset='utf8')  
cur = conn.cursor()  
sql = "SELECT * FROM linregdata8"  
dbquery = cur.execute(sql)  
rows = cur.fetchall()
rowlists = [list(x) for x in rows]
y_var = [item[0] for item in rowlists]
x1_var = [item[1] for item in rowlists]
x2_var = [item[2] for item in rowlists]
x3_var =  [item[3] for item in rowlists]
x_vars = [item[1:8] for item in rowlists]

x = poly.fit_transform(x_vars)


print("Y:",y_var);
print("X1:",x1_var);
print("All rows: ",rowlists)
print ("x_vars:",x_vars);

clf.fit(x,
       y_var)

#print coefficients of regression test and results
print('Coefficients: \n', clf.coef_)
y_pred = clf.predict(x)
print("Mean squared error: %.2f",
     mean_squared_error(y_var, y_pred))
print('Variance score: %.2f' % r2_score(y_var, y_pred))


# Plot outputs 
plt.scatter(x1_var, y_var,  color='black')
plt.plot(x1_var, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

# Plot outputs
plt.scatter(x2_var, y_var,  color='black')
plt.plot(x2_var, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

# Plot outputs
plt.scatter(x3_var, y_var,  color='black')
plt.plot(x3_var, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

# close connection to the database  
cur.close()  
conn.close()
