from django.db import models

# Create your models here.
class Data(models.Model):
    preview_image = models.ImageField(upload_to='data_images')
    title         = models.CharField(max_length=50)
    description   = models.TextField()
    data_file     = models.FileField(upload_to='data-file')

    def __str__(self):
        return self.title