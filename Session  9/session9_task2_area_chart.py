
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
x_indices = np.arange(len(days))
spotify_dau = np.array([3.2, 3.8, 3.5, 4.0, 4.6, 5.2, 4.9])  # Millions
youtube_dau = np.array([5.5, 6.0, 5.8, 6.4, 7.2, 8.5, 8.0])  # Millions

plt.figure(figsize=(9, 5))

plt.plot(x_indices, youtube_dau, color='#FF0000', linewidth=2, label='YouTube')
plt.fill_between(x_indices, youtube_dau, color='#FF0000', alpha=0.25)

plt.plot(x_indices, spotify_dau, color='#1DB954', linewidth=2, label='Spotify')
plt.fill_between(x_indices, spotify_dau, color='#1DB954', alpha=0.35)

plt.xticks(x_indices, days)
plt.title('Daily Active Users Comparison: Spotify vs YouTube', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Day of the Week', fontsize=10)
plt.ylabel('Active Users (in Millions)', fontsize=10)
plt.legend(loc='upper left', frameon=True)

plt.tight_layout()
plt.savefig('session9_task2_area_chart.png', dpi=150)
plt.close()

print("session9_task2_area_chart.py executed successfully. Chart saved as session9_task2_area_chart.png (150 DPI).")
