from django.contrib import admin

from posts.models import Comment, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)


class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    ordering = ('text',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = (PostInline,)
    ordering = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'text', 'author')
    ordering = ('text',)
    search_fields = ('created', 'text')


admin.site.empty_value_display = '-пусто-'
