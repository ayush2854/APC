import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Ayush', 'Sarthak', 'Neha', 'Rohan'],
    'Age': [21, 22, 20, 23],
    'Marks': [88, 92, 79, 85]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 1. head() - Show first few rows
print("\n1. head():\n", df.head(2))

# 2. tail() - Show last few rows
print("\n2. tail():\n", df.tail(2))

# 3. info() - Display structure of DataFrame
print("\n3. info():")
df.info()

# 4. describe() - Summary statistics
print("\n4. describe():\n", df.describe())

# 5. sort_values() - Sort rows by column
print("\n5. sort_values() by Marks:\n", df.sort_values(by='Marks'))

# 6. loc[] - Select rows/columns by labels
print("\n6. loc[] Name & Age Columns:\n", df.loc[:, ['Name', 'Age']])

# 7. iloc[] - Select rows/columns by index positions
print("\n7. iloc[] First two rows:\n", df.iloc[0:2])

# 8. groupby() - Group data
group_data = df.groupby('Age').mean()
print("\n8. groupby() Age Mean:\n", group_data)

# 9. drop() - Drop a column
df_drop = df.drop('Marks', axis=1)
print("\n9. drop() Marks Column:\n", df_drop)

# 10. fillna() - Fill missing values
df2 = df.copy()
df2.loc[2, 'Marks'] = None  # Insert NaN value
print("\nDataFrame with NaN:\n", df2)
print("\n10. fillna() Replacing NaN with 0:\n", df2.fillna(0))
