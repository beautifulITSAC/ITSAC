from django.urls import path, re_path
from apps.ITSAC_WEB.views import views

urlpatterns = [
    # index
    path('', views.index, name='index'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]