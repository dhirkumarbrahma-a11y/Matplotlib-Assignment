
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

prices = [
    150, 299, 450, 499, 
    550, 799, 899, 999, 
    1200, 1499, 1750, 1999, 
    2200, 2999, 3499, 4899
]

custom_bin_edges = [100, 500, 1000, 2000, 5000]

plt.figure(figsize=(9, 4.8))
counts, bins, patches = plt.hist(prices, bins=custom_bin_edges, color='#2874F0', edgecolor='black', alpha=0.85)

plt.title('Flipkart Product Price Tiers Distribution', fontsize=12, fontweight='bold', pad=10)
plt.xlabel('Price Range (INR)', fontsize=10)
plt.ylabel('Number of Products', fontsize=10)
plt.xticks(custom_bin_edges)
plt.grid(axis='y', linestyle='--', alpha=0.5)

for count, edge_left, edge_right in zip(counts, custom_bin_edges[:-1], custom_bin_edges[1:]):
    center = (edge_left + edge_right) / 2
    plt.text(center, count + 0.1, f'{int(count)} items', ha='center', va='bottom', fontsize=9.5, fontweight='semibold')

plt.tight_layout()
plt.savefig('session5_task5_flipkart_bins.png', dpi=150)
plt.close()

print("session5_task5_flipkart_bins.py executed successfully. Chart saved as session5_task5_flipkart_bins.png (150 DPI).")
