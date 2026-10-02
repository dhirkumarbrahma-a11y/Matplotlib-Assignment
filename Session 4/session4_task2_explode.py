
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

categories = ['Food Delivery', 'Shopping', 'Entertainment', 'UPI Payments']
spending_inr = [4500, 8500, 2200, 6800]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

explode = (0, 0.12, 0, 0)

plt.figure(figsize=(7, 7))
plt.pie(
    spending_inr, 
    labels=categories, 
    autopct='%1.1f%%', 
    explode=explode, 
    startangle=90, 
    colors=colors,
    shadow=True,
    textprops={'fontsize': 10}
)
plt.title('Monthly Online Spending Distribution (Highest Spending Highlighted)', fontsize=12, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('session4_task2_explode.png', dpi=150)
plt.close()

print("session4_task2_explode.py executed successfully. Chart saved as session4_task2_explode.png (150 DPI).")
