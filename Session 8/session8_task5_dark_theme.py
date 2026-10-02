

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
zomato_orders = [120, 145, 130, 160, 210, 280, 250]
swiggy_orders = [110, 135, 140, 155, 230, 260, 270]

plt.style.use('dark_background')

plt.figure(figsize=(9, 4.8))

plt.plot(days, zomato_orders, color='#00FFFF', linestyle='--', linewidth=2.5, marker='o', markersize=6, label='Zomato (Neon Cyan)')
plt.plot(days, swiggy_orders, color='#FFEA00', linestyle=':', linewidth=2.8, marker='s', markersize=6, label='Swiggy (Bright Yellow)')

plt.title('Weekly Food Delivery Orders (Dark Theme Restyled)', fontsize=12, fontweight='bold', pad=12, color='#FFFFFF')
plt.xlabel('Day of the Week', fontsize=10, color='#DDDDDD')
plt.ylabel('Daily Orders Placed', fontsize=10, color='#DDDDDD')
plt.legend(loc='upper left', frameon=True, facecolor='#222222', edgecolor='#555555')
plt.grid(True, linestyle='--', color='#444444', alpha=0.6)

plt.tight_layout()
plt.savefig('session8_task5_dark_theme.png', dpi=150)
plt.close()

plt.style.use('default')

print("session8_task5_dark_theme.py executed successfully. Chart saved as session8_task5_dark_theme.png (150 DPI).")
