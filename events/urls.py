from django.urls import path, include
from .views import EventList, DetailEvent, bodyText

urlpatterns = [
	path('text/<int:pk>/', bodyText, name='bodyText'),
	path('<int:pk>/', DetailEvent.as_view(), name='detailevent'),
	path('', EventList.as_view(), name='eventlist'),
]