"""
Cognifyz Technologies - Data Science Internship
Level 2 - Task 3: Feature Engineering
"""

import pandas as pd

df = pd.read_csv("Dataset_cleaned.csv")

# -----------------------------
# 1. Extract additional features from existing columns
# -----------------------------
df["Restaurant Name Length"] = df["Restaurant Name"].astype(str).apply(len)
df["Address Length"] = df["Address"].astype(str).apply(len)

print("=" * 60)
print("1. New length-based features (sample)")
print("=" * 60)
print(df[["Restaurant Name", "Restaurant Name Length", "Address Length"]].head())

# -----------------------------
# 2. Encode categorical variables into new boolean-style features
#    (Has Table booking / Has Online delivery already 0/1 from Level 1 cleaning,
#    rename here to match the task's requested feature names explicitly)
# -----------------------------
df["Has_Table_Booking"] = df["Has Table booking"]
df["Has_Online_Delivery"] = df["Has Online delivery"]

print("\n" + "=" * 60)
print("2. Encoded feature columns (sample)")
print("=" * 60)
print(df[["Has_Table_Booking", "Has_Online_Delivery"]].value_counts())

# Save the feature-engineered dataset for use in Level 3
df.to_csv("Dataset_features.csv", index=False)
print("\nSaved feature-engineered dataset: Dataset_features.csv")
