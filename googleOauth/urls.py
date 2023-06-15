from django.urls import path, include

from . import views


urlpatterns = [
	path('', index, name='index'),
	path('redirect/', RedirectOauthView),
    path('callback/', CallbackView),
]
