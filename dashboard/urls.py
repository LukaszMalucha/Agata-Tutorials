from django.urls import path, include
from dashboard.views import dashboard


urlpatterns = [
    path('', dashboard, name="dashboard"),

]


