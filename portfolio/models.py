from django.db import models

# Create your models here.

#setting that framework for adding to our database
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    #if there's no link then the link will not appear
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
