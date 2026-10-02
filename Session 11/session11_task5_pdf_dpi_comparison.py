
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

categories = ['Instagram', 'YouTube', 'WhatsApp', 'Spotify']
hours = [2.5, 3.5, 1.5, 1.5]
colors = ['#E1306C', '#FF0000', '#25D366', '#1DB954']

fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(
    hours, 
    labels=categories, 
    autopct='%1.1f%%', 
    startangle=130, 
    colors=colors,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
    textprops={'fontsize': 10, 'fontweight': 'bold'}
)
ax.set_title('Screen Time Distribution - PDF Vector Quality Test', fontsize=12, fontweight='bold', pad=15)

plt.savefig('session11_task5_vector.pdf', format='pdf')

plt.savefig('session11_task5_low_res_50dpi.png', dpi=50)

plt.savefig('session11_task5_high_res_300dpi.png', dpi=300)

plt.close()

print("session11_task5_pdf_dpi_comparison.py executed successfully.")
print("Generated:")
print("1. session11_task5_vector.pdf (Infinite vector resolution, zero pixelation at 200%+ zoom)")
print("2. session11_task5_low_res_50dpi.png (Demonstrates pixelation/blurriness)")
print("3. session11_task5_high_res_300dpi.png (Sharp raster comparison)")
