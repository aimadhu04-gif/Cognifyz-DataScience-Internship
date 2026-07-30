"""
Cognifyz Technologies - Data Science Internship
Level 1 - Task 1: Data Exploration and Preprocessing
"""

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_csv("Dataset_.csv")

print("=" * 60)
print("1. Dataset shape (rows, columns)")
print("=" * 60)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# -----------------------------
# 2. Missing values
# -----------------------------
print("\n" + "=" * 60)
print("2. Missing values per column")
print("=" * 60)
missing = df.isnull().sum()
print(missing[missing > 0] if missing.sum() > 0 else "No missing values found.")

# Handle missing values
# 'Cuisines' has a few missing entries -> fill with 'Not Available'
if df["Cuisines"].isnull().sum() > 0:
    df["Cuisines"] = df["Cuisines"].fillna("Not Available")
    print("\nFilled missing 'Cuisines' values with 'Not Available'.")

# -----------------------------
# 3. Data type conversion
# -----------------------------
print("\n" + "=" * 60)
print("3. Data types (before conversion)")
print("=" * 60)
print(df.dtypes)

# Convert Yes/No columns to boolean-like (0/1) for easier analysis
binary_cols = ["Has Table booking", "Has Online delivery", "Is delivering now", "Switch to order menu"]
for col in binary_cols:
    df[col] = df[col].map({"Yes": 1, "No": 0})

print("\nConverted Yes/No columns to 1/0:", binary_cols)

# -----------------------------
# 4. Target variable distribution & class imbalance
# -----------------------------
print("\n" + "=" * 60)
print("4. Aggregate rating - distribution")
print("=" * 60)
print(df["Aggregate rating"].describe())

print("\nRating text (class) counts:")
print(df["Rating text"].value_counts())

# Restaurants with rating 0.0 (Not rated) are a large imbalanced class
zero_rating_pct = (df["Aggregate rating"] == 0).mean() * 100
print(f"\n% restaurants with Aggregate rating = 0 (Not rated): {zero_rating_pct:.2f}%")

# Plot distribution
plt.figure(figsize=(8, 5))
df["Aggregate rating"].plot(kind="hist", bins=20, edgecolor="black")
plt.title("Distribution of Aggregate Rating")
plt.xlabel("Aggregate Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("aggregate_rating_distribution.png")
print("\nSaved plot: aggregate_rating_distribution.png")

# Save cleaned dataset for use in later tasks
df.to_csv("Dataset_cleaned.csv", index=False)
print("\nSaved cleaned dataset: Dataset_cleaned.csv")
