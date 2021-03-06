from django.contrib import admin
from blog.models import Category, Post, UserProfile, Comment, Page

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'category', 'author', 'status')
	search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "created"]

admin.site.register(Comment, CommentAdmin)
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)