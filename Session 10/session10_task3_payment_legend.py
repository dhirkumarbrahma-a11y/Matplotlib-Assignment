

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

payment_methods = ['UPI', 'Card', 'Wallet', 'Cash']
shares = [55, 25, 12, 8]
colors = ['#2874F0', '#FF9900', '#00C853', '#78909C']

plt.figure(figsize=(7.5, 7.5))
wedges, texts, autotexts = plt.pie(
    shares,
    labels=payment_methods,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.7,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
    textprops={'fontsize': 10, 'fontweight': 'medium'}
)

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

plt.legend(
    wedges, 
    payment_methods, 
    title="Payment Method", 
    loc="lower right", 
    frameon=True,
    facecolor='#FAFAFA',
    edgecolor='#CCCCCC'
)

plt.title('Flipkart Payment Methods Distribution', fontsize=13, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('session10_task3_payment_legend.png', dpi=150)
plt.close()

print("session10_task3_payment_legend.py executed successfully. Chart saved as session10_task3_payment_legend.png (150 DPI).")
