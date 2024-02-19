from django.db import models

# Create your models here.
class UserProfile(models.Model):
    image = models.ImageField(upload_to="images") # files are stored in hard disk. Just the path is stored in database.
# ImageField()