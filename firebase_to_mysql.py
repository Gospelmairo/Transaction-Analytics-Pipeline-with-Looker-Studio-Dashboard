import firebase_admin
from firebase_admin import credentials, firestore
import mysql.connector
from datetime import datetime

# === Firebase Setup ===
cred = credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# === MySQL Setup ===
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="*****",  # use your actual username
    password="*******#",
    database="fintech_data"
)
cursor = mysql_conn.cursor()

# === Extract from Firestore ===
docs = db.collection('transactions').stream()

for doc in docs:
    data = doc.to_dict()

    try:
        # Parse timestamp
        timestamp = datetime.fromisoformat(data['timestamp'])
    except Exception as e:
        print(f"Skipping doc due to bad timestamp: {e}")
        continue

    # === Load into MySQL ===
    insert_query = """
    REPLACE INTO transactions (
        txn_id, user_id, amount, currency, txn_type,
        status, timestamp, device, location
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data.get('txn_id'),
        data.get('user_id'),
        data.get('amount'),
        data.get('currency'),
        data.get('txn_type'),
        data.get('status'),
        timestamp,
        data.get('device'),
        data.get('location')
    )

    cursor.execute(insert_query, values)

mysql_conn.commit()
cursor.close()
mysql_conn.close()

print("Firestore data successfully loaded into MySQL.")
