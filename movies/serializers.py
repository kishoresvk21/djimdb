from rest_framework import serializers
from .models import Movies,Directors,Actors,Generes,Language,OnlinePlatform,\
    TvSeries,MovieLikeDislike,TvseriesLikeDislike
from django.contrib.auth.hashers import make_password
from users.serializers import RegistrationSerializer

class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)


class GeneresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Generes
        fields='__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Directors
        fields='__all__'
    # def update(self, instance, validated_data):
    #     partial=True
    #     print(instance.age)
    #
    #     print(validated_data)
    #     return instance

class MoviesSerializer(serializers.ModelSerializer):
    # # director = DirectorSerializer()
    likes = serializers.IntegerField(default=0)
    dislikes = serializers.IntegerField(default=0)
    # dir_rel=serializers.PrimaryKeyRelatedField(read_only=True)
    # gen_rel=serializers.RelatedField(many=True,read_only=True)
    # language_rel=serializers.RelatedField(many=True,read_only=True)
    # platform_rel=serializers.RelatedField(many=True,read_only=True)
    # generes=GeneresSerializer(many=True)
    # director=serializers.StringRelatedField(read_only=True)
        # many=True,read_only=True,view_name='movie-detail')
    class Meta:
        model=Movies
        # likes=MovieLikeDislike.objects.filter(like=1).count
        # dislikes = MovieLikeDislike.objects.filter(dislikes=1).count
        fields=[
            'name',
            'rating',
            'release_date',
            'director',
            'generes',
            'starring',
            'language',
            'platform',
            'generes',
            'likes',
            'dislikes'
        ]
        read_only_fields =('id','like_count','dislike_count','created_at','updated_at') #'liked_people','disliked_people'
        # extra_kwargs={"likes_count":{"write_only":True},"dislike_count":{"write_only":True},"liked_people":{"write_only":True},"disliked_people":{"write_only":True}}

    def get_fields(self):
        likes=MovieLikeDislike.objects.filter(like=1).count
        dislikes= MovieLikeDislike.objects.filter(dislike=1).count


    #     star_data=validated_data.pop('starring')
    #     language_data=validated_data.pop('language')
    #     generes_data=validated_data.pop('generes')
    #     platform_data=validated_data.pop('platform')
    #     import itertools
    #     movie = Movies.objects.create(**validated_data)
    #     for (a,b,c,d) in itertools.zip_longest(star_data,language_data,generes_data,platform_data):
    #         if a:
    #             movie.starring.add(a.id)
    #         if b:
    #             movie.language.add(b.id)
    #         if c:
    #             movie.generes.add(c.id)
    #         if d:
    #             movie.platform.add(d.id)
    #     return movie

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actors
        fields='__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Language
        fields='__all__'

class OnlinePlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model=OnlinePlatform
        fields='__all__'

class TvSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=TvSeries
        fields='__all__'


# class TechnologySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=5)
#     is_active = serializers.BooleanField()
#
#     def create(self, validate_data):
#         return TvSeries.objects.create(**validate_data)
#
#     def update(self, instance, validate_data):  # instance is the new data, validate_data has the old data
#         instance.name = validate_data.get('name', instance.name)
#         instance.is_active = validate_data.get('is_active', instance.is_active)
#         instance.save()
#         return instance
#
#     # object level validations
#     def validate(self, data):
#         nm = data.get('name')
#         if len(nm) < 3:
#             raise serializers.ValidationError('Name validation')
#         return data
#


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        # model = UserModel
        # fields = ['id','name','email','phone','technology']
        fields="__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value: str):
          return make_password(value)


    def validate_username(self, username):
        if len(username)<=2:
            raise serializers.ValidationError(["Username is too short"])
        return username

    def validate_email(self,email):
        if not "@" in email or not (".com" or ".org" or ".edu" or ".gov" or ".net") in email[-4:]:
            raise serializers.ValidationError(["Invalid Email"])
        return email

    def validate_mobile(self,mobile):
        if len(mobile) < 10:
            raise serializers.ValidationError(["Phone should 10 numbers"])
        return mobile




class TvSeriesLikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TvseriesLikeDislike
        fields='__all__'


from users.models import CustomUser
class MovieLikeDislikeSerializer(serializers.ModelSerializer):
    movie = RelatedFieldAlternative(queryset=Movies.objects.all(), serializer=MoviesSerializer)
    user=RelatedFieldAlternative(queryset=CustomUser.objects.all(), serializer=RegistrationSerializer)

    class Meta:
        model=MovieLikeDislike
        fields = [
            'like',
            'dislike',
            'movie',
            'user',
        ]

