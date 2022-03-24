from django.contrib import admin
from api_project import models


admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
# Register your models here.
