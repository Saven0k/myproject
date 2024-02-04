import datetime
from typing import Any
from django.core.management import BaseCommand

from main.models import Author

class Command(BaseCommand):
    help = 'Creates new users'
    
    def handle(self, *args:Any, **kwargs: Any) -> None:
        for i in range(1, 11):
            author = Author(name=f'Author {i}',
                            last_name=f'Last name {i}',
                            email=f'Email {i}',
                            bio = 'Lorem Ipsum',
                            bithday = datetime.date(2000 ,1,1),
                            )
            self.stdout.write(self.style.ERROR(f'Author {author} created.'))
            author.save()
                            