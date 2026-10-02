
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales_data.csv')

plt.figure(figsize=(9, 5))
plt.hist(df['sales_amount'], bins=10, color='#833AB4', edgecolor='black', alpha=0.85)

plt.title('Order Value Distribution: Small vs. Large Ticket Purchases (10 Bins)', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Order Amount (INR)', fontsize=10)
plt.ylabel('Number of Orders (Frequency)', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session12_task4_order_size_hist.png', dpi=150)
plt.close()

print("session12_task4_order_size_hist.py executed successfully. Chart saved as session12_task4_order_size_hist.png (150 DPI).")
