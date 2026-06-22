import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print(df.head())
print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nMovies vs TV Shows")

print(df['type'].value_counts())

print("\nTop Countries")

print(df['country'].value_counts().head(10))

print("\nRatings")

print(df['rating'].value_counts())

import matplotlib.pyplot as plt

df['type'].value_counts().plot(kind='bar')

plt.title("Movies vs TV Shows on Netflix")

plt.show()

print("\nContent Released By Year")

print(df['release_year'].value_counts().head(10))
