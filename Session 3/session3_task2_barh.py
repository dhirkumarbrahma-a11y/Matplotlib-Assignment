
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

influencers = ['Cristiano', 'Kylie Jenner', 'Selena Gomez', 'Leo Messi', 'Ariana Grande', 'Kim Kardashian']
followers_millions = [635, 399, 427, 504, 378, 362]

plt.figure(figsize=(9, 4.8))
plt.barh(influencers, followers_millions, color='#C13584', edgecolor='#833AB4')
plt.title('Instagram Influencer Follower Counts', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Followers (in millions)', fontsize=10)
plt.ylabel('Influencer', fontsize=10)

plt.tight_layout()
plt.savefig('session3_task2_barh.png', dpi=150)
plt.close()

print("session3_task2_barh.py executed successfully. Chart saved as session3_task2_barh.png (150 DPI).")
