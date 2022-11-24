import matplotlib.pyplot as plt
countries = ['Germany', 'Other', 'Italy', 'Ireland', 'Iceland', 'Greece']
share = [102, 210, 303, 177, 107, 102]
Explode = [0.1, 0, 0, 0, 0, 0]
plt.pie(share, explode = Explode, autopct = '%1.2f%%', labels = countries, startangle = 290, shadow = True)
plt.title('Population density index')
plt.show()