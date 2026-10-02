
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
days = [f'Day {i}' for i in range(1, 11)]
mean_delivery = np.array([42, 38, 45, 35, 48, 52, 40, 36, 44, 46])
std_dev = np.array([4.2, 3.5, 5.1, 3.0, 4.8, 6.2, 3.8, 3.2, 4.5, 5.0])

plt.figure(figsize=(9.5, 4.8))
plt.errorbar(
    days, 
    mean_delivery, 
    yerr=std_dev, 
    fmt='-o', 
    color='#2874F0', 
    ecolor='#FF6161', 
    elinewidth=2, 
    capsize=5, 
    capthick=1.5, 
    linewidth=2, 
    markersize=6, 
    label='Mean Delivery Time ± 1 SD'
)

plt.title('Flipkart Average Delivery Times with Standard Deviation (10 Days)', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Day', fontsize=10)
plt.ylabel('Delivery Time (minutes)', fontsize=10)
plt.legend(loc='upper left', frameon=True)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session9_task3_error_bars.png', dpi=150)
plt.close()

print("session9_task3_error_bars.py executed successfully. Chart saved as session9_task3_error_bars.png (150 DPI).")
