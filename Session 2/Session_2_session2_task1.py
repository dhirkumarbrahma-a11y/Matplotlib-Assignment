
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [6200, 7500, 8100, 7900, 9300, 11400, 10500]

plt.figure(figsize=(8, 4.5))
plt.plot(days, steps, color='green', linewidth=2)
plt.title('Daily Steps Walked (Last 7 Days)', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Day of the Week', fontsize=10)
plt.ylabel('Steps Count', fontsize=10)

plt.tight_layout()
plt.savefig('session2_task1_steps.png', dpi=150)
plt.close()

print("session2_task1_steps.py executed successfully. Chart saved as session2_task1_steps.png (150 DPI).")
