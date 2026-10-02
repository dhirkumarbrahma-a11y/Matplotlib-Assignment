
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

apps = ['Instagram', 'YouTube', 'WhatsApp', 'Zomato', 'Spotify']
time_hours = [2.5, 3.0, 1.5, 0.5, 1.5]
colors = ['#E1306C', '#FF0000', '#25D366', '#CB202D', '#1DB954']

plt.figure(figsize=(7, 7))
plt.pie(
    time_hours, 
    labels=apps, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    textprops={'fontsize': 10}
)
plt.title('Daily Screen Time Distribution Across 5 Apps', fontsize=12, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('session4_task1_pie.png', dpi=150)
plt.close()

print("session4_task1_pie.py executed successfully. Chart saved as session4_task1_pie.png (150 DPI).")
