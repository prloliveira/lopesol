from django.urls import include, path
from polls.views import *
urlpatterns = [
    path('', data_collection_view, name='data_collection'),
    path('grafico/', graph_view, name='graph_page'),
    path('bar-chart-data/', bar_chart_data_view, name='bar_chart_data'),
    path("__reload__/", include("django_browser_reload.urls")),
]