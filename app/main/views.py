from flask import render_template, redirect, url_for, request
from . import main
from ..models import News, Article
from ..request import get_sources,get_article


@main.route ('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    popular_general = get_sources('general')
    upcoming_category = get_sources('business')
    now_showing_category = get_sources('sports')
    title = 'Home - Welcome to The best News Review Website Online'


    return render_template('index.html', title = title,popular=popular_general, upcoming =upcoming_category, now_showing = now_showing_category )


@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the article details page and its data
    '''
    article = get_article(id)
    title = f'{id}'

    return render_template('article.html',title = title,articles= article)


   