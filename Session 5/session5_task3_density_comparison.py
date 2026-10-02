
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
daily_steps = np.random.normal(loc=8500, scale=1800, size=30).astype(int)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
fig.suptitle('Daily Step Counts (1 Month): Frequency vs. Probability Density', fontsize=13, fontweight='bold')

ax1.hist(daily_steps, bins=8, color='#3b528b', edgecolor='black', alpha=0.85)
ax1.set_title('Frequency Histogram (Default)', fontsize=11, fontweight='semibold')
ax1.set_xlabel('Daily Steps', fontsize=10)
ax1.set_ylabel('Count of Days (Frequency)', fontsize=10)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

ax2.hist(daily_steps, bins=8, density=True, color='#5dc863', edgecolor='black', alpha=0.85)
ax2.set_title('Normalized Density Histogram (density=True)', fontsize=11, fontweight='semibold')
ax2.set_xlabel('Daily Steps', fontsize=10)
ax2.set_ylabel('Probability Density', fontsize=10)
ax2.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session5_task3_density_comparison.png', dpi=150)
plt.close()

print("session5_task3_density_comparison.py executed successfully. Chart saved as session5_task3_density_comparison.png (150 DPI).")
