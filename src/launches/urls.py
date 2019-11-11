from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [ 
    path('',views.home,name="home"),
    path('launches/',views.allLaunches,name="allLaunches"),
    path('launches/<str:category>/<int:no>',views.launches,name="launches"),
    path('launches/past',views.launchesPast,name="launchesPast"),
    path('launches/upcoming',views.launchesUpcoming,name="launchesUpcoming"),
    path('missions/',views.allMissions,name="allMissions"),
    path('missions/<int:no>',views.missions,name="missions"),
    path('cores/',views.allCores,name="allCores"),
    path('cores/<int:no>',views.cores,name="cores"),
    path('rockets/',views.allRockets,name="allRockets"),
    path('rockets/<int:no>',views.rockets,name="rockets"),
]
