from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import ensure_csrf_cookie
from webapp.models import Photo, Favorite
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator


class AddToFavorite(APIView):
    @method_decorator(ensure_csrf_cookie)
    def post(self, request, pk=None):
        photo = get_object_or_404(Photo, pk=pk)
        created = Favorite.objects.get_or_create(photo=photo, user=request.user)
        if created:
            photo.save()
            return Response({'pk': pk})
        else:
            return Response(status=403)


class RemoveFavorite(APIView):
    @method_decorator(ensure_csrf_cookie)
    def delete(self, request, pk=None):
        favorites = get_object_or_404(Favorite, photo_id=pk, user=request.user)
        print(favorites)
        favorites.delete()
        return Response({'pk': pk})
