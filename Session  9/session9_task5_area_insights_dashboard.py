
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
x_indices = np.arange(len(days))
spotify_dau = np.array([3.2, 3.8, 3.5, 4.0, 4.6, 5.2, 4.9])
youtube_dau = np.array([5.5, 6.0, 5.8, 6.4, 7.2, 8.5, 8.0])

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x_indices, youtube_dau, color='#FF0000', linewidth=2.4, label='YouTube Active Users')
ax.fill_between(x_indices, youtube_dau, color='#FF0000', alpha=0.25)

ax.plot(x_indices, spotify_dau, color='#1DB954', linewidth=2.4, label='Spotify Active Users')
ax.fill_between(x_indices, spotify_dau, color='#1DB954', alpha=0.35)

ax.set_xticks(x_indices)
ax.set_xticklabels(days, fontsize=10)

ax.set_title('Media Platform Engagement Dynamics – Analytics Insights', fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel('Day of the Week', fontsize=10.5, labelpad=8)
ax.set_ylabel('Active Users (Millions)', fontsize=10.5, labelpad=8)
ax.grid(True, linestyle='--', color='#cccccc', alpha=0.7)

ax.legend(loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#dddddd')

plt.tight_layout()
plt.savefig('session9_task5_area_insights_dashboard.png', dpi=150)
plt.close()

print("session9_task5_area_insights_dashboard.py executed successfully. Chart saved as session9_task5_area_insights_dashboard.png (150 DPI).")
