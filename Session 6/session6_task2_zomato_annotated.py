
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

friends = ['Aman', 'Priya', 'Rohan', 'Sneha', 'Vikram', 'Ananya', 'Rahul', 'Neha', 'Karan', 'Pooja', 'Aditya', 'Riya']
num_orders = [6, 12, 9, 15, 4, 18, 11, 7, 14, 20, 8, 13]
amount_spent = [1800, 4200, 3100, 5800, 1200, 6900, 3900, 2400, 5100, 7800, 2700, 4800]

plt.figure(figsize=(9, 5.5))
plt.scatter(num_orders, amount_spent, color='#CB202D', edgecolor='black', s=90, alpha=0.85)

plt.title('Zomato Spending vs. Orders Placed (12 Friends)', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Number of Orders Placed', fontsize=10)
plt.ylabel('Amount Spent (INR)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

for name, x, y in zip(friends, num_orders, amount_spent):
    plt.annotate(
        name, 
        (x, y), 
        textcoords="offset points", 
        xytext=(6, 5), 
        ha='left', 
        fontsize=9, 
        fontweight='medium'
    )

plt.tight_layout()
plt.savefig('session6_task2_zomato_annotated.png', dpi=150)
plt.close()

print("session6_task2_zomato_annotated.py executed successfully. Chart saved as session6_task2_zomato_annotated.png (150 DPI).")
