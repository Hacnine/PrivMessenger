from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):
    default_limit = 25
    limit_query_param = 'page'
    # page_size = 25
    # page_size_query_param = 'records'
    # max_page_size = 10
    # last_page_strings = 'end'
    # Override query 'page=4' to 'p=4'
    # page_query_param = 'p'
