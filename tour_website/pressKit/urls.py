from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_view, name="landing"),
    path("tour-dates", views.tour_dates_view, name="tourDates"),
    path("setup/add-shows", views.add_shows_view, name="addshows"),
]