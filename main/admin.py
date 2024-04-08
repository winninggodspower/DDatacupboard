from django.contrib import admin
from .models import Data, Feedback

# make admins ui changes
admin.site.site_header = 'DataCupboard Admin'
admin.site.site_title = 'DataCupboard Admin Panel'

# Register your models here.
admin.site.register(Data)
admin.site.register(Feedback)
