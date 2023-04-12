from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('contributor', 'post_text', 'created_at')
    orderring = ('-created_at')
    list_filter = ('contributor',)


admin.site.register(Post, PostAdmin)
