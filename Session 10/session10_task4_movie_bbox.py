
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

movies = ['Dune 2', 'Oppenheimer', 'KGF 2', 'Jawan', 'Interstellar', '12th Fail', 'RRR', 'Animal', 'Stree 2', 'Kantara']
reviews_count = np.array([45, 82, 95, 110, 75, 38, 88, 105, 92, 60])  # in thousands
ratings = np.array([8.8, 8.9, 8.4, 7.8, 8.7, 9.2, 8.3, 7.1, 7.6, 8.5])

max_rating_idx = np.argmax(ratings)
best_movie = movies[max_rating_idx]
best_reviews = reviews_count[max_rating_idx]
best_rating = ratings[max_rating_idx]

plt.figure(figsize=(9, 5.5))
plt.scatter(reviews_count, ratings, color='#007ACC', edgecolor='black', s=90, alpha=0.85, label='Movies')

plt.annotate(
    f'Highest Rated:\n{best_movie} ({best_rating}/10)',
    xy=(best_reviews, best_rating),
    xytext=(best_reviews + 10, best_rating - 0.4),
    arrowprops=dict(facecolor='#E23744', shrink=0.08, width=1.6, headwidth=7),
    fontsize=9.5,
    fontweight='bold',
    bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF8E7', edgecolor='#E23744', linewidth=1.5, alpha=0.95)
)

plt.title('Movie Ratings vs. Total Reviews (BookMyShow Platform)', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Number of User Reviews (in Thousands)', fontsize=10)
plt.ylabel('Average Rating (out of 10)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.ylim(6.5, 9.8)

plt.tight_layout()
plt.savefig('session10_task4_movie_bbox.png', dpi=150)
plt.close()

print("session10_task4_movie_bbox.py executed successfully. Chart saved as session10_task4_movie_bbox.png (150 DPI).")
