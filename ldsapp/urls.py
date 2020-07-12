from . import views
from rest_framework import routers
from django.urls import path, include

# the router object
router = routers.DefaultRouter()

# add urls
router.register(r'lds', views.UserView, 'Lds Info')

# all urls that can be visited
urlpatterns = [
    path('', include(router.urls)),
]
