
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
orders_thousands = np.array([210, 195, 230, 240, 280, 310, 260, 290, 320, 380, 420, 450])

min_idx = np.argmin(orders_thousands)
min_month = months[min_idx]
min_orders = orders_thousands[min_idx]

bar_colors = ['#E23744' if i != min_idx else '#8B0000' for i in range(len(months))]

plt.figure(figsize=(10, 5))
bars = plt.bar(months, orders_thousands, color=bar_colors, width=0.55, edgecolor='black', alpha=0.85)

plt.annotate(
    f'Lowest: {min_month} ({min_orders}k)',
    xy=(min_idx, min_orders),
    xytext=(min_idx + 0.8, min_orders + 70),
    arrowprops=dict(facecolor='#8B0000', shrink=0.08, width=1.8, headwidth=8),
    fontsize=10,
    fontweight='bold',
    bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF3CD', edgecolor='#FFEEBA', alpha=0.95)
)

plt.title('Zomato Monthly Orders Volume (Lowest Month Highlighted)', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Month', fontsize=10)
plt.ylabel('Orders Placed (in Thousands)', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.ylim(0, 500)

plt.tight_layout()
plt.savefig('session10_task2_lowest_orders_arrow.png', dpi=150)
plt.close()

print("session10_task2_lowest_orders_arrow.py executed successfully. Chart saved as session10_task2_lowest_orders_arrow.png (150 DPI).")
