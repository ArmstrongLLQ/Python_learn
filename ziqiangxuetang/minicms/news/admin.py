from django.contrib import admin
from .models import Article, Column

# Register your models here.
class ColumnAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'intro')

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'pub_date', 'update_time')

	class Media:
		js = (
			'/static/js/kindeditor-4.1.10/kindeditor-min.js',
			'/static/js/kindeditor-4.1.10/lang/zh_CN.js',
			'/static/js/kindeditor-4.1.10/config.js',
			)

admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)