import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# Merge datasets
movies = movies.merge(credits, on="title")

# Select required columns
movies = movies[['title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

# Fill missing values
movies.fillna('', inplace=True)

# Combine text features
movies['tags'] = (
    movies['overview'] + " " +
    movies['genres'] + " " +
    movies['keywords'] + " " +
    movies['cast'] + " " +
    movies['crew']
)

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
vectors = tfidf.fit_transform(movies['tags'])

# Cosine Similarity
similarity = cosine_similarity(vectors)

# Save model
pickle.dump(movies, open("model/movies.pkl", "wb"))
pickle.dump(similarity, open("model/similarity.pkl", "wb"))

print("Model Trained Successfully!")