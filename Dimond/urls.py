from django.urls import path
from .views import home_page, predict_datapoint

urlpatterns = [
    path('', home_page, name='home'),
    path('predict/', predict_datapoint, name='predict'),
]
