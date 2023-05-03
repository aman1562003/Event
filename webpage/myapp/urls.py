
from . import views
from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet, login_view 
 
app_name = 'webpage'
# router = routers.DefaultRouter()
# router.register(r'events', EventViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('events/', views.EventViewSet.as_view({'get': 'list'})),
    path('api/login/', views.login_view),
    path('api/register/', views.register, name='register'),
]
