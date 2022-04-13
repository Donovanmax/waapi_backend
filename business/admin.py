from django.contrib import admin
from .models import Business, Detail, Images, Type, Comment, Account
# Register your models here.

admin.site.register(Business)
admin.site.register(Detail)
admin.site.register(Account)




admin.site.register(Type)
admin.site.register(Images)
admin.site.register(Comment)

