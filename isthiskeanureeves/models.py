from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models



class Category(models.Model):
      name = models.CharField(max_length=128, unique=True)
      slug = models.SlugField(unique=True)
      
      #img = models.CharField(max_length=64, unique=True)

      def save(self, *args, **kwargs):
           self.slug = slugify(self.name)
           super(Category, self).save(*args, **kwargs)

      class Meta:
           verbose_name_plural = 'Categories'

      def __str__(self):
           return self.name
		   
		   

def user_upload(instance, filename):
    return 'user_{0}/{1}'.format(instance.user, filename)
        
class Page(models.Model):
      category = models.ForeignKey(Category)
      title = models.CharField(max_length=128)
      user = models.ForeignKey(User)
      rating = models.IntegerField(default = 0)
      image = models.ImageField(default = "null",upload_to=user_upload)
      date_added = models.DateTimeField(auto_now_add=True)
      
	  
      def __str__(self): # For Python 2, use __unicode__ too
           return self.title

class UserProfile(models.Model):
   
    user = models.OneToOneField(User)
    #website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
   
    def __str__(self):
        return self.user.username
