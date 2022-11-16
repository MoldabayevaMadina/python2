import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('country_wise_latest.csv')

#for i in data.columns:
#    print(data[i].isna().sum())

print(data.info())

#1
print('Number of countries where the deaths rate is above 5000:\n', (data['Deaths'] > 5000).sum())
print('List of countries where the deaths rate is above 5000:\n', data[data['Deaths'] > 5000]['Country/Region'])



#2
k = data.groupby("WHO Region").agg(confirmed_cases = pd.NamedAgg('Confirmed', sum))
print('\nTotal number of confirmed cases in each WHO region:\n', k)


#3
grouped = data.groupby('WHO Region')
print('Data about COVID-19 in each WHO Region:\n', grouped.sum())
who_regions = data['WHO Region'].value_counts()
print('Number of infected countries in each WHO region:\n', who_regions)



#4
print('Data about COVID-19 in Western Pacific:\n', grouped.get_group('Western Pacific'))


#5
print('Countries that have the minimum number of people that suffer from COVID-19\n', data.sort_values('Active').head(5)['Country/Region'])
print('Countries that have the maximum number of people that suffer from COVID-19\n', data.sort_values('Active', ascending = False).head(5)['Country/Region'])

who_reg = list(set(data['WHO Region']))
who_reg.sort()
cases = list(k['confirmed_cases'])
plt.pie(cases, labels = who_reg, shadow = True)
plt.title('Where number of confirmed cases is the highest?')
#plt.legend(title = 'WHO Regions')
plt.show()