import sqlite3
import os

# Ensure the data folder exists
os.makedirs('data', exist_ok=True)
os.makedirs('stock', exist_ok=True)
database = 'stock/stock_entries.db'
CustomerData = 'data/billing_system.db'

def init_db():
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock_entries (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Brand TEXT NOT NULL,
                Model_No TEXT NOT NULL,
                Gender TEXT NOT NULL,
                Color TEXT NOT NULL,
                Quantity INTEGER NOT NULL,
                Price REAL NOT NULL
            )
        ''')
        conn.commit()

    with sqlite3.connect(CustomerData) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                OrderNo INTEGER PRIMARY KEY,
                Name TEXT,
                PhoneNo TEXT,
                StartDate TEXT,
                EndDate TEXT,
                Address TEXT,
                TotalSales REAL,
                DiscountAmount REAL,
                PayableAmount REAL,
                CashAmount REAL,
                UPIAmount REAL,
                CardAmount REAL,
                BalanceAmount REAL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                OrderNo INTEGER,
                Barcode TEXT,
                Product TEXT,
                ProductCode TEXT,
                Description TEXT,
                Quality INTEGER,
                Colour TEXT,
                ItemDiscount REAL,
                Discount REAL,
                Price REAL,
                FOREIGN KEY (OrderNo) REFERENCES orders (OrderNo)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prescriptions (
                OrderNo INTEGER,
                DVRightSPH TEXT,
                DVRightCYL TEXT,
                DVRightAxis TEXT,
                DVLeftSPH TEXT,
                DVLeftCYL TEXT,
                DVLeftAxis TEXT,
                NVRightSPH TEXT,
                NVRightCYL TEXT,
                NVRightAxis TEXT,
                NVLeftSPH TEXT,
                NVLeftCYL TEXT,
                NVLeftAxis TEXT,
                FOREIGN KEY (OrderNo) REFERENCES orders (OrderNo)
            )
        ''')
        conn.commit()

if __name__ == '__main__':
    init_db()
