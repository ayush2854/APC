import matplotlib.pyplot as plt

ages = [18, 22, 25, 30, 35, 40, 45, 50, 55, 60]

bins = [10, 20, 30, 40, 50, 60, 70]

plt.hist(ages, bins, color='skyblue', edgecolor='black')

plt.title("Simple Age Distribution Histogram")
plt.xlabel("Age Range")
plt.ylabel("Number of People")
plt.show()
