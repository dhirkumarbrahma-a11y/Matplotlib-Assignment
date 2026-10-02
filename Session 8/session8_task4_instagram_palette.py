

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
posts = [3, 5, 4, 7, 9, 12, 10]

instagram_palette = [
    '#405DE6',  
    '#5851DB',  
    '#833AB4', 
    '#C13584',  
    '#E1306C',  
    '#FD1D1D',  
    '#F56040'   
]

plt.figure(figsize=(8.5, 4.8))
bars = plt.bar(days, posts, color=instagram_palette, width=0.55, edgecolor='black', alpha=0.9)

plt.title('Weekly Instagram Posts Uploaded (Instagram Brand Palette)', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Day of the Week', fontsize=10)
plt.ylabel('Number of Posts Uploaded', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.25, str(yval), ha='center', va='bottom', fontsize=9.5, fontweight='semibold')

plt.tight_layout()
plt.savefig('session8_task4_instagram_palette.png', dpi=150)
plt.close()

print("session8_task4_instagram_palette.py executed successfully. Chart saved as session8_task4_instagram_palette.png (150 DPI).")
