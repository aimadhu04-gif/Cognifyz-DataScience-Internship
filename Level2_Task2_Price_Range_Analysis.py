"""
Cognifyz Technologies - Data Science Internship
Level 2 - Task 2: Price Range Analysis
"""

import pandas as pd

df = pd.read_csv("Dataset_cleaned.csv")

# -----------------------------
# 1. Most common price range
# -----------------------------
print("=" * 60)
print("1. Price range distribution")
print("=" * 60)
price_counts = df["Price range"].value_counts().sort_index()
print(price_counts)
most_common = df["Price range"].mode()[0]
print(f"\nMost common price range: {most_common}")

# -----------------------------
# 2. Average rating for each price range
# -----------------------------
print("\n" + "=" * 60)
print("2. Average rating by price range")
print("=" * 60)
avg_rating_by_price = df.groupby("Price range")["Aggregate rating"].mean().sort_index()
print(avg_rating_by_price)

# -----------------------------
# 3. Rating color representing highest average rating
# -----------------------------
print("\n" + "=" * 60)
print("3. Rating color with highest average rating")
print("=" * 60)
color_avg = df.groupby("Rating color")["Aggregate rating"].mean().sort_values(ascending=False)
print(color_avg)
print(f"\nColor representing the highest average rating: {color_avg.idxmax()}")
