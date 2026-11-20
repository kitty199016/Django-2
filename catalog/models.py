from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    # Изображения будут сохраняться в папку media/images/
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")

    def __str__(self):
        return self.title
