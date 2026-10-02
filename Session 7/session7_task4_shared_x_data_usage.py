
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
youtube_data = [18.2, 22.5, 20.1, 26.4, 29.0, 32.5]
instagram_data = [12.0, 14.2, 13.5, 16.8, 18.0, 21.4]
spotify_data = [4.5, 5.2, 4.8, 6.1, 6.8, 7.5]
whatsapp_data = [2.1, 2.4, 2.0, 2.7, 3.1, 3.4]

fig, axes = plt.subplots(2, 2, figsize=(11, 7.5), sharex=True)
fig.suptitle('Monthly App Data Usage Comparison (Shared X-Axis)', fontsize=14, fontweight='bold')

axes[0, 0].plot(months, youtube_data, color='#FF0000', marker='o', linewidth=2.2)
axes[0, 0].set_title('YouTube Usage', fontsize=11, fontweight='semibold')
axes[0, 0].set_ylabel('Data Used (GB)', fontsize=9.5)
axes[0, 0].grid(True, linestyle='--', alpha=0.5)

axes[0, 1].plot(months, instagram_data, color='#E1306C', marker='s', linewidth=2.2)
axes[0, 1].set_title('Instagram Usage', fontsize=11, fontweight='semibold')
axes[0, 1].set_ylabel('Data Used (GB)', fontsize=9.5)
axes[0, 1].grid(True, linestyle='--', alpha=0.5)

axes[1, 0].plot(months, spotify_data, color='#1DB954', marker='^', linewidth=2.2)
axes[1, 0].set_title('Spotify Usage', fontsize=11, fontweight='semibold')
axes[1, 0].set_xlabel('Month', fontsize=10)
axes[1, 0].set_ylabel('Data Used (GB)', fontsize=9.5)
axes[1, 0].grid(True, linestyle='--', alpha=0.5)

axes[1, 1].plot(months, whatsapp_data, color='#25D366', marker='D', linewidth=2.2)
axes[1, 1].set_title('WhatsApp Usage', fontsize=11, fontweight='semibold')
axes[1, 1].set_xlabel('Month', fontsize=10)
axes[1, 1].set_ylabel('Data Used (GB)', fontsize=9.5)
axes[1, 1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session7_task4_shared_x_data_usage.png', dpi=150)
plt.close()

print("session7_task4_shared_x_data_usage.py executed successfully. Chart saved as session7_task4_shared_x_data_usage.png (150 DPI).")
