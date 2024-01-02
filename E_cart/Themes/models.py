from django.db import models

# Models for themes
class SiteSettings(models.Model):
    banner=models.ImageField(upload_to='/media/site')
    caption=models.TextField()
