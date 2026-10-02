
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
zomato_orders = np.array([120, 145, 130, 160, 210, 280, 250])
swiggy_orders = np.array([110, 135, 140, 155, 230, 260, 270])

plt.figure(figsize=(9, 5))

plt.bar(days, zomato_orders, label='Zomato', color='#E23744', width=0.55, edgecolor='black', alpha=0.9)
plt.bar(days, swiggy_orders, bottom=zomato_orders, label='Swiggy', color='#FC8019', width=0.55, edgecolor='black', alpha=0.9)

plt.title('Daily Food Delivery Orders (Stacked Zomato & Swiggy)', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Day of the Week', fontsize=10)
plt.ylabel('Total Orders Placed', fontsize=10)
plt.legend(loc='upper left', frameon=True)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session9_task1_stacked_bar.png', dpi=150)
plt.close()

print("session9_task1_stacked_bar.py executed successfully. Chart saved as session9_task1_stacked_bar.png (150 DPI).")
