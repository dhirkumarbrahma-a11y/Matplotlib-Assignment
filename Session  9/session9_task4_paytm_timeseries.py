
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

base_date = datetime(2026, 6, 1)
dates = [base_date + timedelta(days=i) for i in range(14)]
balances = [4250, 3900, 3750, 5200, 4800, 4300, 6100, 5700, 5400, 4900, 7200, 6800, 6400, 5950]

fig, ax = plt.subplots(figsize=(10, 4.8))
ax.plot(dates, balances, color='#00B9F5', marker='o', linewidth=2.2, markersize=6)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
fig.autofmt_xdate(rotation=45)

ax.set_title('Paytm Wallet Balance Trend (Past 14 Days)', fontsize=12, fontweight='bold', pad=12)
ax.set_xlabel('Date', fontsize=10)
ax.set_ylabel('Balance (INR)', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('session9_task4_paytm_timeseries.png', dpi=150)
plt.close()

print("session9_task4_paytm_timeseries.py executed successfully. Chart saved as session9_task4_paytm_timeseries.png (150 DPI).")
