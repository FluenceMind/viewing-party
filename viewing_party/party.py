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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

