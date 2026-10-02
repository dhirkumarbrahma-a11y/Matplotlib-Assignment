
import pandas as pd

df = pd.read_csv('sales_data.csv')

print("=== First 5 Records of Sales Dataset ===")
print(df.head())

print("\n=== Dataset Information ===")
print(f"Total Records: {len(df)}")
print(f"Columns: {list(df.columns)}")
print(df.info())
