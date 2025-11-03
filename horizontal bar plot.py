import matplotlib.pyplot as plt

languages = ['Python', 'Java', 'C++', 'C', 'JavaScript']
popularity = [90, 80, 70, 60, 85]

plt.barh(languages, popularity,)
plt.title("Programming Language Popularity (Horizontal)")
plt.xlabel("Popularity (%)")
plt.ylabel("Language")
plt.show()
