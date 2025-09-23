# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """If all three values are truthy, return a movie dictionary.
    Otherwise, return None."""
    if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating}
    return None


def add_to_watched(user_data, movie):
    """Add the given movie to the user's 'watched' list.
    Return the same user_data.
    Note: In Wave 1 it's okay to modify user_data in place."""
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    """Add the given movie to the user's 'watchlist'.
    Return the same user_data.
    Note: In Wave 1 it's okay to modify user_data in place."""
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    """If a movie with this title is in the 'watchlist':
      - remove it from 'watchlist'
      - add it to 'watched'
    Always return user_data.
    Note: In Wave 1 it's okay to modify user_data in place."""

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
    """Average rating of movies in user_data["watched"].
    If the list is empty, return 0.0."""
    watched = user_data.get("watched", [])
    if not watched:
        return 0.0

    total = 0.0
    count = 0
    for movie in watched:
        # Assume rating exists and is valid (no validation here)
        total += movie.get("rating", 0.0)
        count += 1

    # Do float division
    return total / count if count > 0 else 0.0


def get_most_watched_genre(user_data):
    """Find the most common genre in watched movies.
    If watched is empty, return None."""
    watched = user_data.get("watched", [])
    if not watched:
        return None

    # Count how many times each genre appears
    genre_counts = {}
    for movie in watched:
        genre = movie.get("genre")
        if genre:
            if genre in genre_counts:
                genre_counts[genre] += 1
            else:
                genre_counts[genre] = 1

    # If no genres were found, return None
    if not genre_counts:
        return None

    # Find the genre with the highest count (without using max())
    most_genre = None
    most_count = -1
    for g in genre_counts:
        if genre_counts[g] > most_count:
            most_count = genre_counts[g]
            most_genre = g

    return most_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

