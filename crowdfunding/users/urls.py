from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
    path('register/', views.RegisterView.as_view()),
    # path('profile/<int:pk>/', views.ProfileDetail.as_view()),
    path('puns/', views.PunsList.as_view()),
    path('puns/<int:pk>/', views.PunsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)