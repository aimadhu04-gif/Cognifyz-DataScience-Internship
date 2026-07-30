"""
Cognifyz Technologies - Data Science Internship
Level 2 - Task 1: Table Booking and Online Delivery
"""

import pandas as pd

df = pd.read_csv("Dataset_cleaned.csv")
# Note: 'Has Table booking' / 'Has Online delivery' are already 1/0 from Level 1 Task 1 cleaning

# -----------------------------
# 1. Percentage of restaurants offering table booking / online delivery
# -----------------------------
table_booking_pct = df["Has Table booking"].mean() * 100
online_delivery_pct = df["Has Online delivery"].mean() * 100

print("=" * 60)
print("1. Table booking & online delivery availability")
print("=" * 60)
print(f"Restaurants offering table booking: {table_booking_pct:.2f}%")
print(f"Restaurants offering online delivery: {online_delivery_pct:.2f}%")

# -----------------------------
# 2. Average rating comparison: table booking vs no table booking
# -----------------------------
print("\n" + "=" * 60)
print("2. Average rating: table booking vs no table booking")
print("=" * 60)
avg_rating_booking = df.groupby("Has Table booking")["Aggregate rating"].mean()
print(avg_rating_booking.rename({0: "No Table Booking", 1: "Has Table Booking"}))

# -----------------------------
# 3. Online delivery availability across price ranges
# -----------------------------
print("\n" + "=" * 60)
print("3. Online delivery % by price range")
print("=" * 60)
delivery_by_price = df.groupby("Price range")["Has Online delivery"].mean() * 100
print(delivery_by_price)
