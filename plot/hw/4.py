import matplotlib.pyplot as plt
countries = ['US', 'South Korea', 'Australia', 'Germany', 'India', 'UK']
share = [198, 92, 31, 165, 277, 246]
Explode = [0.1, 0, 0, 0, 0, 0]
plt.pie(share, explode = Explode, autopct = '%1.2f%%', labels = countries, startangle = 290, shadow = True)
plt.title('Population density index')
plt.show()