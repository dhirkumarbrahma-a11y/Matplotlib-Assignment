
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
data_used_gb = [18.5, 22.3, 19.8, 25.4, 28.1, 31.0]

plt.figure(figsize=(8, 4.5))
plt.plot(months, data_used_gb, color='#007ACC', linewidth=2.2, marker='^', markersize=6)

# Explicitly using required plt functions
plt.title('Monthly Data Usage Trend', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Month', fontsize=10)
plt.ylabel('Data Used (GB)', fontsize=10)

plt.tight_layout()
plt.savefig('session2_task4_data_usage.png', dpi=150)
plt.close()

print("session2_task4_data_usage.py executed successfully. Chart saved as session2_task4_data_usage.png (150 DPI).")
