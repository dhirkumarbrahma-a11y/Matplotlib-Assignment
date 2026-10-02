
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [6500, 8200, 7800, 9100, 10400, 12500, 11200]
water_litres = [2.5, 3.0, 2.2, 3.5, 3.8, 4.0, 3.2]

plt.figure(figsize=(8, 7))

plt.subplot(2, 1, 1)
plt.plot(days, steps, color='#1f77b4', marker='o', linewidth=2.2, markersize=6)
plt.title('Daily Step Count (Past 7 Days)', fontsize=11, fontweight='bold')
plt.ylabel('Step Count', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

plt.subplot(2, 1, 2)
plt.plot(days, water_litres, color='#00A8E8', marker='s', linewidth=2.2, markersize=6)
plt.title('Daily Water Intake (Past 7 Days)', fontsize=11, fontweight='bold')
plt.xlabel('Day of the Week', fontsize=10)
plt.ylabel('Water Intake (Litres)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session7_task1_health_subplots.png', dpi=150)
plt.close()

print("session7_task1_health_subplots.py executed successfully. Chart saved as session7_task1_health_subplots.png (150 DPI).")
