from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from webapp.models import Photo, AddFavorite


class AddToFavorite(APIView):
    def post(self, request, *args, **kwargs):
        author = request.user
        photo = get_object_or_404(Photo, pk=kwargs['pk'])
        favorite = AddFavorite.objects.get_or_create(author=author, photo=photo)


class RemoveFavorite(APIView):
    def delete(self, request, *args, **kwargs):
        author = request.user
        photo = get_object_or_404(Photo, pk=kwargs['pk'])
        favorite = AddFavorite.objects.get_or_create(author=author, photo=photo)




