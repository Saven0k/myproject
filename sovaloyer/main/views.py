from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging
from .models import Coin, Author, Article
from .forms import GameTypeForm, AuthorAddForm, ArticleAddForm
# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
	context = {
		'title': 'Главная страница',
		'content': '<p> Привет, тут информация о том какие мы хорошие <\p>',
	}
    
	logger.info('index get request')
	return render(request, 'main/index.html', context=context)


def about(request):
	context = {
		'title': 'Стрничка о нас',
		'content': '<p> Привет, тут информация о том какие мы хорошие <\p>',
	}
    
	logger.info('about get request')
	return render(request, 'main/about.html', context=context)


def orel_reshka(request, count=3):
	list_res = []
	for _ in range(count):
		list_res.append(choice(['Орел', 'Решка']))	
	context = {
		'title': 'OrelReshka',
		'result': list_res,	
	}	
	logger.info(f'Get {list_res}')
	return render(request, 'main/game.html', context=context)


def random_n(request, count=3):
	list_res = []
	for _ in range(count):
		list_res.append(randint(1, 100))
	context = {
		'title': 'random number',
		'result':list_res,	
	}
	logger.info(f'Get {list_res} ')
	return render(request, 'main/game.html', context=context)


def rubik(request, count=3):
	list_res = []
	for _ in range(count):
		list_res.append(randint(1,6))

	context = {
    	'title': 'rubik',
		'result':list_res,	
	}
	logger.info(f'Get {list_res} ')
	return render(request, 'main/game.html', context=context)


def author_view(request):
    authors = Author.objects.all()
    
    res_str = '<br>'.join([str(author) for author in authors])
    
    return  HttpResponse(res_str)

def articles_view(request):
    articles = Article.objects.all()
    
    res_str = '<br>'.join([str(article) for article in articles])
    
    return HttpResponse(res_str)


def author_article(request, author_id):
    author = Author.objects.get(id=author_id)
    articles = Article.objects.filter(author=author)
    
    context = {
        'title': 'Authors',
		'author': author,
		'articles': articles,
	}
    
    return render(request, 'main/author_article.html', context=context)
    
    
def article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'main/article.html', context={'article': article})


def choose_game(request):
    if request.method == 'POST':
        form = GameTypeForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            throws_number = form.cleaned_data['throws_number']
            logger.info(f'Получили {game_type=} {throws_number=}')
            if game_type == 'C':
                return orel_reshka(request, throws_number)
            elif game_type == 'D':
                return rubik(request, throws_number)
            elif game_type == 'N':
                return random_n(request, throws_number)
                
    else: 
        form=GameTypeForm()
        
    return render(request, 'main/games.html' , {'form' : form})
        
        
def author_add(request):
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        message = 'Ошибка данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            bithday = form.cleaned_data['bithday']
            logger.info(f'Получили {name=}\n {email=}\n {last_name=} \n {bio=} \n {bithday}')
            author = Author(name=name, last_name=last_name,  email=email, bio=bio, bithday=bithday)
            author.save()
            message = 'Автор сохранен'
            
    else: 
        form = AuthorAddForm()
        message = 'Заполните форму'
    
    return render(request, 'main/add_author.html', {'form': form, 'message': message})


def add_article(request):
	if request.method == 'POST':
		form = ArticleAddForm(request.POST)
		message = 'Ошибка данных'
		if form.is_valid():
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			author = form.cleaned_data['author']
			published = form.cleaned_data['is_published']
			date_of_publish = form.cleaned_data['date_of_published']
			category = form.cleaned_data['category']
			logger.info(f'Получили {title=}\n {content=}\n {author=} \n {published=} \n {date_of_publish}')
			article = Article(title=title, content=content, author=author, published=published, date_of_publish=date_of_publish)
			article.save()		
			message = 'Статья сохранена'
            
	else: 
		form =  ArticleAddForm()
		message = 'Заполните форму'
    
	return render(request, 'main/add_article.html', {'form': form, 'message': message})