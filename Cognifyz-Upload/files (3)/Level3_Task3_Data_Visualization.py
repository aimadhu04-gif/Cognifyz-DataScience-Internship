"""
Cognifyz Technologies - Data Science Internship
Level 3 - Task 3: Data Visualization
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset_features.csv")

# -----------------------------
# 1. Distribution of ratings (histogram + bar plot of rating text)
# -----------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].hist(df["Aggregate rating"], bins=20, edgecolor="black", color="steelblue")
axes[0].set_title("Distribution of Aggregate Rating")
axes[0].set_xlabel("Aggregate Rating")
axes[0].set_ylabel("Frequency")

rating_text_counts = df["Rating text"].value_counts()
axes[1].bar(rating_text_counts.index, rating_text_counts.values, color="darkorange")
axes[1].set_title("Restaurant Count by Rating Category")
axes[1].set_xlabel("Rating Text")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig("rating_distribution_charts.png")
print("Saved: rating_distribution_charts.png")

# -----------------------------
# 2. Compare average ratings across top cuisines and cities
# -----------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

top_cuisines = df.groupby("Cuisines").filter(lambda x: len(x) >= 20).groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False).head(10)
axes[0].barh(top_cuisines.index, top_cuisines.values, color="seagreen")
axes[0].set_title("Top 10 Cuisines by Avg Rating")
axes[0].set_xlabel("Average Rating")
axes[0].invert_yaxis()

top_cities = df.groupby("City").filter(lambda x: len(x) >= 20).groupby("City")["Aggregate rating"].mean().sort_values(ascending=False).head(10)
axes[1].barh(top_cities.index, top_cities.values, color="mediumpurple")
axes[1].set_title("Top 10 Cities by Avg Rating")
axes[1].set_xlabel("Average Rating")
axes[1].invert_yaxis()

plt.tight_layout()
plt.savefig("cuisine_city_comparison.png")
print("Saved: cuisine_city_comparison.png")

# -----------------------------
# 3. Relationship between features and target variable
# -----------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].scatter(df["Votes"], df["Aggregate rating"], alpha=0.3, s=8, color="crimson")
axes[0].set_title("Votes vs Aggregate Rating")
axes[0].set_xlabel("Votes")
axes[0].set_ylabel("Aggregate Rating")
axes[0].set_xscale("log")

price_avg = df.groupby("Price range")["Aggregate rating"].mean()
axes[1].bar(price_avg.index.astype(str), price_avg.values, color="teal")
axes[1].set_title("Price Range vs Avg Rating")
axes[1].set_xlabel("Price Range")
axes[1].set_ylabel("Average Rating")

plt.tight_layout()
plt.savefig("feature_vs_rating.png")
print("Saved: feature_vs_rating.png")
