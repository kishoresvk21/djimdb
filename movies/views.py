from .serializers import MoviesSerializer,DirectorSerializer,\
    ActorSerializer,GeneresSerializer,LanguageSerializer,OnlinePlatformSerializer,TvSeriesSerializer,\
    MovieLikeDislikeSerializer,TvSeriesLikeDislikeSerializer
from .models import Movies,Directors,Actors,Generes,Language,OnlinePlatform,TvSeries,MovieLikeDislike,TvseriesLikeDislike
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets,generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import Http404
from rest_framework_simplejwt.authentication import JWTAuthentication
from .paginations import LargeResultsSetPagination,MyCursorPagination
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from .paginations import StandardResultsSetPagination,LargeResultsSetPagination
from . import logger
from datetime import datetime
class TvSeriesView(viewsets.ViewSet):
    def get_permissions(self):
        if self.action == 'list':
            permission_classes=[IsAuthenticated]
        else:
            permission_classes=[IsAdminUser]
        return [permission() for permission in permission_classes]

    def list(self,request):
        queryset=TvSeries.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer=TvSeriesSerializer(result_page,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            query = TvSeries.objects.get(id=pk)
            seriliazer = TvSeriesSerializer(query)
            return Response(seriliazer.data)

    def create(self, request):
        seriliazer = TvSeriesSerializer(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response({'msg': 'Data created','data':seriliazer.data}, status=status.HTTP_200_OK)
        return Response(seriliazer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        id = pk
        query = TvSeries.objects.get(pk=id)
        serializer = TvSeriesSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        id = pk
        stu = TvSeries.objects.get(pk=id)
        serializer = TvSeriesSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data partial update'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        id = pk
        query = TvSeries.objects.get(pk=id)
        query.delete()
        return Response({'msg': 'Data deleted'}, status=status.HTTP_200_OK)


class GeneresView(viewsets.ModelViewSet):
    queryset = Generes.objects.all()
    serializer_class = GeneresSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    pagination_class = LargeResultsSetPagination


class OnlinePlatformView(viewsets.ModelViewSet):
    queryset = OnlinePlatform.objects.all()
    serializer_class = OnlinePlatformSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = MyCursorPagination


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LargeResultsSetPagination


class MoviesAPI(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


# class DirectorCRUD(viewsets.ModelViewSet):
#     queryset = Directors.objects.all()
#     serializer_class = DirectorSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

class DirectorCRUD(viewsets.ViewSet):
    def get_permissions(self):
        if not self.action == 'create':
            permission_classes=[IsAuthenticated]
        return [permission() for permission in permission_classes]

    # def get_permissions(self):
    #     permission_classes=[IsAuthenticatedOrReadOnly]
    #     return [permission() for permission in permission_classes]
    # def get_object(self,pk=None):
    #     try:
    #         return CustomUser.objects.get(pk=pk)
    #     except CustomUser.DoesNotExist:
    #         raise Http404
    def create(self,request):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            logger.info(f"{datetime.now()} Email Sent to Registered User")
            # handle_uploaded_file(request.FILES['image'])
            logger.info(f"{datetime.now()} File Uploaded in Storage")
            serializer.save()
            logger.info(f"{datetime.now()} Data Saved")
            return Response({"msg":"Success","data":serializer.data},status=status.HTTP_200_OK)
        return Response({"msg": "Failure", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        query_set=Directors.objects.all().order_by('username')
        serializer = DirectorSerializer(query_set,many=True)
        if serializer:
            return Response({"data":serializer.data,'message':'success'},status=status.HTTP_200_OK)
        return Response({"data":serializer.errors,'message':'failure'},status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if pk:
            query_set=Directors.objects.filter(pk=pk).first()
            serializer=DirectorSerializer(query_set)
        else:
            query_set = Directors.objects.all().order_by('name')
            serializer = DirectorSerializer(query_set, many=True)
        if serializer:
            return Response({"data":serializer.data,"message":"success"},status=status.HTTP_200_OK)
        return Response({"data":serializer.errors,"message":"failure"},status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if pk:
            query_set=Directors.objects.filter(pk=pk).first()
            serializer=DirectorSerializer(query_set,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'message':'success'},status=status.HTTP_200_OK)
            return Response({'data':serializer.errors,'message':'failure'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'data': None, 'message': 'failure'}, status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self, request, pk=None):
        if pk:
            query_set=Directors.objects.filter(pk=pk).first()
            serializer=DirectorSerializer(query_set,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"message":"success"},status=status.HTTP_200_OK)
            return Response({"data":serializer.errors,"message":"failure"},status=status.HTTP_400_BAD_REQUEST)
        return Response({'data':None,"message":"failure"},status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if pk:
            query_set=Directors.objects.filter(pk=pk).first()
            query_set.delete()
            return Response({"data":None,"message":"success"},status=status.HTTP_200_OK)
        return Response({"data":None,"message":"failure"},status=status.HTTP_400_BAD_REQUEST)




class ActorsViews(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_object(self,pk):
        try:
            return Actors.objects.get(pk=pk)
        except Actors.DoesNotExist:
            raise Http404

    def get(self,request,pk=None):
        if pk:
            actordata=self.get_object(pk)
            serializer=ActorSerializer(actordata)
        else:
            actordata=Actors.objects.all()
            serializer=ActorSerializer(actordata,many=True)
        if serializer:
            return Response({'data':serializer.data,'message':'success'},status=status.HTTP_200_OK)
        return Response({'data':serializer.errors,'message':'failure'},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request,format=None):
        serializer=ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # logger.info(f"{datetime.now()} Actor Record Data Saved")
            return Response({"data":serializer.data,"message":"success"},status=status.HTTP_200_OK)
        return Response({"data": serializer.errors, "message": "failure"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
        actordata=self.get_object(pk)
        serializer=ActorSerializer(actordata,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'success'},status=status.HTTP_200_OK)
        return Response({'data':serializer.errors,'message':'failure'},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        actordata=self.get_object(pk)
        if actordata:
            actordata.delete()
            return Response({'data':None,'message':'success'},status=status.HTTP_200_OK)
        return Response({'data': None, 'message': 'failure'}, status=status.HTTP_400_BAD_REQUEST)


class MovieLikeView(viewsets.ViewSet):
    def get_permissions(self):
        permission_classes=[IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self,request):
        request.data['user']=request.user.id
        check_movie=Movies.objects.filter(id=request.data.get('movie')).first()
        if not check_movie:
            return Response({'msg':'Movie Not Found','data':None},status=status.HTTP_204_NO_CONTENT)
        check_movie_like_dislike=MovieLikeDislike.objects.filter(movie=request.data.get('movie')).first()
        if check_movie_like_dislike:
            if check_movie_like_dislike.like == 0 and check_movie_like_dislike.dislike == 0:
                like=1
                dislike=0
            elif check_movie_like_dislike.like == 1 and check_movie_like_dislike.dislike == 0:
                like=0
                dislike=0
            elif check_movie_like_dislike.like == 0 and check_movie_like_dislike.dislike == 1:
                like=1
                dislike=0
            request.data['like']=like
            request.data['dislike']=dislike
            serializer=MovieLikeDislikeSerializer(check_movie_like_dislike,data=request.data)
            if serializer.is_valid():
                serializer.save()
        else:
            request.data['like']=1
            serializer=MovieLikeDislikeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        return Response({"msg":"Success","data":serializer.data},status=status.HTTP_200_OK)


class MovieDisLikeView(viewsets.ViewSet):
    def get_permissions(self):
        if self.action == "create":
            permission_classes=[IsAuthenticated]
            return [permission() for permission in permission_classes]

    def create(self,request):
        request.data['user']=request.user.id
        check_movie=Movies.objects.filter(id=request.data.get('movie')).first()
        if not check_movie:
            return Response({'msg':'Movie Not Found','data':None},status=status.HTTP_204_NO_CONTENT)
        check_movie_like_dislike=MovieLikeDislike.objects.filter(movie=request.data.get('movie')).first()
        if check_movie_like_dislike:
            if check_movie_like_dislike.like == 0 and check_movie_like_dislike.dislike == 0:
                like=0
                dislike=1
            elif check_movie_like_dislike.like == 1 and check_movie_like_dislike.dislike == 0:
                like=0
                dislike=1
            elif check_movie_like_dislike.like == 0 and check_movie_like_dislike.dislike == 1:
                like=0
                dislike=0
            request.data['like']=like
            request.data['dislike']=dislike
            serializer=MovieLikeDislikeSerializer(check_movie_like_dislike,data=request.data)
            if serializer.is_valid():
                serializer.save()
        else:
            request.data['dislike']=1
            serializer=MovieLikeDislikeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        return Response({"msg":"Success","data":serializer.data},status=status.HTTP_200_OK)


class TvseriesLikeView(viewsets.ViewSet):

    def get_permissions(self):
        if self.action == 'create':
            permission_classes=[IsAuthenticated]
            return [permission() for permission in permission_classes]

    def create(self, request):
        user_id = request.user.id
        request.data['user']=user_id
        check_tvseries=TvSeries.objects.filter(id=request.data.get('tvseries')).first()
        if not check_tvseries:
            return Response({"msg":"TvSeries Not Found","data":None},status=status.HTTP_204_NO_CONTENT)

        check_tvseries_like_dislike=TvseriesLikeDislike.objects.filter(tvseries=request.data.get('tvseries')).first()
        if check_tvseries_like_dislike:
            if check_tvseries_like_dislike.like==0 and check_tvseries_like_dislike.dislike==0:
                like=1
                dislike=0
            elif check_tvseries_like_dislike.like==1 and check_tvseries_like_dislike.dislike==0:
                like=0
                dislike=0
            elif check_tvseries_like_dislike.like==0 and check_tvseries_like_dislike.dislike==1:
                like=1
                dislike=0
            request.data['like'] = like
            request.data['dislike']=dislike
            serializer = TvSeriesLikeDislikeSerializer(check_tvseries_like_dislike, data=request.data)
            if serializer.is_valid():
                serializer.save()
        else:
            request.data['like']=1
            serializer = TvSeriesLikeDislikeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        return Response({'msg': 'Data created','data':serializer.data}, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TvseriesDisLikeView(viewsets.ViewSet):

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
            return [permission() for permission in permission_classes]


    def create(self, request):
        user_id = request.user.id
        request.data['user'] = user_id
        check_tvseries = TvSeries.objects.filter(id=request.data.get('tvseries')).first()
        if not check_tvseries:
            return Response({"msg": "Not Found", "data": None}, status=status.HTTP_204_NO_CONTENT)

        check_tvseries_like_dislike = TvseriesLikeDislike.objects.filter(tvseries=request.data.get('tvseries')).first()
        print(check_tvseries_like_dislike)
        if check_tvseries_like_dislike:
            if check_tvseries_like_dislike.like == 0 and check_tvseries_like_dislike.dislike == 0:
                dislike = 1
                like=0
            elif check_tvseries_like_dislike.like == 1 and check_tvseries_like_dislike.dislike == 0:
                dislike = 1
                like=0
            elif check_tvseries_like_dislike.like == 0 and check_tvseries_like_dislike.dislike == 1:
                dislike = 0
                like=0
            request.data['dislike'] = dislike
            request.data['like'] = like
            serializer = TvSeriesLikeDislikeSerializer(check_tvseries_like_dislike, data=request.data)
            if serializer.is_valid():
                serializer.save()
        else:
            request.data['dislike'] = 1
            serializer = TvSeriesLikeDislikeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        return Response({'msg': 'Data created', 'data': serializer.data}, status=status.HTTP_200_OK)


class UserLikedMoviesSeries(viewsets.ViewSet):
    def create(self,request):
        request.data['logged_in_user']=request.user.id
        movies_list=MovieLikeDislike.objects.filter(like=True).\
            filter(user=request.data.get('searchuser'))
        serializer=MovieLikeDislikeSerializer(movies_list,many=True)
        if serializer:
            return Response({"data":serializer.data,"message":"success"},status=status.HTTP_200_OK)
        return Response({"data":serializer.errors,"message":"failure"},status=status.HTTP_400_BAD_REQUEST)

# class