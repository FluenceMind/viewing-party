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

# Made the code DRY later.
def get_unique_watched(user_data):
    # user_data = {'watched': [{...}, {...}, {...}, {...}, {...}, {...}], 
    # 'friends': [{...}, {...}]}
    if not user_data["watched"]:
        return []
    
    friends_movies = []
    unique_movies = []

    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]

    for movie_friends in friends_watched:
        for movie in movie_friends["watched"]:
            friends_movies.append(movie["title"])

    for movie_user in user_watched:
        movie_title = movie_user["title"]
        if movie_title not in friends_movies:
            unique_movies.append(movie_user)

    return unique_movies

def get_friends_unique_watched(user_data):
    
    user_movies = []
    unique_movies = []

    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]

    for movie in user_watched:
            user_movies.append(movie["title"])
    
    titles = []

    for movies in friends_watched:
        for movie in movies["watched"]:
            if movie["title"] not in user_movies and movie["title"] not in titles:
                titles.append(movie["title"])
                unique_movies.append(movie)
    
    return unique_movies
    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------