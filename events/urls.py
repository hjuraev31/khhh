from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
	EventList, 
	DetailEvent, 
	DeleteDataBase, 
	ImgList, 
	ImageAPIView,
	TgUsers,
	post_data,
	studimg,
	bodyText, 
	byName, 
	delApi,
)

urlpatterns = [
	path('name/<str:name>/', byName, name='FilterByName'),
	path('text/<int:pk>/', bodyText, name='bodyText'),
	path('<int:pk>/', DetailEvent.as_view(), name='detailevent'),
	path('deleteDataBase/',delApi, name='deleteDB'),
	path('img/', ImgList.as_view(), name='save_img'),
	path('showimg/<int:id>/', ImageAPIView.as_view(), name='img_api_id'),
	path('studentimg/<str:name>/', studimg, name='filterByName'),
	path('v2/showimg/',post_data,name='post_img'),
	path('tgusers/', TgUsers.as_view(), name='tg_users'),
	path('', EventList.as_view(), name='eventlist'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
