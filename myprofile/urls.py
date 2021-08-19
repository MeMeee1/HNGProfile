from django.urls import path
from .views import Postview, Thankview
urlpatterns = [
	path('', Postview.as_view(), name='home'),
	path('response/', Thankview.as_view(), name='response'),
    ]