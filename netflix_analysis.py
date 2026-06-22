import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("netflix_titles.csv")


# Dataset Information

print("=" * 50)
print("NETFLIX DATA ANALYSIS")
print("=" * 50)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())


# Movies vs TV Shows

print("\nMovies vs TV Shows:")
print(df['type'].value_counts())

plt.figure(figsize=(6, 4))

df['type'].value_counts().plot(kind='bar')

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("movie_vs_tvshow.png")
plt.show()
plt.close()


# Top 10 Countries

print("\nTop 10 Countries:")
print(df['country'].dropna().value_counts().head(10))

plt.figure(figsize=(8, 5))

df['country'].dropna().value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("top_countries.png")
plt.show()
plt.close()


# Content Ratings

print("\nMost Common Ratings:")
print(df['rating'].dropna().value_counts().head(10))

plt.figure(figsize=(8, 5))

df['rating'].dropna().value_counts().head(10).plot(kind='bar')

plt.title("Most Common Netflix Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("content_ratings.png")
plt.show()
plt.close()


# Release Year Trend

print("\nContent Released By Year:")
print(df['release_year'].value_counts().head(10))

plt.figure(figsize=(10, 5))

df['release_year'].value_counts().sort_index().plot(kind='line')

plt.title("Netflix Content Release Trend")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("release_year_trend.png")
plt.show()
plt.close()


# Final Message

print("\nAnalysis Completed Successfully!")
print("Charts saved as:")
print("- movie_vs_tvshow.png")
print("- top_countries.png")
print("- content_ratings.png")
print("- release_year_trend.png")
