from django.contrib import admin

# Register your models here.
from blog.models import *

class ArticleAdmin(admin.ModelAdmin):
	field = ('title', 'desc', 'comment',)
	list_display = ('title', 'desc', 'click_count')


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
