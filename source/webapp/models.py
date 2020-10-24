from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    picture = models.ImageField(upload_to='user_pics', verbose_name='Картинка')
    sign = models.CharField(max_length=100, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='photos',
                               verbose_name='Автор')

    def __str__(self):
        return self.sign

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ["-created_at"]


class Favorite(models.Model):
    photo = models.ForeignKey('webapp.Photo', on_delete=models.CASCADE,
                              related_name='photo_fav', verbose_name='Фото')
    user = models.ForeignKey(get_user_model(), related_name='user_fav',
                             verbose_name='Пользователь', on_delete=models.CASCADE)


class AddFavorite(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='user_add',
                             verbose_name='Пользователь', on_delete=models.CASCADE)
    photo = models.ForeignKey('webapp.Photo', on_delete=models.CASCADE,
                              related_name='photo_add', verbose_name='Фото')

    def __str__(self):
        return f'{self.user.username} - {self.photo.sign}'

    class Meta:
        verbose_name = 'Добаленить в избранное'
        verbose_name_plural = 'Добаление в избранное'
