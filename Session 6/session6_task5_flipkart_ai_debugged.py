

import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import numpy as np

num_orders = np.array([3, 7, 5, 12, 8, 15, 4, 10, 6, 14])
amount_spent = np.array([1250, 4100, 2800, 8900, 5400, 11500, 1950, 7200, 3600, 10200])

m, c = np.polyfit(num_orders, amount_spent, 1)
x_fit = np.linspace(num_orders.min(), num_orders.max(), 100)
y_fit = m * x_fit + c

plt.figure(figsize=(8.5, 5))
plt.scatter(num_orders, amount_spent, color='#2874F0', edgecolor='black', s=85, label='Customer Orders', zorder=5)
plt.plot(x_fit, y_fit, color='#FF6161', linestyle='--', linewidth=2.2, label=f'Fit Line: Spend = ₹{m:.1f} × Orders + ₹{c:.1f}')

plt.title('Flipkart Orders vs. Total Spend (AI-Refactored Regression)', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Number of Flipkart Orders', fontsize=10)
plt.ylabel('Total Amount Spent (INR)', fontsize=10)
plt.legend(loc='upper left', frameon=True)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session6_task5_flipkart_ai_debugged.png', dpi=150)
plt.close()

print("session6_task5_flipkart_ai_debugged.py executed successfully. Chart saved as session6_task5_flipkart_ai_debugged.png (150 DPI).")
