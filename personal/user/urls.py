from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from user import views
from django.urls import path


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/verify/', views.VerifyView.as_view(), name='token_verify'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
]
