from django.db import models
from users import models as m
# Create your models here.
class Generes(models.Model):
    name=models.CharField(max_length=40,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name=models.CharField(unique=True,max_length=40,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Actors(models.Model):
    name=models.CharField(unique=True,max_length=50,null=False)
    age=models.IntegerField()
    dob=models.DateField()
    details = models.TextField(max_length=999)

    def __str__(self):
        return self.name

class Directors(models.Model):
    name = models.CharField(unique=True, max_length=50, null=False)
    age = models.IntegerField()
    dob = models.DateField()
    details=models.TextField(max_length=999)

    def __str__(self):
        return self.name


class OnlinePlatform(models.Model):
    name = models.CharField(max_length=40, unique=True)
    about = models.TextField(max_length=200)
    website = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Movies(models.Model):
    name=models.CharField(unique=True,max_length=50,null=False)
    generes=models.ManyToManyField(Generes,related_name='movie_genere')
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    director=models.ForeignKey(Directors,on_delete=models.CASCADE,related_name='movie')
    #models.ForeignKey(Directors,on_delete=models.CASCADE)
    starring=models.ManyToManyField(Actors,related_name='movie_starring')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    language=models.ManyToManyField(Language,related_name='movie_language')
    release_date=models.DateField()
    platform=models.ManyToManyField(OnlinePlatform,related_name='movie_onlineplatform')
    # liked_people=models.ManyToManyField(m.CustomUser,related_name='movielikedpeople')
    # disliked_people=models.ManyToManyField(m.CustomUser,related_name='moviedislikedpeople')
    # like_count=models.IntegerField(default=0)
    # dislike_count=models.IntegerField(default=0)

    def __str__(self):
        return self.name


class TvSeries(models.Model):
    name=models.CharField(unique=True,max_length=50,null=False)
    generes=models.ManyToManyField(Generes)
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    director=models.ForeignKey(Directors,on_delete=models.CASCADE)
    starring=models.ManyToManyField(Actors)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    language=models.ManyToManyField(Language)
    release_date=models.DateField()
    platform=models.ManyToManyField(OnlinePlatform)
    # liked_people = models.ManyToManyField(m.CustomUser,related_name='likedpeople')
    # disliked_people = models.ManyToManyField(m.CustomUser,related_name='dislikedpeople')
    # like_count = models.IntegerField(default=0)
    # dislike_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class MovieLikeDislike(models.Model):
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE,related_name='movieprofile')
    like=models.BooleanField(default=0)
    dislike=models.BooleanField(default=0)
    user=models.ForeignKey(m.CustomUser,on_delete=models.CASCADE,related_name='userprofile')

    def __str__(self):
        return f"{self.movie}->{self.like}->{self.dislike}"

class TvseriesLikeDislike(models.Model):
    tvseries=models.ForeignKey(TvSeries,on_delete=models.CASCADE,related_name='tvprofile')
    like = models.BooleanField(default=0)
    dislike = models.BooleanField(default=0)
    user=models.ForeignKey(m.CustomUser,on_delete=models.CASCADE,related_name='tvlikedislike')

    def __str__(self):
        return f"{self.tvseries}->{self.like}->{self.dislike}"

