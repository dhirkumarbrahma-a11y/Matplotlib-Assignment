

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

friends = ['Aman', 'Priya', 'Rohan', 'Sneha', 'Vikram', 'Ananya', 'Rahul', 'Neha', 'Karan', 'Pooja', 'Aditya', 'Riya']
num_orders = np.array([6, 12, 9, 15, 4, 18, 11, 7, 14, 20, 8, 13])
amount_spent = np.array([1800, 4200, 3100, 5800, 1200, 6900, 3900, 2400, 5100, 7800, 2700, 4800])

slope, intercept = np.polyfit(num_orders, amount_spent, 1)
x_vals = np.linspace(num_orders.min(), num_orders.max(), 100)
trend_y = slope * x_vals + intercept

plt.figure(figsize=(9, 5.5))
plt.scatter(num_orders, amount_spent, color='#CB202D', edgecolor='black', s=90, label='Actual Data', zorder=5)
plt.plot(x_vals, trend_y, color='#1f77b4', linestyle='--', linewidth=2, label=f'Trend Line (y = {slope:.1f}x + {intercept:.1f})')

for name, x, y in zip(friends, num_orders, amount_spent):
    plt.annotate(name, (x, y), textcoords="offset points", xytext=(6, 5), ha='left', fontsize=9)

plt.title('Zomato Spending with Best-Fit Regression Line', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Number of Orders Placed', fontsize=10)
plt.ylabel('Amount Spent (INR)', fontsize=10)
plt.legend(loc='upper left', frameon=True)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session6_task3_zomato_trendline.png', dpi=150)
plt.close()

print("session6_task3_zomato_trendline.py executed successfully. Chart saved as session6_task3_zomato_trendline.png (150 DPI).")
