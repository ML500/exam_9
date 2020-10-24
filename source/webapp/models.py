from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to='user_pics', verbose_name='Картинка')
    sign = models.CharField(max_length=100, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='photos',
                               verbose_name='Автор')

    def __str__(self):
        return self.sign

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


# class Favorites(models.Model):
#
