
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

apps = ['Zomato', 'Swiggy', 'Uber Eats', 'Dunzo', "Domino's"]
orders = [450, 410, 280, 190, 320]
custom_colors = ['#E23744', '#FC8019', '#06C167', '#00B9F5', '#00549A']

plt.figure(figsize=(8, 4.5))
plt.bar(apps, orders, color=custom_colors)
plt.title('Daily Orders Across Food Delivery Apps', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Food Delivery App', fontsize=10)
plt.ylabel('Number of Daily Orders', fontsize=10)

plt.tight_layout()
plt.savefig('session3_task1_bar.png', dpi=150)
plt.close()

print("session3_task1_bar.py executed successfully. Chart saved as session3_task1_bar.png (150 DPI).")
