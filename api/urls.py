from django.urls import path, include
from api.views import PingPongView, LinksRetrieveUpdateDestroyView, LinksListCreateView

urlpatterns = [
    path("ping/", PingPongView.as_view()),
    path("links/<pk>", LinksRetrieveUpdateDestroyView.as_view()),
    path("links/", LinksListCreateView.as_view()),
]
