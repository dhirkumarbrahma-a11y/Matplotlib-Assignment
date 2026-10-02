
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
users_millions = [45.2, 48.0, 50.5, 53.1, 56.4, 60.2]

plt.figure(figsize=(8, 4.5))
plt.plot(months, users_millions, color='#1DB954', linewidth=2, marker='o', markerfacecolor='red', markeredgecolor='red', markersize=7)
plt.title('Music Streaming App - Monthly Active Users (6 Months)', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Month', fontsize=10)
plt.ylabel('Active Users (Millions)', fontsize=10)

plt.tight_layout()
plt.savefig('session2_task2_music_users.png', dpi=150)
plt.close()

print("session2_task2_music_users.py executed successfully. Chart saved as session2_task2_music_users.png (150 DPI).")
