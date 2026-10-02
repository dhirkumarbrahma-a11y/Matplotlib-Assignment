
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

apps = ['Zomato', 'Swiggy', 'Uber Eats', 'Dunzo', "Domino's"]
orders = [450, 410, 280, 190, 320]
custom_colors = ['#E23744', '#FC8019', '#06C167', '#00B9F5', '#00549A']

plt.figure(figsize=(8, 5))
# width set to 0.45 (< 0.8) to make bars thinner and increase visual spacing
bars = plt.bar(apps, orders, color=custom_colors, width=0.45)

plt.title('Daily Orders Across Apps (Thinner Bars, width=0.45)', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Food Delivery App', fontsize=10)
plt.ylabel('Number of Daily Orders', fontsize=10)
plt.ylim(0, 520)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2, 
        height + 10, 
        str(height), 
        ha='center', 
        va='bottom', 
        fontsize=10, 
        fontweight='semibold'
    )

plt.tight_layout()
plt.savefig('session3_task4_custom_width.png', dpi=150)
plt.close()

print("session3_task4_custom_width.py executed successfully. Chart saved as session3_task4_custom_width.png (150 DPI).")
