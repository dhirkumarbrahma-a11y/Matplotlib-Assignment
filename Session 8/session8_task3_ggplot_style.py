

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

days = [f'Day {i}' for i in range(1, 11)]
sales_lakhs = [14.5, 18.2, 16.0, 21.4, 25.0, 23.5, 29.8, 34.2, 31.0, 38.5]

plt.style.use('ggplot')

plt.figure(figsize=(9, 4.8))
plt.plot(days, sales_lakhs, color='orange', linewidth=2.6, marker='o', markersize=6)

plt.title('Flipkart Daily Sales Trend (10 Days) - ggplot Style', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Days', fontsize=10)
plt.ylabel('Sales Revenue (Lakhs INR)', fontsize=10)

plt.tight_layout()
plt.savefig('session8_task3_ggplot_style.png', dpi=150)
plt.close()

plt.style.use('default')

print("session8_task3_ggplot_style.py executed successfully. Chart saved as session8_task3_ggplot_style.png (150 DPI).")
