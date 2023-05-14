from django.urls import path
from filter.views import main_page, SearchResults

app_name = 'filter'

urlpatterns = [
    path('search/', SearchResults.as_view(), name='search_results'),
    path('', main_page, name='main_page'),
]