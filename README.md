# Transaction Analytics Pipeline with Looker Studio Dashboard

## 📸 Screenshots

### Transaction Dashboard
![Dashboard Screenshot](/Users/user/Desktop/atechcoins/screenshots.jpg)

## 📌 Overview

This project simulates transaction events, processes them through a data pipeline, and visualizes insights in a Looker Studio dashboard.

It covers:
- Data generation and storage
- ETL (Extract, Transform, Load) process
- Data visualization for KPIs like transaction volume, success/failure rates, and peak transaction times

---

## Tech Stack
- **python** - Data simulation, ETL scripts
- **Firebase Realtime Database** - Raw data storage 
- **MySQL** – Clean data storage  
- **Looker Studio** – Dashboard visualization  
- **CSV** – Used for final data upload to Looker Studio (due to MySQL connection issue)  

---

## Data Pipeline Flow
```plaintext
1. Simulate transaction data → Save as CSV  
2. Load raw CSV into Firebase  
3. Extract from Firebase → Transform → Load into MySQL  
4. Export clean MySQL data → CSV  
5. Upload CSV to Looker Studio → Build Dashboard
```

## Setup Instructions

### 1️ Simulate and Save CSV
python generate_transactions.py


### 2 Upload to Firebase
python upload_to_firebase.py

### 3 ETL to MySQL
python firebase_to_mysql.py


### 4 Export Clean Data
mysqldump -u USER -pPASSWORD DATABASE_NAME > clean_data.csv


### 5 Upload to Looker Studio
- Go to Looker Studio
- Create Data Source → CSV Upload → Select clean_data.csv
- Create calculated fields:
    - transaction_day
    - transaction_hour
    - success_flag
    - failure_flag

- Build visualizations

## 📊 Dashboard Visuals
- Daily/Weekly Transaction Volume
- Success vs Failure Rates
- Top Users by Transaction Amount
- Peak Transaction Hours (Heatmap)

## 🚀 Challenges & Solutions
| Challenge                             | Solution                                    |
| ------------------------------------- | ------------------------------------------- |
| MySQL not connecting to Looker Studio | Used CSV upload as alternative              |
| Status values had inconsistent casing | Applied `UPPER()` in Looker formulas        |
| TIME/DATE parsing errors              | Converted timestamp using `DATETIME` format |





