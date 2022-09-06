from .serializers import *
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from apps.blog import models
from .pagination import MyPagination
from rest_framework import filters


class ListRetrieveView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    pass


class BlogApiView(ListRetrieveView):
    queryset = models.Blog.objects.filter(status=1)
    serializer_class = ReadBlogSerializer
    # pagination_class = MyPagination
    # authentication_classes = [JWTAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__word']
    # filter_fields = ['category']
    # filterset_fields = ['category']

    # def get_queryset(self):
    #     category = self.request.query_params.get('category')
    #     if category:
    #         queryset = self.queryset.filter(category__word=category)
    #         return queryset
    #     return self.queryset


class TagApiView(ListRetrieveView):
    queryset = models.Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = MyPagination
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [AllowAny]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']


class CategoryApiView(ListRetrieveView):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyPagination
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [AllowAny]

