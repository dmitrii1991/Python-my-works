from django.contrib import admin
from .models import Bd, Rubric

class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')  # вывод полей
    list_display_links = ('title', 'content')  # ссылки на правку
    search_fields = ('title', 'content')  # фильтр

admin.site.register(Bd, BdAdmin)
admin.site.register(Rubric)

