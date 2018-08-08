from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp"]
	list_display_links = ["timestamp"]
	list_filter = ["timestamp"]
	list_editable = ["title"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)