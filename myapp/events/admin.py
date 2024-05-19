from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import UserCreation, Post, Image, Article,Speaker
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import redirect
from django.utils.html import format_html


class ResearcherSite(AdminSite):
    site_header = 'Researcher Site'
    site_title = 'Researcher Site'

    def logout(self, request):
        logout(request)
        return redirect(reverse('index'))


researcher_site = ResearcherSite(name='researcher')
admin.site.site_header = 'Super Admin Site'
admin.site.site_title = 'Super Admin Site'

researcher_site.register(UserCreation)
admin.site.register(UserCreation)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
class SpeakerInline(admin.TabularInline):
    model = Speaker
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline, SpeakerInline]
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    exclude = ['images']  # Exclude the images field

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        images = request.FILES.getlist('images')
        for image in images:
            Image.objects.create(post=obj, image=image)

class ArticleInline(admin.StackedInline):
    model = Article
    can_delete = False
    readonly_fields = ('get_article_title',)
    list_display = ('get_article_title', 'article_type')
    def get_article_title(self, obj):
        if obj.title_link:
            return format_html('<a href="{}" target="_blank">{}</a>', obj.title_link, obj.title)
        else:
            return obj.title

    get_article_title.short_description = 'Title'

admin.site.register(Post, PostAdmin)  
researcher_site.register(Post, PostAdmin)
admin.site.register(Article)
researcher_site.register(Article)








