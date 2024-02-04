import datetime
from typing import Any
from django.core.management import BaseCommand

from main.models import Author
from django.core.management.base import CommandParser


class Command(BaseCommand):
    help = 'Delete authors'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('id', type=int, help='Author id to delete')
        
    def handle(self, *args, **kwargs) -> str | None:
        id = kwargs['id']
        
        author = Author.objects.filter(pk=id).first()
        
        author.delete()
        self.stdout.write(self.style.ERROR(f'Deleted author {author}'))
        