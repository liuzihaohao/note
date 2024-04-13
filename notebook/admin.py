from django.contrib import admin
from .models import *

# Register your models here.

class NoteConAdmin(admin.ModelAdmin):
	list_display = ['id','content']
	list_display_links = ['id']
	search_fields = ['id','content']
admin.site.register(NoteCon,NoteConAdmin)

admin.site.site_title="Note"
admin.site.site_header="Note"