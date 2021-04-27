from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    readonly_fields = ['created_on']

    def approve_comments(self, queryset):
        queryset.update(active=True)
