

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
posts = [12, 19, 15, 24]
colors = ['#405DE6', '#5851DB', '#833AB4', '#C13584']

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Quarterly Instagram Posts Activity (Multi-Chart Comparison)', fontsize=14, fontweight='bold')

axes[0, 0].plot(quarters, posts, color='#E1306C', marker='o', linewidth=2.5, markersize=7)
axes[0, 0].set_title('Trend Progression (Line Chart)', fontsize=11, fontweight='semibold')
axes[0, 0].set_ylabel('Number of Posts', fontsize=9.5)
axes[0, 0].grid(True, linestyle='--', alpha=0.5)

axes[0, 1].bar(quarters, posts, color=colors, width=0.5, edgecolor='black', alpha=0.85)
axes[0, 1].set_title('Quarterly Volume (Bar Chart)', fontsize=11, fontweight='semibold')
axes[0, 1].set_ylabel('Number of Posts', fontsize=9.5)
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.5)

axes[1, 0].scatter(quarters, posts, color='#FD1D1D', s=120, edgecolor='black', alpha=0.9, zorder=5)
axes[1, 0].set_title('Quarterly Scatter Points (Scatter Plot)', fontsize=11, fontweight='semibold')
axes[1, 0].set_xlabel('Quarter', fontsize=9.5)
axes[1, 0].set_ylabel('Number of Posts', fontsize=9.5)
axes[1, 0].grid(True, linestyle='--', alpha=0.5)

axes[1, 1].pie(posts, labels=quarters, autopct='%1.1f%%', colors=colors, startangle=140, textprops={'fontsize': 9.5})
axes[1, 1].set_title('Annual Share (Pie Chart)', fontsize=11, fontweight='semibold')

plt.tight_layout()
plt.savefig('session7_task2_posts_multipanel.png', dpi=150)
plt.close()

print("session7_task2_posts_multipanel.py executed successfully. Chart saved as session7_task2_posts_multipanel.png (150 DPI).")
