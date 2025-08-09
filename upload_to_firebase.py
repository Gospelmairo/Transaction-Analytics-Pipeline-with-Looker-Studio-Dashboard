import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# === CONFIGURATION ===
csv_path = 'simulated_transactions.csv'
firebase_key_path = '***************'
collection_name = 'transactions'

# === FIREBASE INIT ===
cred = credentials.Certificate(firebase_key_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

# === LOAD CSV ===
df = pd.read_csv(csv_path)

# === UPLOAD TO FIRESTORE USING BATCH WRITES ===
batch = db.batch()
batch_size = 500  # Firestore has a limit of 500 writes per batch

for i, row in df.iterrows():
    doc_data = row.to_dict()
    doc_ref = db.collection(collection_name).document(doc_data['txn_id'])
    batch.set(doc_ref, doc_data)

    # Commit the batch if the batch size is reached
    if (i + 1) % batch_size == 0:
        batch.commit()
        batch = db.batch()  # Start a new batch

# Commit any remaining documents in the last batch
if df.shape[0] % batch_size != 0:
    batch.commit()

print(f"Uploaded {len(df)} transactions to Firestore collection '{collection_name}' using batch writes")