
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

youtube_hours = np.array([12, 18, 25, 8, 30, 15, 22, 10, 28, 14, 20, 26, 9, 35, 17])
spotify_hours = np.array([8, 14, 20, 6, 26, 11, 19, 7, 23, 12, 16, 22, 5, 29, 13])

slope, intercept = np.polyfit(youtube_hours, spotify_hours, 1)
x_line = np.linspace(youtube_hours.min(), youtube_hours.max(), 100)
y_line = slope * x_line + intercept

eq_text = f'Regression Equation:\n$y = {slope:.2f}x {"+" if intercept >= 0 else "-"} {abs(intercept):.2f}$'

plt.figure(figsize=(9, 5.5))
plt.scatter(youtube_hours, spotify_hours, color='#1DB954', edgecolor='black', s=85, label='User Data Points', zorder=5)
plt.plot(x_line, y_line, color='#FF0000', linewidth=2, linestyle='-', label='Fitted Line')

plt.text(
    0.05, 0.82, 
    eq_text, 
    transform=plt.gca().transAxes, 
    fontsize=10, 
    fontweight='semibold',
    bbox=dict(boxstyle="round,pad=0.5", facecolor='white', edgecolor='#cccccc', alpha=0.9)
)

plt.title('YouTube Watch Hours vs. Spotify Listening Hours', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('YouTube Watch Hours (Weekly)', fontsize=10)
plt.ylabel('Spotify Listening Hours (Weekly)', fontsize=10)
plt.legend(loc='lower right', frameon=True)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session6_task4_media_regression.png', dpi=150)
plt.close()

print("session6_task4_media_regression.py executed successfully. Chart saved as session6_task4_media_regression.png (150 DPI).")
