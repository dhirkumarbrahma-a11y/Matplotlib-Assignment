
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

categories = ['Food Delivery', 'Shopping', 'Entertainment', 'UPI Payments']
spending_inr = [4500, 8500, 2200, 6800]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

fig, ax = plt.subplots(figsize=(7, 7))

# Pie base
wedges, texts, autotexts = ax.pie(
    spending_inr, 
    labels=categories, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors,
    pctdistance=0.75,
    textprops={'fontsize': 10}
)

# Transform into Donut Chart by adding a central white circle
centre_circle = plt.Circle((0, 0), 0.55, fc='white')
ax.add_artist(centre_circle)

ax.set_title('Monthly Online Spending - Donut Chart', fontsize=12, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('session4_task3_donut.png', dpi=150)
plt.close()

print("session4_task3_donut.py executed successfully. Chart saved as session4_task3_donut.png (150 DPI).")
