from django.urls import path
from .views.home_view import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='hello_world'),  # ルートURLにマッピング
]