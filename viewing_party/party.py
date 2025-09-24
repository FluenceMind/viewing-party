# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """
    If all three values are truthy, return a movie dictionary.
    Otherwise, return None.
    """
    
    if not title or not genre or not rating:
        return None
        
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):    
    """
    Add the given movie to the user's 'watched' list.
    Return the same user_data.
    Note: In Wave 1 it's okay to modify user_data in place.
    """

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """
    Add the given movie to the user's 'watchlist'.
    Return the same user_data.
    Note: In Wave 1 it's okay to modify user_data in place.
    """

    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """
    If a movie with this title is in the 'watchlist':
        - remove it from 'watchlist'
        - add it to 'watched'
    Always return user_data.
    Note: In Wave 1 it's okay to modify user_data in place.
    """

    watchlist = user_data.get("watchlist", [])
    for i in range(len(watchlist)):
        movie = watchlist[i]
        if movie.get("title") == title:
            # Move the movie from watchlist to watched
            moved = watchlist.pop(i)
            user_data["watched"].append(moved)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    """
    Average rating of movies in user_data["watched"].
    If the list is empty, return 0.0.
    """
    total_ratings = 0.0

    watched = user_data.get("watched", [])
    if not watched:
        return total_ratings
    
    for movie in watched:
        rating = movie["rating"]
        total_ratings += rating
    
    ave_rating = total_ratings / len(watched)

    return ave_rating


def get_most_watched_genre(user_data):
    """
    Find the most common genre in watched movies.
    If watched is empty, return None.
    """

    if not user_data["watched"]:
        return None
    
    genre_count = {} 
    max_count = -1
    most_watched_genre = None

    for movie in user_data["watched"]:
        genre = movie["genre"]
        genre_count[genre] = genre_count.get(genre, 0) + 1
        if genre_count[genre] > max_count:
            max_count = genre_count[genre]
            most_watched_genre = genre

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
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
def get_available_recs(user_data):
    """
    Return a list of movie dicts recommended to the user.
    A movie is recommended if:
        - At least one friend watched it,
        - The user has NOT watched it,
        - The movie's host is in the user's subscriptions.
    """
    recommendations = []

    friends_watched = user_data.get("friends", [])
    user_watched = user_data.get("watched", [])
    subscriptions_set = set(user_data["subscriptions"])

    user_movies_titles = get_titles(user_watched)

    friends_movie_titles = set()
    
    for friend in friends_watched:
        for movie in friend.get("watched", []):
            title = movie["title"]
            host = movie["host"] 
            if (
                title not in user_movies_titles 
                and title not in friends_movie_titles
                and host in subscriptions_set
            ):
                    recommendations.append(movie)
                    friends_movie_titles.add(movie["title"])
    return recommendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    """
    Recommend movies by the user's most-watched genre.
    Conditions:
    - user has NOT watched the movie
    - at least one friend HAS watched it
    - movie["genre"] == user's most frequent genre
    No .get() used. Do not modify user_data.
    """
    favorite_genre = get_most_watched_genre(user_data)
    if not favorite_genre:
        return []

    # Titles the user already watched
    user_titles = set()
    for movie in user_data["watched"]:
        user_titles.add(movie["title"])

    recs = []
    seen_titles = set()  # avoid duplicates
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            genre = movie["genre"]
            if title not in user_titles and title not in seen_titles and genre == favorite_genre:
                recs.append(movie)
                seen_titles.add(title)

    return recs


def get_rec_from_favorites(user_data):
    """
    Recommend from the user's favorites only if no friends watched them.
    Conditions:
    - movie is in user_data["favorites"]
    - none of the friends have watched it
    No .get() used. Do not modify user_data.
    """
    # All titles watched by friends
    friends_titles = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_titles.add(movie["title"])

    # Favorites not watched by any friend (no duplicates)
    recs = []
    seen_titles = set()
    for movie in user_data["favorites"]:
        title = movie["title"]
        if title not in friends_titles and title not in seen_titles:
            recs.append(movie)
            seen_titles.add(title)

    return recs
