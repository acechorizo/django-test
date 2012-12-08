from django.contrib import admin
from sizetemplatemap.models import CreativeSize, CreativeTemplate, CreativeSizeTemplateRel

class CreativeTemplateInline(admin.TabularInline):
    model = CreativeSizeTemplateRel

class CreativeSizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','height','width','status','insertDate','updateDate','bufferName')
    fieldsets = [
        (None,               {'fields': ['name','description','height','width','status','bufferName']}),
    ]
    inlines = [CreativeTemplateInline]
    list_filter = ['updateDate']
    search_fields = ['name','width','height']

admin.site.register(CreativeSize, CreativeSizeAdmin)