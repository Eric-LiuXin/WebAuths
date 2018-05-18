from django.contrib import admin

# Register your models here.

from .models import User, UserAuths

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')

class UserAuthsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'indentifer')

admin.site.register(User, UserAdmin)
admin.site.register(UserAuths, UserAuthsAdmin)
