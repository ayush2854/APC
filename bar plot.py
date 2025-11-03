import matplotlib.pyplot as plt

languages = ['Python', 'Java', 'C++', 'C', 'JavaScript']
popularity = [90, 80, 70, 60, 85]

plt.bar(languages, popularity)
plt.title("Programming Language Popularity")
plt.xlabel("Language")
plt.ylabel("Popularity (%)")
plt.show()
