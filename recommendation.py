import pickle

# Load saved model
movies = pickle.load(open("model/movies.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))

def recommend(movie_name):
    movie_name = movie_name.lower()

    movie_index = None

    for index, movie in movies.iterrows():
        if movie['title'].lower() == movie_name:
            movie_index = index
            break

    if movie_index is None:
        return []

    distances = list(enumerate(similarity[movie_index]))

    movies_list = sorted(
        distances,
        reverse=True,
        key=lambda x: x[1]
    )[1:11]

    recommendations = []

    for movie in movies_list:
        recommendations.append(
            movies.iloc[movie[0]].title
        )

    return recommendations