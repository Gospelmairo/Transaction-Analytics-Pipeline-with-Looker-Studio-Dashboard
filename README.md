# Transaction Analytics Pipeline with Looker Studio Dashboard
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

### 1️⃣ Simulate and Save CSV
```bash
python generate_transactions.py
```



