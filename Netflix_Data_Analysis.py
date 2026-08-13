import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Netflix dataset
df = pd.read_csv("netflix_titles.csv")

# Display first 5 rows
print(df.head())

# Display dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Fill missing values in important text columns
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDataset Shape After Cleaning:")
print(df.shape)

# -----------------------------------------
# 8. Project Summary
# -----------------------------------------

# Recreate genre data for summary
genre_data = df["listed_in"].str.split(",").explode().str.strip()

# Recreate country data for summary
country_data = df["country"].str.split(",").explode().str.strip()

print("\n" + "=" * 50)
print("NETFLIX DATA ANALYSIS - PROJECT SUMMARY")
print("=" * 50)

print("\nDataset:")
print(f"Total Titles: {len(df)}")
print(f"Total Columns: {len(df.columns)}")

print("\nContent Type:")
print(f"Movies: {len(df[df['type'] == 'Movie'])}")
print(f"TV Shows: {len(df[df['type'] == 'TV Show'])}")

print("\nTop 5 Content Ratings:")
print(df["rating"].value_counts().head(5))

print("\nTop 5 Genres:")
print(genre_data.value_counts().head(5))

print("\nTop 5 Countries:")
print(country_data.value_counts().head(5))

print("\nAnalysis completed successfully.")
