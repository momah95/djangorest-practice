from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HeroView

"""router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewset)"""

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = {
    url(r'^hero/$', HeroView.as_view(), name="hero"),
    #path('api-auth/', include('rest_framework.urls', namespace= 'rest_framework'))
}

urlpatterns = format_suffix_patterns(urlpatterns)