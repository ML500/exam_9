from django.urls import path

from api.views import AddToFavorite, RemoveFavorite

app_name = 'api'

urlpatterns = [
    path('add/<int:pk>/', AddToFavorite.as_view(), name='add'),
    path('remove/<int:pk>/', RemoveFavorite.as_view(), name='remove'),

]