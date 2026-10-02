
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales_data.csv')
category_sales = df.groupby('category')['sales_amount'].sum().sort_values(ascending=False)

colors = ['#2874F0', '#FC8019', '#06C167', '#FF9900', '#C13584']

plt.figure(figsize=(9.5, 5.5))
bars = plt.bar(category_sales.index, category_sales.values, color=colors, width=0.55, edgecolor='black', alpha=0.9)

plt.title('E-Commerce Category Sales KPI Dashboard', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Product Category', fontsize=10.5)
plt.ylabel('Total Sales Amount (INR)', fontsize=10.5)
plt.xticks(rotation=15, ha='right', fontsize=9.5)
plt.ylim(0, category_sales.max() * 1.15)  
plt.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2, 
        yval + (category_sales.max() * 0.02), 
        f'₹{yval:,.2f}', 
        ha='center', 
        va='bottom', 
        fontsize=9.5, 
        fontweight='bold'
    )

plt.tight_layout()
plt.savefig('category_sales_kpi.png', dpi=150)
plt.close()

print("session12_task5_annotated_kpi.py executed successfully. Chart saved as category_sales_kpi.png (150 DPI).")
