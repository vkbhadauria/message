from django.urls import include, path

urlpatterns = [
	path('', include('message.api.urls'))
]