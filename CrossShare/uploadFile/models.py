from django.db import models

from CrossShare.settings import BASE_DIR, MEDIA_ROOT

# Create your models here.
class uploadFile(models.Model):
    
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to=MEDIA_ROOT,null=True)
    created_at = models.CharField(max_length=30)

    def __str__(self):
            return self.title