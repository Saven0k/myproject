from django.contrib import admin
from .models import Article, Author, Coin
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'bithday']
    ordering = ['name', '-bithday']
    list_filter = ['name', 'bithday']
    search_fields = ['name']
    search_help_text = 'Поиск по полю имя автора(name)'
    
    readonly_fields = ['bithday']
    
    fieldsets = [
        (
            'Author',
            {
                'classes':['wide'],
                'fields':['name', 'last_name']
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description':'Биография автора',
                'fields': ['bithday','bio'],
            },
        ),
        (
            'Other',
            {
                'description': 'Контактная информация',
                'fields': ['email'] 
            }
        )
    ]
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'date_of_publish', 'author']
    ordering = ['title', '-date_of_publish']
    list_filter = ['title', 'author']
    search_fields = ['title']
    search_help_text = 'Поиск по полю название статьи'
    
    @admin.action(description="Удалить все посты у автора")
    def delete_all_articles(modeladmin, request, queryset):
        queryset.update(content='')

    actions = [delete_all_articles]
        
    readonly_fields = ['published'] 
    fieldsets = [
        (
            'Author',
            {
                'classes':['wide'],
                'fields':['title', 'content']
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description':'Автор ',
                'fields': ['author'],
            },
        ),
        (
            'Other',
            {
                'description': 'Прочая информация',
                'fields': ['published', 'views'] 
            }
        )
    ]
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Coin)


