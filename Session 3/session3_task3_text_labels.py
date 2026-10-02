
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

apps = ['Zomato', 'Swiggy', 'Uber Eats', 'Dunzo', "Domino's"]
orders = [450, 410, 280, 190, 320]
custom_colors = ['#E23744', '#FC8019', '#06C167', '#00B9F5', '#00549A']

plt.figure(figsize=(8, 5))
bars = plt.bar(apps, orders, color=custom_colors)
plt.title('Daily Orders with Value Labels', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Food Delivery App', fontsize=10)
plt.ylabel('Number of Daily Orders', fontsize=10)
plt.ylim(0, 520)

# Iterate through bars and add text label above each bar
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
plt.savefig('session3_task3_text_labels.png', dpi=150)
plt.close()

print("session3_task3_text_labels.py executed successfully. Chart saved as session3_task3_text_labels.png (150 DPI).")
