from statistics import mode
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models import Q

from rest_framework.authtoken.models import Token
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver



# class User(AbstractUser):
#    _id = models.AutoField(primary_key=True, verbose_name='id')
#    email = models.EmailField(unique=True)
#    username = models.CharField(max_length=45, unique=True)
#    phone = models.CharField(max_length=20, )
#    date_joined = models.DateTimeField(auto_now_add=True)   
#    last_login = models.DateTimeField(auto_now=True)
#    is_admin = models.BooleanField(default=False)
#    is_active = models.BooleanField(default=True)
#    profile_img = models.ImageField(upload_to=f'uploads/Users/{_id}', null=True, blank=True)


#    USERNAME_FIELD = 'email'
   
#    REQUIRED_FIELDS = []
   
#    def __str__(self):
#        return self.username


#    def get_image(self):
#         if self.image:
#             return 'http://127.0.0.1:8000' + self.profile_img.url
#         return ''

host = 'https://48ae-102-129-82-191.ngrok.io'
def upload_to(instance, filename):
    return 'uploads/users/{filename}'.format(filename=filename)

class Account(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name='id')
    username = models.CharField(max_length=255, unique=True)
    contact = models.CharField(max_length=255, unique=True)
    external_pic = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField(upload_to=upload_to)
    date_joined = models.DateField(auto_now=True)
    active = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.username
    
    def natural_key(self):
        return self.username
    
    
    def get_image(self):
        if self.picture:
            return host + self.picture.url
        return ''

    
    
class Type(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name='id')
    types = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.types
    
    def natural_key(self):
        return self.types

class Comment(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name='id')
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Account, related_name = 'comment_owner', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.body[:50]
    
    def natural_key(self):
        return self.body[:15]
    
    
class Images(models.Model):
      _id = models.AutoField(primary_key=True, verbose_name='id')
      businessName = models.CharField(max_length=100, blank=True, null=True) 
      image2 = models.ImageField(upload_to='uploads/business/', blank=True, null=True)
      image3 = models.ImageField(upload_to='uploads/business/', null=True, blank=True)  
      image4 = models.ImageField(upload_to='uploads/business/', null=True, blank=True) 
      
      def __str__(self): 
          return self.businessName
      
      
      def save(self, *args, **kwargs):
          super().save(*args, **kwargs)
          img2 = Image.open(self.image2.path)
          img3 = Image.open(self.image3.path)
          img4 = Image.open(self.image4.path)
        
          if img2.height > 2500 or img2.width > 2500:
            output_size = (img2.height-1500, img2.width-1500)
            img2.thumbnail(output_size)
            img2.save(self.image2.path)
            
          if img3.height > 2500 or img3.width > 2500:
            output_size = (img3.height-1500, img3.width-1500)
            img3.thumbnail(output_size)
            img3.save(self.image3.path)
        
          if img4.height > 2500 or img4.width > 2500:
            output_size = (img4.height-1500, img4.width-1500)
            img4.thumbnail(output_size)
            img4.save(self.image4.path)
        
            

      def get_image2(self):
         if self.get_image2:
            return host + self.image2.url
         return ''
    
      def get_image3(self):
         if self.image3:
            return host + self.image3.url
         return ''
     
      def get_image4(self):
         if self.image4:
            return host + self.image4.url
         return ''
    
      

    
class Business(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='uploads/business/')
    carousel = models.ForeignKey(Images, related_name='carousel_img', blank=True, on_delete=models.CASCADE, null=True)
    contact_tel = models.CharField(max_length=80, blank=True, null=True)
    website = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    description = models.CharField(max_length=255,blank=True, null=True)
    comments = models.ManyToManyField(Comment,  related_name = 'comment', blank=True)
    liked = models.ManyToManyField(Account, related_name = 'likes', blank=True)
    type = models.ForeignKey(Type, related_name='genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    visited = models.ManyToManyField(Account, related_name = 'visitors', blank=True)
    ville = models.CharField(max_length=255, blank=True, null=True)
    adress = models.CharField(max_length=255, blank=True, null=True)
    quartier = models.CharField(max_length=255, blank=True)
    arrondissement  = models.CharField(max_length=255, blank=True)
    rate = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    to_be_visited = models.ManyToManyField(Account, related_name = 'favourites', blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name
    
    def natural_key(self):
        return self.name
    
    
    @property
    def numbers_likes(self):
        return self.liked.all().count()

    def get_absolute_url(self):
        return f'/{self.slug}/'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        
        if img.height > 2500 or img.width > 2500:
            output_size = (img.height-1500, img.width-1500)
            img.thumbnail(output_size)
            img.save(self.image.path)
               

    def get_image(self):
        if self.image:
            return host + self.image.url
        return ''




LIKE_CHOICES = {
    
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
}
    

class Detail(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name='id')
    business_id = models.ForeignKey(Business, related_name='details', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='uploads/details', null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    prix = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    livraison = models.BooleanField(default=False)
    tested = models.ManyToManyField(Account, related_name = 'vu', blank=True)

    class Meta:
        ordering = ('-prix',) 

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name
    
    
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        
        if img.height >2500 or img.width > 2500:
            output_size = (img.height-2000, img.width-2000)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_image(self):
        if self.image:
            return host + self.image.url
        return ''
    
    # def get_thumbnail(self):
    #     if self.thumbnail:
    #         if self.thumbnail:
    #             return 'http://127.0.0.1:8000' + self.thumbnail.url
    #         else:
    #             if self.image:
    #                 self.thumbnail = self.make_thumbnail(self.image)
    #                 self.save()
    #
    #                 return 'http://127.0.0.1:8000' + self.thumbnail.url
    #             else:
    #                 return ''
    #
    #
    # def make_thumbnail(self, image, size=(300, 200)):
    #     img = Image.open(image)
    #     img.convert('RGB')
    #     img.thumbnail(size)
    #
    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'JPEG', qualilty=90)
    #
    #     thumbnail = File(thumb_io, name=image.name)
    #     return thumbnail