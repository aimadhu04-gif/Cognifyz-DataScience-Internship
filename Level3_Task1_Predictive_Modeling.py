"""
Cognifyz Technologies - Data Science Internship
Level 3 - Task 1: Predictive Modeling
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("Dataset_features.csv")

# -----------------------------
# Prepare features and target
# -----------------------------
features = [
    "Average Cost for two", "Price range", "Votes",
    "Has_Table_Booking", "Has_Online_Delivery",
    "Restaurant Name Length", "Address Length"
]
target = "Aggregate rating"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# Train & evaluate multiple models
# -----------------------------
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42, max_depth=8),
    "Random Forest": RandomForestRegressor(random_state=42, n_estimators=100, max_depth=10),
}

print("=" * 60)
print("Model performance comparison")
print("=" * 60)
results = []
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    rmse = mean_squared_error(y_test, preds) ** 0.5
    r2 = r2_score(y_test, preds)
    results.append((name, rmse, r2))
    print(f"{name:20s} | RMSE: {rmse:.4f} | R2: {r2:.4f}")

best_model = max(results, key=lambda x: x[2])
print(f"\nBest performing model: {best_model[0]} (R2: {best_model[2]:.4f})")
