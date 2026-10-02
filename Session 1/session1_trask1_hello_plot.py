import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [6500, 8200, 7800, 9400, 10200, 12500, 11000]

plt.figure(figsize=(8, 4.5))
plt.plot(days, steps, marker='o', color='#1f77b4', linewidth=2, markersize=6)
plt.title('Daily Steps Walked Over the Past 7 Days', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Day of the Week', fontsize=10)
plt.ylabel('Steps Count', fontsize=10)

plt.tight_layout()
plt.savefig('hello_plot.png', dpi=150)
plt.close()

print("hello_plot.py executed successfully. Chart saved as hello_plot.png (150 DPI).")
