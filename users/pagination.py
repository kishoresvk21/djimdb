# from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination,CursorPagination

class MyPagination(LimitOffsetPagination):
    default_limit = 1

class MyCursorPagination(CursorPagination):
    page_size = 1
    ordering = 'id'

# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 20
#
# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 1
#     page_size_query_param = 'page_size'
#     max_page_size = 2