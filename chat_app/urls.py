from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', TemplateView.as_view(template_name='chat_app/home.html'), name='home'),
    # path('(?P<room_name>[^/]+)',views.room, name='room')
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]