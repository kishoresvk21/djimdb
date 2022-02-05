from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from django.http import Http404
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import logger
from datetime import datetime
# from .pagination import LargeResultsSetPagination,StandardResultsSetPagination
from .pagination import MyPagination,MyCursorPagination
from rest_framework import viewsets
from .email_send import register_email
from rest_framework import status
from rest_framework.response import Response

# class UserView(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = RegistrationSerializer(queryset, context={"request": request}, many=True)
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     authentication_classes = [JWTAuthentication]
#     pagination_class = MyCursorPagination

def handle_uploaded_file(f):
    with open(f.name , 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class UserView(viewsets.ViewSet):
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
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            password=serializer.validated_data['password']
            hashed_pwd=make_password(password)
            serializer.validated_data['password']=hashed_pwd
            email=serializer.validated_data['email']
            name=serializer.validated_data['username']
            # register_email(email,name)
            logger.info(f"{datetime.now()} Email Sent to Registered User")
            # handle_uploaded_file(request.FILES['image'])
            logger.info(f"{datetime.now()} File Uploaded in Storage")
            serializer.save()
            logger.info(f"{datetime.now()} Data Saved")
            return Response({"msg":"Success","data":serializer.data},status=status.HTTP_200_OK)
        return Response({"msg": "Failure", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        query_set=CustomUser.objects.all().order_by('username').exclude(is_active=0)
        from django.db.models import Count
        query_set = CustomUser.objects.alias(mobile=Count('mobile')).filter(mobile__icontains=5)
        print(query_set)
        serializer = RegistrationSerializer(query_set,many=True)
        if serializer:
            return Response({"data":serializer.data,'message':'success'},status=status.HTTP_200_OK)
        return Response({"data":serializer.errors,'message':'failure'},status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if pk:
            query_set=CustomUser.objects.filter(pk=pk).first()
            serializer=RegistrationSerializer(query_set)
        else:
            query_set = CustomUser.objects.all().order_by('name')
            serializer = RegistrationSerializer(query_set, many=True)
        if serializer:
            return Response({"data":serializer.data,"message":"success"},status=status.HTTP_200_OK)
        return Response({"data":serializer.errors,"message":"failure"},status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if pk:
            query_set=CustomUser.objects.filter(pk=pk).first()
            serializer=RegistrationSerializer(query_set,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data,'message':'success'},status=status.HTTP_200_OK)
            return Response({'data':serializer.errors,'message':'failure'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'data': None, 'message': 'failure'}, status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self, request, pk=None):
        if pk:
            query_set=CustomUser.objects.filter(pk=pk).first()
            serializer=RegistrationSerializer(query_set,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"message":"success"},status=status.HTTP_200_OK)
            return Response({"data":serializer.errors,"message":"failure"},status=status.HTTP_400_BAD_REQUEST)
        return Response({'data':None,"message":"failure"},status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if pk:
            query_set=CustomUser.objects.filter(pk=pk).first()
            query_set.delete()
            return Response({"data":None,"message":"success"},status=status.HTTP_200_OK)
        return Response({"data":None,"message":"failure"},status=status.HTTP_400_BAD_REQUEST)


# class UserView(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     authentication_classes = [JWTAuthentication]
#     pagination_classes = MyPagination
#     def get_object(self, pk):
#         try:
#             return CustomUser.objects.get(pk=pk)
#         except CustomUser.DoesNotExist:
#             raise Http404
#
#
#     def post(self,request,format=None):
#         serializer=RegistrationSerializer(request.data)
#         print(request.data)
#         if serializer.is_valid():
#             password=serializer.validated_data['password']
#             hashed_pwd=make_password(password)
#             serializer.validated_data['password']=hashed_pwd
#             email = serializer.validated_data["email"]
#             name = serializer.validated_data["name"]
#             register_email(email, name)
#             serializer.save()
#             logger.info("Data Saved")
#             return Response({"data":serializer.data,"message": "Success"},status=status.HTTP_201_CREATED)
#         # return Response({"data":None,"message":"failure"},status=status.HTTP_400_BAD_REQUEST)
#     def get(self,request,pk=None):
#         if pk:
#             Userdata=self.get_object(pk)
#             serializer = RegistrationSerializer(Userdata,context={"request": request}, many=True)
#         else:
#             Userdata=CustomUser.objects.all()
#             serializer=RegistrationSerializer(Userdata,many=True,context={"request": request})
#         logger.info(f"{datetime.now()} Returning user data")
#         if serializer:
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         # return Response({"data":serializer.data,"message":"failure"},status=status.HTTP_400_BAD_REQUEST)
#     def put(self,request,pk,format=None):
#         user_id=self.get_object(pk)
#         serializer=RegistrationSerializer(user_id,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"data":serializer.data,"message":"success"},status=status.HTTP_200_OK)
#         return Response({"data":serializer.errors,"message":"failure"},status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,format=None):
#         user_data=self.get_object(pk)
#         user_data.delete()
#         return Response({"data":None,"message":"success"},status=status.HTTP_200_OK)
