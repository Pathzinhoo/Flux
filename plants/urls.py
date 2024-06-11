from .views import plantingResum
from django.urls import path

urlpatterns = [
    path('resum/', plantingResum)
]
