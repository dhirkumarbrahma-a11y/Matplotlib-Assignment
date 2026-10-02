\
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

months = ['Feb', 'Mar', 'Apr', 'May', 'Jun']
zomato_orders = [14, 18, 12, 22, 19]
swiggy_orders = [10, 15, 17, 16, 23]

plt.figure(figsize=(8.5, 4.5))
plt.plot(months, zomato_orders, color='#E23744', linestyle='-', linewidth=2.2, marker='o', label='Zomato')
plt.plot(months, swiggy_orders, color='#FC8019', linestyle='--', linewidth=2.2, marker='s', label='Swiggy')

plt.title('Monthly Orders Comparison: Zomato vs Swiggy (Last 5 Months)', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Month', fontsize=10)
plt.ylabel('Number of Orders', fontsize=10)
plt.legend(loc='upper left', frameon=True)

plt.tight_layout()
plt.savefig('session2_task3_food_delivery.png', dpi=150)
plt.close()

print("session2_task3_food_delivery.py executed successfully. Chart saved as session2_task3_food_delivery.png (150 DPI).")
