def avg_ratings(movie_ratings):
    avg = sum(movie_ratings.values())/len(movie_ratings)
    return round(avg,2)

def highest_rated(movie_ratings):
    data = max(movie_ratings.items(),key=lambda m:m[1])
    maX_rate = data[1]
    movie_name = data[0]
    return movie_name,maX_rate

def find_top_performer():
    lst=list(sorted(movie_ratings.items(), key=lambda i:i[1],reverse=True))
    tp_lst = lst[:3]
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


