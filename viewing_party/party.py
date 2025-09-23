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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

