from django.urls import path,include
from . import views
from rest_framework import routers

app_name='imdb'
router=routers.SimpleRouter()
router.register('movies',views.MoviesAPI)
router.register('directors',views.DirectorCRUD,basename='directors')
router.register('generes',views.GeneresView)
router.register('languages',views.LanguageView)
router.register('onlineplatform',views.OnlinePlatformView)
router.register('tvseries',views.TvSeriesView,basename='tvseries')
router.register('tvserieslike',views.TvseriesLikeView,basename='like')
router.register('tvseriesdislike',views.TvseriesDisLikeView,basename='dislike')
router.register('movielike',views.MovieLikeView,basename='like')
router.register('moviedislike',views.MovieDisLikeView,basename='dislike')
router.register('userlikedmovies',views.UserLikedMoviesSeries,basename='userlikedmoviesseries')
# router.register('users',views.UserView)

urlpatterns=[
    path('',include(router.urls)),
    path('actors/',views.ActorsViews.as_view()),
    path('actors/<int:pk>/',views.ActorsViews.as_view()),
]