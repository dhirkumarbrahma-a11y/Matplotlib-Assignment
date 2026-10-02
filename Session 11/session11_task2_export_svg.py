

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
steps = [6200, 7800, 8100, 9400, 10200, 12800, 11500]

plt.figure(figsize=(8.5, 4.5))
plt.plot(days, steps, color='#007ACC', marker='o', linewidth=2.4, markersize=7)

plt.title('Daily Step Count Tracker (Past 7 Days) - Vector SVG Export', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Day of the Week', fontsize=10)
plt.ylabel('Steps Count', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
# Export chart directly as an SVG vector file
plt.savefig('session11_task2_step_count.svg', format='svg')
# Also save PNG for visual verification and PPT inclusion
plt.savefig('session11_task2_step_count.png', dpi=150)
plt.close()

print("session11_task2_export_svg.py executed successfully. Saved as session11_task2_step_count.svg.")
