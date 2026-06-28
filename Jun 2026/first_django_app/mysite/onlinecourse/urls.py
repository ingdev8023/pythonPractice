from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.course_list, name='course_list'),
    path(route="date", view=views.get_date, name='date')
]