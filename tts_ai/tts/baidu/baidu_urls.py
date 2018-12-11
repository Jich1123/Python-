from django.conf.urls import url
from . import views
app_name ='[baidu]'
urlpatterns = [
    url(r'^tts/', views.index, name='tts'),
    url(r'^action/$', views.tts_action, name='tts_action'),
    url(r'^play/$', views.play, name='play'),
]