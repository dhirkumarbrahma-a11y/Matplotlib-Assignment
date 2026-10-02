
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

delivery_times = [
    32, 28, 45, 30, 36, 40, 29, 34, 38, 31, 
    27, 41, 33, 35, 39, 37, 44, 30, 29, 32, 
    36, 28, 43, 31, 35, 40, 38, 33, 30, 42
]

plt.figure(figsize=(8, 4.5))
plt.hist(delivery_times, bins=8, color='#FC8019', edgecolor='black', alpha=0.85)
plt.title('Distribution of Swiggy Delivery Times (30 Orders)', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Delivery Time (minutes)', fontsize=10)
plt.ylabel('Number of Orders (Frequency)', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session5_task1_delivery_hist.png', dpi=150)
plt.close()

print("session5_task1_delivery_hist.py executed successfully. Chart saved as session5_task1_delivery_hist.png (150 DPI).")
