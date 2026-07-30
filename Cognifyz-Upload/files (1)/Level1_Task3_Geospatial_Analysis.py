"""
Cognifyz Technologies - Data Science Internship
Level 1 - Task 3: Geospatial Analysis
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset_cleaned.csv")

# -----------------------------
# 1. Visualize restaurant locations (lat/long) colored by rating
# -----------------------------
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    df["Longitude"], df["Latitude"],
    c=df["Aggregate rating"], cmap="RdYlGn", s=8, alpha=0.6
)
plt.colorbar(scatter, label="Aggregate Rating")
plt.title("Restaurant Locations (colored by Aggregate Rating)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.savefig("restaurant_locations_map.png")
print("Saved plot: restaurant_locations_map.png")

# -----------------------------
# 2. Distribution of restaurants across cities/countries
# -----------------------------
print("\n" + "=" * 60)
print("Restaurant count by top 10 cities")
print("=" * 60)
print(df["City"].value_counts().head(10))

print("\n" + "=" * 60)
print("Restaurant count by top 10 country codes")
print("=" * 60)
print(df["Country Code"].value_counts().head(10))

# -----------------------------
# 3. Correlation between location (lat/long) and rating
# -----------------------------
print("\n" + "=" * 60)
print("Correlation: Latitude/Longitude vs Aggregate Rating")
print("=" * 60)
corr = df[["Latitude", "Longitude", "Aggregate rating"]].corr()["Aggregate rating"]
print(corr)

print(
    "\nNote: Latitude/Longitude are raw coordinates, so a linear correlation "
    "here is weak/not meaningful on its own — location matters more at the "
    "City/Country level (see grouped averages below) than as raw coordinates."
)

print("\n" + "=" * 60)
print("Average rating by top 10 cities (min 20 restaurants)")
print("=" * 60)
city_avg = df.groupby("City").filter(lambda x: len(x) >= 20).groupby("City")["Aggregate rating"].mean().sort_values(ascending=False)
print(city_avg.head(10))
