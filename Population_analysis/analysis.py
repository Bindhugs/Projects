import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\bindhu\OneDrive\Projects\Population_analysis\population.csv')
print(df)

# Total population
total_population = df['Value'].sum()
print(f'Total Population of the world: {total_population}')

# Average population
avg_population = df['Value'].mean()
print(f'Average population of the world: {avg_population}')

#Highest population and Lowest population
highest_population = df['Value'].max()
lowest_population = df["Value"].min()
print(f'Highest population of the world: {highest_population} \n Lowest population of the world: {lowest_population}')

# Highest and Lowest populated countries
highest_populated_country = df.loc[df['Value'].idxmax(), 'Country Name']
lowest_populated_country = df.loc[df['Value'].idxmin(), 'Country Name']
print(f'Highest populated country : {highest_populated_country} \nLowest populated country : {lowest_populated_country}')

# Population growth over time
country = 'India'
data = df[df['Country Name']==country]
plt.plot(data['Year'],data['Value'])
plt.title(f'Population Growth of {country} over time')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()
