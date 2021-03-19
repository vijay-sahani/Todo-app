from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('save',views.saveReminder),
    path('delete/<int:id>',views.deleteReminder),
    path('update/',views.updateReminder),
]