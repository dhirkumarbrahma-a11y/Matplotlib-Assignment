
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
zomato_orders = [120, 145, 130, 160, 210, 280, 250]
swiggy_orders = [110, 135, 140, 155, 230, 260, 270]

plt.figure(figsize=(9, 4.8))

# Dashed line for Zomato, Dotted line for Swiggy
plt.plot(days, zomato_orders, color='#E23744', linestyle='--', linewidth=2.4, marker='o', label='Zomato (Dashed)')
plt.plot(days, swiggy_orders, color='#FC8019', linestyle=':', linewidth=2.6, marker='s', label='Swiggy (Dotted)')

plt.title('Weekly Food Orders Comparison: Zomato vs Swiggy', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Day of the Week', fontsize=10)
plt.ylabel('Daily Orders Placed', fontsize=10)
plt.legend(loc='upper left', frameon=True)
plt.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig('session8_task2_line_styles.png', dpi=150)
plt.close()

print("session8_task2_line_styles.py executed successfully. Chart saved as session8_task2_line_styles.png (150 DPI).")
