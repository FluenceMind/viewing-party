# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
        
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for index in range(len(watchlist)):
        current_movie_title = watchlist[index]["title"]
        if current_movie_title == title:
            watched_movie = watchlist.pop(index)
            user_data["watched"].append(watched_movie)

    return user_data

# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    total_ratings = 0.0

    if not user_data["watched"]:
        return total_ratings
    
    for movie in user_data["watched"]:
        rating = movie["rating"]
        total_ratings += rating
    
    ave_rating = total_ratings / len(user_data["watched"])

    return ave_rating


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_count = {}
    max_count = 0
    most_watched_genre = None

    for movie in user_data["watched"]:
        genre = movie["genre"]
        genre_count[genre] = genre_count.get(genre, 0) + 1
        if genre_count[genre] > max_count:
            max_count = genre_count[genre]
            most_watched_genre = genre

    return most_watched_genre

# ------------- WAVE 3 --------------------

def get_titles(watched, from_friends=False):
    """
    Return a set of titles the user or friends have watched.
    """
    titles = set()
    if from_friends:
        for movie in watched:
            for movie in movie["watched"]:
                titles.add(movie["title"])
    else:
        for movie in watched:
            titles.add(movie["title"])
    
    return titles

def get_unique_watched(user_data):
    """
    Movies the user watched that none of the friends watched.
    """
    user_watched = user_data.get("watched", [])

    if not user_watched:
        return []
    
    unique_movies = []
    friends_watched = user_data.get("friends", [])
    friends_movies_titles = get_titles(friends_watched, True)
    
    for movie in user_watched:
        if movie["title"] not in friends_movies_titles:
            unique_movies.append(movie)

    return unique_movies


def get_friends_unique_watched(user_data):
    """
    Movies at least one friend watched that the user hasn't watched.
    Return each title at most once (first occurrence kept).
    """
    unique_movies = []

    user_watched = user_data.get("watched", [])
    friends_watched = user_data.get("friends", [])

    user_movies_titles = get_titles(user_watched)

    titles = set()
    for movies in friends_watched:
        for movie in movies["watched"]:
            title = movie["title"]
            if  title not in user_movies_titles and title not in titles:
                titles.add(movie["title"])
                unique_movies.append(movie)
    
    return unique_movies
    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------