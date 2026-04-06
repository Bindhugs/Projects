import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\bindhu\OneDrive\Projects\Sales_Data_Analysis\dataset.csv')

print(data)

data['date'] = pd.to_datetime(data['date']) # Converts the date column to datetime format

data['revenue'] = data[' quantity'] * data[' price'] # Creates a new column 'revenue' by multiplying quantity and price



total_revenue = data['revenue'].sum()
print("\n Total Revenue: ",total_revenue)

product_sales = data.groupby(' product')[' quantity'].sum()
print("\n Product Sales: \n",product_sales)

data['month'] = data['date'].dt.month
monthly_revenue = data.groupby('month')['revenue'].sum()
print("\n Monthly Revenue: \n",monthly_revenue)

avg_revenue = np.mean(data['revenue'])
print("\n Average Revenue: ",avg_revenue)

print("Max Revenue: ",np.max(data['revenue']))

print("Min Revenue: ",np.min(data['revenue']))

plt.figure()
product_sales.plot(kind='bar')
plt.title("Product Sales Analysis")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation = 0)
plt.show()

plt.figure()
monthly_revenue.plot(kind='line')
plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()


