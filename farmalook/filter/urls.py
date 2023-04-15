from django.urls import path
from filter.views import main_page

app_name = 'filter'

urlpatterns = [
    path('', main_page),
]