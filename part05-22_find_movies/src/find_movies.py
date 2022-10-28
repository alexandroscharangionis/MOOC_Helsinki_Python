def find_movies(database: list, search_term: str):
    movie_results = []
    for movie in database:
        if search_term in movie["name"].lower():
            movie_results.append(movie)
    return movie_results
