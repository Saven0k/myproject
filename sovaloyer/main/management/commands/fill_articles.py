import datetime
from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from main.models import Article

class Command(BaseCommand):
    help = 'Creates new articles'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('count', type=int, help='Number of articles to create ')
        
    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        count = kwargs['count']
        
        authors = Author.objects.all()
        
        for author in authors:
            for i in range(count):
                article = Article (
                    title = f'Title {i}',
                    content = f'Content {i}',
                    author=author,
                )
                
                self.stdout.write(self.style.SUCCESS(f'Creater article'))
                article.save()
    