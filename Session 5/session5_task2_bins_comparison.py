
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
scores = np.random.randint(120, 221, size=60)

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
fig.suptitle('IPL Match Scores Distribution across Different Bin Configurations', fontsize=13, fontweight='bold')

bin_counts = [5, 10, 15]
colors = ['#1f77b4', '#2ca02c', '#d62728']

for ax, b, c in zip(axes, bin_counts, colors):
    ax.hist(scores, bins=b, color=c, edgecolor='black', alpha=0.8)
    ax.set_title(f'Histogram with bins = {b}', fontsize=11, fontweight='semibold')
    ax.set_xlabel('Runs per Team', fontsize=9.5)
    ax.set_ylabel('Frequency', fontsize=9.5)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session5_task2_bins_comparison.png', dpi=150)
plt.close()

print("session5_task2_bins_comparison.py executed successfully. Chart saved as session5_task2_bins_comparison.png (150 DPI).")
