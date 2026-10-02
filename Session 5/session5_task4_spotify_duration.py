
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
durations = np.random.uniform(120, 300, size=50)

plt.figure(figsize=(8, 4.5))
plt.hist(durations, bins=10, color='purple', edgecolor='black', alpha=0.8)
plt.title('Spotify Song Duration Distribution', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Song Duration (seconds)', fontsize=10)
plt.ylabel('Number of Songs (Frequency)', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session5_task4_spotify_duration.png', dpi=150)
plt.close()

print("session5_task4_spotify_duration.py executed successfully. Chart saved as session5_task4_spotify_duration.png (150 DPI).")
