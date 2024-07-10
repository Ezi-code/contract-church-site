from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home_page"),
    path("sermons/", views.SermonView.as_view(), name="sermons"),
    path("events/", views.EventView.as_view(), name="events"),
    path("video-sermons/", views.VideoSermonView.as_view(), name="video_sermons"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("register-event/", views.RegisterEventView.as_view(), name="register_event"),
    path(
        "newsletter-sub/", views.SubsribeNewsLetterView.as_view(), name="newletter_sub"
    ),
]
