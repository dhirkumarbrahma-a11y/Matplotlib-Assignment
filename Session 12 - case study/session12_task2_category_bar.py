
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales_data.csv')

category_sales = df.groupby('category')['sales_amount'].sum().sort_values(ascending=False)

colors = ['#2874F0', '#FC8019', '#06C167', '#FF9900', '#C13584']

plt.figure(figsize=(9, 5))
plt.bar(category_sales.index, category_sales.values, color=colors, width=0.55, edgecolor='black', alpha=0.88)

plt.title('Total Sales by Product Category (Flipkart/Myntra Benchmark)', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Product Category', fontsize=10)
plt.ylabel('Total Sales Amount (INR)', fontsize=10)
plt.xticks(rotation=15, ha='right', fontsize=9.5)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session12_task2_category_sales.png', dpi=150)
plt.close()

print("session12_task2_category_bar.py executed successfully. Chart saved as session12_task2_category_sales.png (150 DPI).")
