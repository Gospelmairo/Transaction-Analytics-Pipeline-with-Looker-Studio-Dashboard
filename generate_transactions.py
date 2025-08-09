import pandas as pd
import random
import uuid
from datetime import datetime, timedelta

# Settings
num_records = 2500
currencies = ['NGN', 'USD', 'BTC']
txn_types = ['deposit', 'withdrawal', 'transfer']
statuses = ['success', 'failed', 'pending']
devices = ['mobile', 'web']
locations = ['Lagos', 'Abuja', 'London', 'New York', 'Berlin', 'Tokyo']

# Generate sample transaction data
def generate_transaction_data(n):
    data = []
    start_date = datetime(2025, 7, 1)
    for _ in range(n):
        txn = {
            'txn_id': str(uuid.uuid4()),
            'user_id': f'user_{random.randint(1, 200)}',
            'amount': round(random.uniform(10, 5000), 2),
            'currency': random.choice(currencies),
            'txn_type': random.choice(txn_types),
            'status': random.choice(statuses),
            'timestamp': (start_date + timedelta(seconds=random.randint(0, 2592000))).isoformat(),
            'device': random.choice(devices),
            'location': random.choice(locations)
        }
        data.append(txn)
    return pd.DataFrame(data)

# Generate and save to CSV
df = generate_transaction_data(num_records)
df.to_csv('simulated_transactions.csv', index=False)
print("✅ Simulated transaction data saved to 'simulated_transactions.csv'")
