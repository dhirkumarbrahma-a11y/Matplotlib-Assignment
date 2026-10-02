

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

apps = ['Instagram', 'YouTube', 'WhatsApp', 'Spotify']
time_hours = [2.5, 3.5, 1.5, 1.5]
colors = ['#E1306C', '#FF0000', '#25D366', '#1DB954']

plt.figure(figsize=(7, 7))
wedges, texts, autotexts = plt.pie(
    time_hours, 
    labels=apps, 
    autopct='%1.1f%%', 
    startangle=130, 
    colors=colors,
    pctdistance=0.72,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
    textprops={'fontsize': 10, 'fontweight': 'medium'}
)

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

plt.title('Daily App Screen Time Distribution', fontsize=13, fontweight='bold', pad=15)

plt.tight_layout()
# Export chart as PDF vector document
plt.savefig('session11_task3_screen_time.pdf', format='pdf')
# Also save PNG for visual verification and PPT inclusion
plt.savefig('session11_task3_screen_time.png', dpi=150)
plt.close()

print("session11_task3_save_pdf.py executed successfully. Saved as session11_task3_screen_time.pdf.")
