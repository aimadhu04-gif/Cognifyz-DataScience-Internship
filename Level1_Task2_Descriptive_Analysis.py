"""
Cognifyz Technologies - Data Science Internship
Level 1 - Task 2: Descriptive Analysis
"""

import pandas as pd

df = pd.read_csv("Dataset_cleaned.csv")

# -----------------------------
# 1. Basic statistical measures for numerical columns
# -----------------------------
print("=" * 60)
print("1. Statistical summary (numerical columns)")
print("=" * 60)
numeric_cols = ["Average Cost for two", "Price range", "Aggregate rating", "Votes"]
print(df[numeric_cols].describe())

# -----------------------------
# 2. Distribution of categorical variables
# -----------------------------
print("\n" + "=" * 60)
print("2. Country Code - value counts (top 10)")
print("=" * 60)
print(df["Country Code"].value_counts().head(10))

print("\n" + "=" * 60)
print("City - value counts (top 10)")
print("=" * 60)
print(df["City"].value_counts().head(10))

print("\n" + "=" * 60)
print("Cuisines - value counts (top 10)")
print("=" * 60)
print(df["Cuisines"].value_counts().head(10))

# -----------------------------
# 3. Top cuisines and cities with highest number of restaurants
# -----------------------------
print("\n" + "=" * 60)
print("3. Top 5 Cuisines by restaurant count")
print("=" * 60)
top_cuisines = df["Cuisines"].value_counts().head(5)
print(top_cuisines)

print("\n" + "=" * 60)
print("Top 5 Cities by restaurant count")
print("=" * 60)
top_cities = df["City"].value_counts().head(5)
print(top_cities)
