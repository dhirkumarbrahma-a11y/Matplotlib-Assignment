
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

restaurants = ['Spice Villa', 'Burger Street', 'Tandoor Box', 'Biryani Blues', 'Pasta Bowl']
orders = [340, 480, 290, 520, 210]
colors = ['#E23744', '#FC8019', '#F4C430', '#D11242', '#8B0000']

plt.figure(figsize=(8.5, 4.8))
bars = plt.bar(restaurants, orders, color=colors, width=0.55, edgecolor='black', alpha=0.9)

plt.title('Daily Orders for 5 Zomato Partner Restaurants', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Restaurant Name', fontsize=10)
plt.ylabel('Number of Daily Orders', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 10, str(yval), ha='center', va='bottom', fontsize=9.5, fontweight='semibold')

plt.tight_layout()
plt.savefig('session11_task1_zomato_orders.png', dpi=150)
plt.close()

print("session11_task1_save_png_dpi150.py executed successfully. Saved as session11_task1_zomato_orders.png (150 DPI).")
