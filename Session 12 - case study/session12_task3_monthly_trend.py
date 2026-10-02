
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales_data.csv')
df['date'] = pd.to_datetime(df['date'])

df['month_year'] = df['date'].dt.to_period('M')
monthly_sales = df.groupby('month_year')['sales_amount'].sum()
month_labels = [period.strftime('%b %Y') for period in monthly_sales.index]

plt.figure(figsize=(10, 5))
plt.plot(month_labels, monthly_sales.values, color='#007ACC', marker='o', linewidth=2.5, markersize=7)

plt.title('Annual Monthly Sales Revenue Trajectory (Presentation-Ready)', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Month', fontsize=10.5)
plt.ylabel('Gross Sales Revenue (INR)', fontsize=10.5)
plt.xticks(rotation=35, ha='right', fontsize=9.5)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session12_task3_monthly_trend.png', dpi=150)
plt.close()

print("session12_task3_monthly_trend.py executed successfully. Chart saved as session12_task3_monthly_trend.png (150 DPI).")
