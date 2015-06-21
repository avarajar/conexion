from django.contrib import admin
from .models import *

# class ColorAdmin(admin.ModelAdmin):
#     list_display = ('id', 'nombre',)
#     list_filter = ('nombre',)
#     #list_editable = ('color',)
#     search_fields = ('nombre', )

admin.site.register(Co_Creadore)
admin.site.register(Tag)
admin.site.register(Dinamica)
admin.site.register(Reto)
