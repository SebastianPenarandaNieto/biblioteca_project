from rest_framework.pagination import PageNumberPagination

class AutorPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class LibroPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class ResenaPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100
