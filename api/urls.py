from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [

    path('mainmenu/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('mainmenu/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('mainmenu/', views.getCourses),
    path('mainmenu/<str:pk>/', views.getCourse)
    ]

