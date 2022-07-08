from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('hashed_url', 'original_link')
    link_display = ('hashed_url', )
    search_fields = ('hashed_url', 'original_link')


admin.site.register(Link, LinkAdmin)
