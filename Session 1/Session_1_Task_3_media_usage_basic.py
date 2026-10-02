
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
spotify_hours = [1.5, 2.0, 1.2, 2.5, 3.0, 4.2, 3.8]
youtube_hours = [2.0, 1.8, 2.2, 1.5, 2.8, 5.0, 4.5]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(days, spotify_hours, color='#1DB954', marker='o')
ax2.plot(days, youtube_hours, color='#FF0000', marker='o')

plt.tight_layout()
plt.savefig('media_usage_basic.png', dpi=150)
plt.close()

print("media_usage_basic.py executed successfully. Chart saved as media_usage_basic.png (150 DPI).")
