"""定义learning_logs的url模式"""

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),

    path('topics/', views.topics, name='topics'),

    path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),

    path('new_topic/', views.new_topic, name='new_topic'),

    path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),

    path('edit_entry/(?P<entry_id>\id+)/', views.edit_entry, name='edit_entry'),

]
app_name = 'learning_logs'