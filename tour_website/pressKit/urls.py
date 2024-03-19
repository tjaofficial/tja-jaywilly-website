from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_view, name="landing"),
    path("tour-dates", views.tour_dates_view, name="tourDates"),
    path("tour-dates/<str:showName>", views.view_shows_view, name="viewShow"),
    path("artist/<str:artistName>", views.artist_page_view, name="artistPage"),
    path("artist-tjaofficial", views.tjaofficial_view, name="tja"),
    path("artist-jaywilly", views.jaywilly_view, name="jay"),
    path("setup/add-shows", views.add_shows_view, name="addshows"),
]