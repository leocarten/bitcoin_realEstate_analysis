# A function to see the circulation of Bitcoin as time progresses
def getTotalCirculation():
    initial_year = 2009
    reward_amount = 50
    total_bitcoin_in_circulation = 0
    for i in range(1, 200):
        if i % 4 == 0:
            total_bitcoin_in_circulation += reward_amount * 210000
            reward_amount = reward_amount / 2
            initial_year += 4
            print(f"In year {initial_year}, there will be {total_bitcoin_in_circulation:.3f} Bitcoin in circulation.")
getTotalCirculation()

# Below I talk about log regression ...

# Important note: The 'Close' column in the CSV is the Closing price for Bitcoin that day...
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import csv

# Define a function to predict prices for new dates based on fitted curve
def predict_price_for_new_date(new_date):
    x_value = len(df) + 1 + (new_date - df['Date'].iloc[-1]).days  # Extrapolate based on the time difference
    return np.exp(func1(x_value, popt[0], popt[1]))

# Load the data from an external CSV file
df = pd.read_csv('predicted.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Define the fitting function
def func1(x, point1, point2):
    return point1 * np.log(x) + point2

# Create x and y data for fitting
xData = np.array([x + 1 for x in range(len(df))])
yData = np.log(df['Close'])

# Perform curve fitting
optimal_parameters, pcov = curve_fit(func1, xData, yData, p0=(3.0, -10))

# Plot the data and the fitted line
fitted_y_data = func1(xData, optimal_parameters[0], optimal_parameters[1])
plt.style.use('dark_background')

# Plot the real data from the CSV
plt.semilogy(df['Date'], df['Close'], label='Real Data')

# Plot the fitted curve 
plt.plot(df['Date'], np.exp(fitted_y_data), label='Log Regression', color='red')

# Use a loop to create the 'rainbow' effect to encapsulate majority of the real data
for i in range(-2,4):
    plt.fill_between(df['Date'], np.exp(fitted_y_data+(i/2 -.5)), np.exp(fitted_y_data+(i/2)), alpha=0.3)

# Show the graph [Yay!]
plt.legend()
plt.show()


# below is other code I used to help extrapolate data
'''
current_date = pd.to_datetime('2023-11-30')

end_date = pd.to_datetime('2030-06-15')

huge_array=[]
while current_date <= end_date:
    new_array=[]
    predicted_price = predict_price_for_new_date(current_date) #generate the new price
    new_array.append((current_date.strftime('%Y-%m-%d')))
    new_array.append("-")
    new_array.append("-")
    new_array.append("-")
    new_array.append(predicted_price*1.52)
    new_array.append("-")
    new_array.append("-")
    huge_array.append(new_array)

    current_date += pd.DateOffset(days=1)

with open("predicted.csv", 'a') as fd: # open the new CSV 
    writer = csv.writer(fd)
    for i in huge_array:
        writer.writerow(i) # write all of the data from the 'huge_array'
    fd.close()
'''
