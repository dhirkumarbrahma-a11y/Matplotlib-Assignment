

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
zomato_orders = [14, 18, 12, 22, 19, 25]
swiggy_orders = [10, 15, 17, 16, 23, 20]
dominos_orders = [6, 8, 5, 9, 7, 10]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14, 4.8), sharey=True)
fig.suptitle('Monthly Food Delivery Orders Comparison (Shared Y-Axis)', fontsize=13, fontweight='bold')

ax1.bar(months, zomato_orders, color='#E23744', edgecolor='black', alpha=0.85)
ax1.set_title('Zomato Orders', fontsize=11, fontweight='semibold')
ax1.set_xlabel('Month', fontsize=9.5)
ax1.set_ylabel('Number of Orders', fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

ax2.bar(months, swiggy_orders, color='#FC8019', edgecolor='black', alpha=0.85)
ax2.set_title('Swiggy Orders', fontsize=11, fontweight='semibold')
ax2.set_xlabel('Month', fontsize=9.5)
ax2.grid(axis='y', linestyle='--', alpha=0.5)

ax3.bar(months, dominos_orders, color='#00549A', edgecolor='black', alpha=0.85)
ax3.set_title("Domino's Orders", fontsize=11, fontweight='semibold')
ax3.set_xlabel('Month', fontsize=9.5)
ax3.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session7_task3_shared_y_orders.png', dpi=150)
plt.close()

print("session7_task3_shared_y_orders.py executed successfully. Chart saved as session7_task3_shared_y_orders.png (150 DPI).")
