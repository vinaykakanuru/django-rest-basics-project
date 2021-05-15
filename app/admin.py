from django.contrib import admin

from app.models import CheckList, CheckListItem

# Register your models here.

admin.site.register(CheckList)
admin.site.register(CheckListItem)
