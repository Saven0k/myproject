from django.db import models

class Coin(models.Model):
    side = models.IntegerField()
    time_game = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Drop {self.side} at {self.time_game}'

    @staticmethod
    def get_data(count):
        coins = Coin.objects.all()[:count]
        coins_dict = {
            'orel': [],
            'reshka': [],
        }
        
        for i in coins:
            if i.side == 0:
                coins_dict['orel'].append(i.time_game)
            else: 
                coins_dict['reshka'].append(i.time_game)
                
        return coins_dict
    
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    bio = models.TextField()
    bithday = models.DateField()
    
    def get_full_name(self):
        return f'{self.last_name} {self.name}'
    
    def __str__(self) -> str:
        return f'Author: {self.last_name}, {self.name}, {self.email}'
    
    
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_of_publish = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.title}, {self.author}, {self.date_of_publish}'