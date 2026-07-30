"""
Cognifyz Technologies - Data Science Internship
Level 3 - Task 2: Customer Preference Analysis
"""

import pandas as pd

df = pd.read_csv("Dataset_features.csv")

# -----------------------------
# 1. Relationship between cuisine type and rating
# -----------------------------
print("=" * 60)
print("1. Average rating by cuisine (top 15 cuisines, min 20 restaurants)")
print("=" * 60)
cuisine_stats = df.groupby("Cuisines").filter(lambda x: len(x) >= 20)
cuisine_avg_rating = cuisine_stats.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False)
print(cuisine_avg_rating.head(15))

# -----------------------------
# 2. Most popular cuisines by number of votes
# -----------------------------
print("\n" + "=" * 60)
print("2. Most popular cuisines by total votes")
print("=" * 60)
cuisine_votes = df.groupby("Cuisines")["Votes"].sum().sort_values(ascending=False)
print(cuisine_votes.head(10))

# -----------------------------
# 3. Cuisines that tend to receive higher ratings
# -----------------------------
print("\n" + "=" * 60)
print("3. Top rated cuisines (min 20 restaurants) - higher rating tendency")
print("=" * 60)
print(cuisine_avg_rating.head(10))

print(
    "\nObservation: cuisines like these consistently score above the overall "
    "dataset average rating (~2.67), suggesting these cuisine categories "
    "tend to receive higher customer ratings."
)
