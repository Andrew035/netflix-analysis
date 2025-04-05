import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv("netflix_titles.csv")

# Preview
print("\n📋 First 5 rows:\n", df.head())
print("\n🧪 Columns:\n", df.columns)

# Drop rows with missing "type" or "release_year"
df = df.dropna(subset=["type", "release_year"])

# Fill null values in 'country' and 'rating'
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")

# Count TV Shows vs Movies
type_counts = df["type"].value_counts()
print("\n📊 Content Type Breakdown:\n", type_counts)

# Plot
type_counts.plot(kind="bar", title="Netflix Content Type", color=["red", "blue"])
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# Group by year
content_by_year = df.groupby("release_year")["title"].count()

# Plot
plt.figure(figsize=(10, 6))
content_by_year.plot(kind="line", title="Netflix Content Added Over Time")
plt.xlabel("Relase Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.show()

# Explode the country column (some entries have multiple countries)
df["country"] = df["country"].str.split(", ")
countries_exploded = df.explode("country")

# Top 10 countries
top_countries = countries_exploded["country"].value_counts().head(10)

# Plot
top_countries.plot(
    kind="barh", title="Top 10 Content-Producing Countries", color="green"
)
plt.xlabel("Number of Titles")
plt.tight_layout()
plt.show()

df["listed_in"] = df["listed_in"].str.split(", ")
genres_exploded = df.explode("listed_in")

top_genres = genres_exploded["listed_in"].value_counts().head(10)

# Plot
top_genres.plot(kind="bar", title="Top 10 Genres", color="purple")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# Export cleaned data
df.to_csv("netflix_cleaned.csv", index=False)
