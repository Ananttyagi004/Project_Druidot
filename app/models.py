from django.db import models
import os
def rename_image(instance, filename):
    upload_to = 'person_images/'
    ext = filename.split('.')[-1]
    # get the name of the person and replace spaces with underscores
    name = instance.email.replace(' ', '_')
    # set the filename as <name>.jpg
    filename = '{}.{}'.format(name, 'jpg')
    return os.path.join(upload_to, filename)

class Person(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField(upload_to=rename_image, null=True, blank=True)

    def __str__(self):
        return self.name
