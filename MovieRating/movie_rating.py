import pandas as pd

def solve():
    movies_data = [
        {'movie_id': 1, 'title': 'Avengers'},
        {'movie_id': 2, 'title': 'Frozen 2'},
        {'movie_id': 3, 'title': 'Joker'},
    ]
    movies_df = pd.DataFrame(movies_data)

    users_data = [
        {'user_id': 1, 'name': 'Daniel'},
        {'user_id': 2, 'name': 'Monica'},
        {'user_id': 3, 'name': 'Maria'},
        {'user_id': 4, 'name': 'James'},
    ]
    users_df = pd.DataFrame(users_data)

    movie_rating_data = [
        {'movie_id': 1, 'user_id': 1, 'rating': 3, 'created_at': '2020-01-12'},
        {'movie_id': 1, 'user_id': 2, 'rating': 4, 'created_at': '2020-02-11'},
        {'movie_id': 1, 'user_id': 3, 'rating': 2, 'created_at': '2020-02-12'},
        {'movie_id': 1, 'user_id': 4, 'rating': 1, 'created_at': '2020-01-01'},
        {'movie_id': 2, 'user_id': 1, 'rating': 5, 'created_at': '2020-02-17'},
        {'movie_id': 2, 'user_id': 2, 'rating': 2, 'created_at': '2020-02-01'},
        {'movie_id': 2, 'user_id': 3, 'rating': 2, 'created_at': '2020-03-01'},
        {'movie_id': 3, 'user_id': 1, 'rating': 3, 'created_at': '2020-02-22'},
        {'movie_id': 3, 'user_id': 2, 'rating': 4, 'created_at': '2020-02-25'},
    ]
    movie_rating_df = pd.DataFrame(movie_rating_data)

    user_ratings_count = movie_rating_df.groupby('user_id').size().reset_index(name='rating_count')
    max_rating_count = user_ratings_count['rating_count'].max()
    top_users_by_count = user_ratings_count[user_ratings_count['rating_count'] == max_rating_count]
    top_users_with_names = pd.merge(top_users_by_count, users_df, on='user_id', how='inner')
    user_result = top_users_with_names.sort_values(by='name').iloc[0]['name']

    movie_rating_df['created_at'] = pd.to_datetime(movie_rating_df['created_at'])
    feb_2020_ratings = movie_rating_df[
        (movie_rating_df['created_at'].dt.year == 2020) &
        (movie_rating_df['created_at'].dt.month == 2)
    ]
    movie_avg_ratings = feb_2020_ratings.groupby('movie_id')['rating'].mean().reset_index(name='avg_rating')
    max_avg_rating = movie_avg_ratings['avg_rating'].max()
    top_movies_by_avg = movie_avg_ratings[movie_avg_ratings['avg_rating'] == max_avg_rating]
    top_movies_with_titles = pd.merge(top_movies_by_avg, movies_df, on='movie_id', how='inner')
    movie_result = top_movies_with_titles.sort_values(by='title').iloc[0]['title']

    return [user_result, movie_result]