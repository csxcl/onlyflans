import uuid
from django.db import models
# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=50)
    description = models.TextField ()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    favorite = models.BooleanField()


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    costumer_email = models.EmailField()
    costumer_name = models.CharField(max_length=30)
    message = models.TextField()