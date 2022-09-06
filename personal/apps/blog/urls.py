from rest_framework import routers
from apps.blog import views
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()

router.register('blog', views.BlogApiView, basename='blog')
router.register('category', views.CategoryApiView, basename='category')
router.register('tag', views.TagApiView, basename='tag')
# router.register('User', views.UserApiView, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
