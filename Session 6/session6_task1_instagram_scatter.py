
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

hours_per_day = [1.2, 2.5, 3.8, 0.8, 4.5, 2.0, 3.2, 1.5, 5.0, 2.8, 3.5, 4.0]
posts_per_month = [4, 10, 18, 2, 25, 8, 15, 6, 28, 12, 16, 22]

plt.figure(figsize=(8, 5))
plt.scatter(hours_per_day, posts_per_month, color='#E1306C', edgecolor='black', s=80, alpha=0.85)

plt.title('Daily Instagram Usage vs. Monthly Posts Uploaded', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Hours Spent per Day', fontsize=10)
plt.ylabel('Number of Posts Uploaded per Month', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session6_task1_instagram_scatter.png', dpi=150)
plt.close()

print("session6_task1_instagram_scatter.py executed successfully. Chart saved as session6_task1_instagram_scatter.png (150 DPI).")
