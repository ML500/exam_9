from django.urls import path

from webapp.views.photo_views import IndexView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
]
