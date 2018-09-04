from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from	django.template.loader	import	render_to_string
from	django.utils.safestring	import	mark_safe
# Create your models





class Activity(models.Model):
    name=models.CharField(max_length=23)
    # slug=models.CharField(max_length=40)
    description=models.TextField(max_length=7000)
    date_happen=models.DateField()
    image=models.ImageField()
    # video = EmbedVideoField()
    # def	render(self):
    #     return	render_to_string('app/content/{}.html'.format(self._meta.model_name),	{'activity': self})
    video= models.FileField(upload_to='videos/tigo')
