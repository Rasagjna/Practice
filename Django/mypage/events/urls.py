from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    # path("getEvents", views.getEventsDetails),
    # path("getEvent",views.getEventFromEventType),
    path("",views.EventsapiOverView,name="apiOverview"),
     path("upcomingEvents/",views.getUpcomingEvents,name="upcomingEvents"),
    path('eventsList/',views.getEventsDetails,name='event-list'),
    path('eventsCreate/',views.createEvents,name='create-events'),
    path('eventsDelete/<int:pk>/',views.deleteEvents,name='delete-events'),
    path('eventsUpdate/<int:pk>/',views.updateEvents,name="update-events") ,
    path('eventTypes/',views.getEventTypes,name="getEventTypes"),
    path('getWorkshops/',views.getWorkshops,name="get-workshops"),
    path('upcomingWorkshops/',views.getUpcomingWorkshops,name="upcoming-workshops"),
    path('createWorkshops/',views.createWorkshops,name="create-workshops"),
    path('deleteUpdateWorkshops/<int:pk>/',views.deleteAndUpdateWorkshops,name="update-delete"),
    path('getSports/',views.getSports,name='get-sports'),
    path('createSports/',views.createSports,name="create-sports"),
    path('deleteAndUpdateSports/<int:pk>/',views.deleteAndUpdateSports,name="delete-update-sports"),
    path('emailsending/',views.send_mail_plain_with_file,name="send-mail"),
    path("postfile/",views.readfiles,name="my-file"),
    path("getfile/<int:pk>",views.getfile),
    path('register/',views.CustomUserCreate.as_view(),name="custom-user")
    ,path('logout/blacklist/',views.BlacklistTokenUpdateView.as_view(),name="blacklist"),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path("getEventsByLocation/<int:emp_id>",views.getEventsByLocation,name="events-by-location")
    
]
