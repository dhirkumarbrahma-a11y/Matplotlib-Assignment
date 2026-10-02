
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

teams = ['CSK', 'MI', 'RCB', 'KKR']
followers_millions = [15.2, 14.8, 14.1, 5.2]
team_colors = ['#F9CD05', '#004BA0', '#EC1C24', '#3A225D']

fig, ax = plt.subplots(figsize=(7, 7))

wedges, texts, autotexts = ax.pie(
    followers_millions, 
    labels=teams, 
    autopct='%1.1f%%', 
    startangle=120, 
    colors=team_colors,
    pctdistance=0.75,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
    textprops={'fontsize': 10, 'fontweight': 'semibold'}
)

for autotext in autotexts:
    autotext.set_color('white')

# Adding center circle
centre_circle = plt.Circle((0, 0), 0.55, fc='white')
ax.add_artist(centre_circle)

ax.set_title('IPL Teams Instagram Followers Share', fontsize=13, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('session4_task4_ipl_donut.png', dpi=150)
plt.close()

print("session4_task4_ipl_donut.py executed successfully. Chart saved as session4_task4_ipl_donut.png (150 DPI).")
