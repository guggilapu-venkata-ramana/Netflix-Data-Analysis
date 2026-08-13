import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================================
# NETFLIX DATA ANALYSIS
# =========================================

# Load Netflix dataset
df = pd.read_csv("netflix_titles.csv")

# -----------------------------------------
# 1. Initial Dataset Information
# -----------------------------------------

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# -----------------------------------------
# 2. Data Cleaning
# -----------------------------------------

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# Fill missing text values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDataset Shape After Cleaning:")
print(df.shape)

# =========================================
# 3. Movies vs TV Shows
# =========================================

content_type = df["type"].value_counts()

print("\nMovies vs TV Shows:")
print(content_type)

plt.figure(figsize=(7, 5))
plt.bar(content_type.index, content_type.values)

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.show()

# =========================================
# 4. Netflix Content by Release Year
# =========================================

content_by_year = df["release_year"].value_counts().sort_index()

print("\nContent by Release Year:")
print(content_by_year.tail(10))

plt.figure(figsize=(12, 6))
plt.plot(content_by_year.index, content_by_year.values)

plt.title("Netflix Content by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.show()

# =========================================
# 5. Top 10 Countries
# =========================================

country_data = (
    df["country"]
    .str.split(",")
    .explode()
    .str.strip()
)

top_countries = country_data.value_counts().head(10)

print("\nTop 10 Countries Producing Netflix Content:")
print(top_countries)

plt.figure(figsize=(10, 6))
plt.barh(
    top_countries.index[::-1],
    top_countries.values[::-1]
)

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.tight_layout()
plt.show()

# =========================================
# 6. Netflix Content by Rating
# =========================================

rating_counts = df["rating"].value_counts().head(10)

print("\nTop Netflix Content Ratings:")
print(rating_counts)

plt.figure(figsize=(10, 6))
plt.bar(rating_counts.index, rating_counts.values)

plt.title("Netflix Content by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# =========================================
# 7. Top 10 Netflix Genres
# =========================================

genre_data = (
    df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
)

top_genres = genre_data.value_counts().head(10)

print("\nTop 10 Netflix Genres:")
print(top_genres)

plt.figure(figsize=(10, 6))
plt.barh(
    top_genres.index[::-1],
    top_genres.values[::-1]
)

plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")

plt.tight_layout()
plt.show()

# =========================================
# 8. Movies vs TV Shows by Release Year
# =========================================

type_by_year = (
    df.groupby(["release_year", "type"])
    .size()
    .unstack(fill_value=0)
)

print("\nMovies vs TV Shows by Release Year:")
print(type_by_year.tail(10))

plt.figure(figsize=(12, 6))

if "Movie" in type_by_year.columns:
    plt.plot(
        type_by_year.index,
        type_by_year["Movie"],
        label="Movies"
    )

if "TV Show" in type_by_year.columns:
    plt.plot(
        type_by_year.index,
        type_by_year["TV Show"],
        label="TV Shows"
    )

plt.title("Movies vs TV Shows by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.legend()

plt.tight_layout()
plt.show()

# =========================================
# 9. Movie Duration Analysis
# =========================================

movie_data = df[df["type"] == "Movie"].copy()

movie_data["duration_minutes"] = (
    movie_data["duration"]
    .str.extract(r"(\d+)")
    .astype(float)
)

print("\nMovie Duration Statistics:")
print(movie_data["duration_minutes"].describe())

plt.figure(figsize=(10, 6))

plt.hist(
    movie_data["duration_minutes"].dropna(),
    bins=20
)

plt.title("Distribution of Netflix Movie Durations")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")

plt.tight_layout()
plt.show()

# =========================================
# 10. Project Summary
# =========================================

print("\n" + "=" * 50)
print("NETFLIX DATA ANALYSIS - PROJECT SUMMARY")
print("=" * 50)

print("\nDataset:")
print(f"Total Titles: {len(df)}")
print(f"Total Columns: {len(df.columns)}")

print("\nContent Type:")
print(
    f"Movies: {len(df[df['type'] == 'Movie'])}"
)
print(
    f"TV Shows: {len(df[df['type'] == 'TV Show'])}"
)

print("\nTop 5 Content Ratings:")
print(
    df["rating"]
    .value_counts()
    .head(5)
)

print("\nTop 5 Genres:")
print(
    genre_data
    .value_counts()
    .head(5)
)

print("\nTop 5 Countries:")
print(
    country_data
    .value_counts()
    .head(5)
)

print("\nAverage Movie Duration:")
print(
    round(
        movie_data["duration_minutes"].mean(),
        2
    ),
    "minutes"
)

print("\nAnalysis completed successfully.")
