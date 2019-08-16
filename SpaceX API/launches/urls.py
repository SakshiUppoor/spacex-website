from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('',views.home,name="home"),
    path('details/',views.details,name="details"),
    path('launches/',views.allLaunches,name="allLaunches"),
    path('launches/<str:category>/<int:no>',views.launches,name="launches"),
    path('launches/past',views.launchesPast,name="launchesPast"),
    path('launches/upcoming',views.launchesUpcoming,name="launchesUpcoming"),
]
