from django.urls import path, include
from .views import EventList, DetailEvent

urlpatterns = [
	path('<int:pk>/', DetailEvent.as_view(), name='detailevent'),
	path('', EventList.as_view(), name='eventlist'),
]