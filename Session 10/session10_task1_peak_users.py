
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
active_users_m = np.array([45, 48, 52, 55, 59, 64, 68, 72, 75, 80, 85, 92])  # Millions

plt.figure(figsize=(10, 5))
plt.plot(months, active_users_m, color='#1DB954', marker='o', linewidth=2.5, markersize=6, label='Active Users')

max_idx = np.argmax(active_users_m)
max_month = months[max_idx]
max_users = active_users_m[max_idx]

plt.annotate(
    f'Peak: {max_month} ({max_users}M)',
    xy=(max_idx, max_users),
    xytext=(max_idx - 2.5, max_users - 8),
    arrowprops=dict(facecolor='#111111', shrink=0.08, width=1.5, headwidth=7),
    fontsize=10,
    fontweight='bold',
    bbox=dict(boxstyle='round,pad=0.4', facecolor='#D4EDDA', edgecolor='#1DB954', alpha=0.9)
)

plt.title('Spotify Monthly Active Users Trend (12 Months)', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Month', fontsize=10)
plt.ylabel('Daily Active Users (Millions)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.ylim(40, 100)

plt.tight_layout()
plt.savefig('session10_task1_peak_users.png', dpi=150)
plt.close()

print("session10_task1_peak_users.py executed successfully. Chart saved as session10_task1_peak_users.png (150 DPI).")
