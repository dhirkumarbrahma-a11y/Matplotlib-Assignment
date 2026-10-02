
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
active_users_k = [420, 435, 410, 460, 510, 580, 540]

# Set exact figure dimensions: 10 inches wide by 4 inches tall
plt.figure(figsize=(10, 4))
plt.plot(days, active_users_k, color='#1DB954', marker='o', linewidth=2.5, markersize=7)

plt.title('Daily Active Users on Music Streaming App (Past 7 Days)', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Day of the Week', fontsize=10)
plt.ylabel('Active Users (in Thousands)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session8_task1_figure_size.png', dpi=150)
plt.close()

print("session8_task1_figure_size.py executed successfully. Chart saved as session8_task1_figure_size.png (150 DPI).")
