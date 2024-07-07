from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name="home_page"),
    path('sermons/', views.SermonView.as_view(), name="sermons"),
    path('events/', views.EventView.as_view(), name="events"),
    path('video-sermons/', views.VideoSermonView.as_view(), name="video_sermons"),
]