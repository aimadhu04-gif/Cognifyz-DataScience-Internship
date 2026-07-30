# Cognifyz Technologies — Data Science Internship

Internship program by **Cognifyz Technologies** (Where Data Meets Intelligence).
This repo contains all completed tasks across **Level 1, Level 2, and Level 3** using a
restaurant dataset (9,551 restaurants, 21 columns) covering ratings, cuisines, location,
price range, table booking, and online delivery.

## 📁 Repo Structure
```
├── Level1_Task1_Data_Exploration_Preprocessing.py
├── Level1_Task2_Descriptive_Analysis.py
├── Level1_Task3_Geospatial_Analysis.py
├── Level2_Task1_Table_Booking_Online_Delivery.py
├── Level2_Task2_Price_Range_Analysis.py
├── Level2_Task3_Feature_Engineering.py
├── Level3_Task1_Predictive_Modeling.py
├── Level3_Task2_Customer_Preference_Analysis.py
├── Level3_Task3_Data_Visualization.py
├── Dataset_.csv                # original dataset
├── Dataset_cleaned.csv         # after Level 1 cleaning
├── Dataset_features.csv        # after Level 2 feature engineering
└── *.png                       # generated charts
```

## 🔹 Level 1 — Exploration & Analysis
**Task 1: Data Exploration & Preprocessing**
- Dataset: 9,551 rows × 21 columns
- Missing values only in `Cuisines` (9 rows) → filled with "Not Available"
- Yes/No columns converted to 1/0
- Target (`Aggregate rating`) is imbalanced — 22.49% restaurants are "Not rated" (0.0)

**Task 2: Descriptive Analysis**
- Top cities: New Delhi, Gurgaon, Noida, Faridabad
- Top cuisines: North Indian, North Indian+Chinese, Chinese, Fast Food

**Task 3: Geospatial Analysis**
- Mapped restaurant locations by latitude/longitude, colored by rating
- Raw coordinates show weak correlation with rating; city-level averages (London, Bangalore, Dubai, Chennai) show stronger patterns

## 🔹 Level 2 — Deeper Analysis & Feature Engineering
**Task 1: Table Booking & Online Delivery**
- 12.12% offer table booking, 25.66% offer online delivery
- Table booking restaurants average 3.44 rating vs 2.56 without
- Online delivery highest in mid-price range (Price range 2: 41.3%)

**Task 2: Price Range Analysis**
- Most common price range: 1 (budget)
- Higher price range → higher average rating
- "Dark Green" rating color has the highest average rating (4.66)

**Task 3: Feature Engineering**
- Added `Restaurant Name Length`, `Address Length`
- Encoded `Has_Table_Booking`, `Has_Online_Delivery` as binary features

## 🔹 Level 3 — Modeling & Visualization
**Task 1: Predictive Modeling**
- Compared Linear Regression (R²: 0.26), Decision Tree (R²: 0.95), Random Forest (R²: 0.95)
- **Random Forest** performed best for predicting `Aggregate rating`

**Task 2: Customer Preference Analysis**
- Highest-rated cuisines: American, Italian, Mexican
- Most popular cuisines by votes: North Indian, North Indian+Mughlai

**Task 3: Data Visualization**
- Rating distribution histograms & bar charts
- Cuisine/city rating comparisons
- Votes vs rating and price range vs rating plots

## 🛠 Tools Used
Python, Pandas, Matplotlib, Scikit-learn

## 📌 About Cognifyz Technologies
Cognifyz Technologies is a technology company specializing in data science, AI, and ML
solutions, offering internship programs to build practical, real-world data skills.

---
**#cognifyz #cognifyzTech #cognifyzTechnologies**
