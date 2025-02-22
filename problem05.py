def avg_ratings(movie_ratings):
    tm = len(movie_ratings)
    tr = 0
    for val in movie_ratings.values():
        tr += val
    return round(tr/tm,2)

def highest_rated(movie_ratings):
    maX_rate = 0
    movie_name = ''
    for mn,mr in movie_ratings.items():
        if maX_rate < mr:
            movie_name=''
            maX_rate = mr
            movie_name += mn
    return movie_name,maX_rate

def find_top_performer():
    tp_lst=[]
    for i in range(3):
        mn,mr = highest_rated(movie_ratings)
        tp_lst.append(highest_rated(movie_ratings))
        movie_ratings.pop(mn)
    return tp_lst

movie_ratings = {
    "Inception": 8.8,
    "Interstellar": 8.6,
    "Parasite": 8.9,
    "The Dark Knight": 9.0,
    "Avengers: Endgame": 8.4
}

movie_name,movie_rating = highest_rated(movie_ratings)
print(f'Highest Rated Movie : {movie_name}({movie_rating})')
avg_rate = avg_ratings(movie_ratings)
print(f'Top 3 Movies:{find_top_performer()}')
print(f'Average Rating : {avg_rate}')


