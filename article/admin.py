from django.contrib import admin
from article.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	"""docstring for ArticleAdmin"""
	list_display = ('title','category','date_time')
	list_filter = ('date_time',)
	search_fields = ('category',)

admin.site.register(Article)
