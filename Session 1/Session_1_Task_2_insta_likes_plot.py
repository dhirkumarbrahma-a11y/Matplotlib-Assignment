

import matplotlib.pyplot as plt

posts = [f'Post {i}' for i in range(1, 11)]
likes = [124, 185, 142, 210, 195, 260, 310, 280, 345, 420]

plt.figure(figsize=(9, 4.5))
plt.plot(posts, likes, marker='s', color='#E1306C', linewidth=2.2, markersize=6)
plt.title('Instagram Post Performance - Last 10 Posts', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Instagram Posts', fontsize=10)
plt.ylabel('Number of Likes', fontsize=10)
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig('insta_likes_plot.png', dpi=150)
plt.close()

print("insta_likes_plot.py executed successfully. Chart saved as insta_likes_plot.png (150 DPI).")
