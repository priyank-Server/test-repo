from rest_framework import routers
from apps.snippet import views

router = routers.DefaultRouter()

router.register('', views.SnippetView, basename='snippet')
urlpatterns = router.urls
