
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    body = RichTextUploadingField(null=True, config_name="default", )
     

    def __str__(self):
        return self.name
    