from django.db import models
from django.conf import settings
from django.utils.text import slugify



# Create your models here.

class Image(models.Model):
    #user:   The User object that bookmarked this image. This is a ForeignKey
    #        field because it specifies a one-to-many relationship: A user can post multiple
    #        images, but each image is posted by a single user.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created')
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    
    #created: The datetime that indicates when the object has been created in
    #        the database. Since we use auto_now_add, this datetime is automatically set
    #        when the object is created. We use db_index=True so that Django creates
    #        an index in the database for this field.
    created = models.DateField(auto_now_add=True, db_index=True)
    
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked',
                                       blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **Kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Image, self).save(*args, **Kwargs)
            
        #In this code, we use the slufigy() function provided by Django to automatically
        #generate the image slug for the given title when no slug is provided. Then, we save
        #the object. We will generate slugs for images automatically so that users don't have
        #to enter a slug for each image.
    
    