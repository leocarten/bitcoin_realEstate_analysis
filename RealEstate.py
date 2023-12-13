# Below i create a linear regression model
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read the CSV file
df = pd.read_csv('real_estate.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Convert 'Date' to numeric values (UNIX timestamp)
df['Date'] = pd.to_numeric(df['Date'])

# Extract x and y values
x = df['Date']
y = df['Price']

# Perform linear regression
slope, intercept, r, p, std_err = linregress(x, y)
# Show the equation
print(f"The equation y={slope}x+{intercept} has an r^2 value of {r}.")

# Plot the scatter plot
plt.scatter(x, y, label='Data')

# Plot the regression line
plt.plot(x, intercept + slope * x, 'r', label='Linear Regression')

# Show the graph
plt.legend()
plt.show()

# below i show how to 'add zones' to the linear regression model
regression_line = intercept + slope * x
margin = 15000
upper_mean_bound = regression_line + margin
lower_mean_bound = regression_line - margin
margin = 15000*2
upper_mean_plus_one_bound = regression_line + margin
lower_mean_minus_one_bound = regression_line - margin
margin = 15000*3
upper_mean_plus_two_bound = regression_line + margin
lower_mean_minus_two_bound = regression_line - margin
plt.scatter(x, y, label='Data')
# Plot the regression line
plt.plot(x, regression_line, 'r', label='Linear Regression')
# Shade the area between the upper and lower bounds
plt.fill_between(x, lower_mean_bound, upper_mean_bound, color='red', alpha=0.7, label='Average Zone')
plt.fill_between(x, lower_mean_minus_one_bound, upper_mean_plus_one_bound, color='blue', alpha=0.5, label='+ or - 1 Zone')
plt.fill_between(x, lower_mean_minus_two_bound, upper_mean_plus_two_bound, color='yellow', alpha=0.3, label='+ or minus - 2 Zone')  


# below i show how to extrapolate the data and write back to the CSV
import csv 
import datetime
huge_array = []
def writeToCSVFile():
    year = 2023
    for i in range(251, 500, 4):
        if year > 2052:
            break
        else:
            new_array = []
            price = 1964 * i - 53974
            date_time = datetime.datetime(year, 7, 26, 21, 20)
            new_array.append(date_time.strftime('%Y-%m-%d'))
            print(f"In year {date_time.strftime('%Y-%m-%d')}, the price will be {price}")
            new_array.append(price)
            huge_array.append(new_array)
            year += 1
writeToCSVFile()

with open("real_estate.csv", 'a') as fd:
    writer = csv.writer(fd)
    for i in huge_array:
        writer.writerow(i)
    fd.close() 

