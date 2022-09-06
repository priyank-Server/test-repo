from apps.snippet import models, serializers
from .pagination import MyPagination
from apps.blog.views import ListRetrieveView


class SnippetView(ListRetrieveView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer
    pagination_class = MyPagination
