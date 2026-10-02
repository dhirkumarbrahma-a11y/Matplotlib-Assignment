
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
spotify_hours = [1.5, 2.0, 1.2, 2.5, 3.0, 4.2, 3.8]
youtube_hours = [2.0, 1.8, 2.2, 1.5, 2.8, 5.0, 4.5]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Weekly Digital Media Consumption Insights', fontsize=14, fontweight='bold', y=0.98)

ax1.plot(days, spotify_hours, color='#1DB954', marker='o', linewidth=2.5, markersize=6, label='Spotify')
ax1.set_title('Daily Spotify Listening Time', fontsize=11, fontweight='semibold')
ax1.set_xlabel('Day of the Week', fontsize=10)
ax1.set_ylabel('Listening Duration (Hours)', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_ylim(0, 6)

# Ax 2: YouTube
ax2.plot(days, youtube_hours, color='#FF0000', marker='s', linewidth=2.5, markersize=6, label='YouTube')
ax2.set_title('Daily YouTube Viewing Time', fontsize=11, fontweight='semibold')
ax2.set_xlabel('Day of the Week', fontsize=10)
ax2.set_ylabel('Viewing Duration (Hours)', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.set_ylim(0, 6)

plt.tight_layout()
plt.savefig('media_dashboard_insights.png', dpi=150)
plt.close()

print("media_dashboard_insights.py executed successfully. Chart saved as media_dashboard_insights.png (150 DPI).")
