from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# API endpoints
# The API URLs aew now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]
