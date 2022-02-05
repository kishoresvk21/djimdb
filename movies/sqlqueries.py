from .models import MovieLikeDislike,TvseriesLikeDislike
from users.models import CustomUser
from django.db.models import Q
def user_liked_movies():
    movie_likes_dislikes=MovieLikeDislike.objects.filter(like=True)
    print(movie_likes_dislikes)
    return movie_likes_dislikes.movielikedislike_set.filter(id=1)
    # return MovieLikeDislike.objects.filter(like=True)