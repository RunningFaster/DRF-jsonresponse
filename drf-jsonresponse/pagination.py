from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from collections import OrderedDict
from rest_framework.response import Response


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        msg = 'success'
        if not data:
            msg = "data not found"
        data = dict(count=self.page.paginator.count,
                    next=self.get_next_link(),
                    previous=self.get_previous_link(),
                    results=data)
        return Response(OrderedDict([
            ('message', msg),
            ('data', data),
        ]))
