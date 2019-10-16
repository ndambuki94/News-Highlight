import urllib.request
import json
from .models import News, Article
from datetime import datetime

api_key = None
base_url = None
article_base_url = None


def config_requests(app):
    global api_key, base_url, article_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]
    article_base_url = app.config['ARTICLE_API_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            article_result_list = get_sources_response['sources']
            source_results = process_results(article_result_list)
            # source_results = (source_results_list)

    return source_results


def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if id:
            source_object = News(id, name, description, url,
                                 category, language, country)
            source_results.append(source_object)

    return source_results


def get_article(id):
    get_article_details_url = article_base_url.format(id, api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_results = None

        if article_details_response['articles']:
            article_results_list = article_details_response['articles']
            article_results = process_result(article_results_list)

    return article_results


def process_result(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain source details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage =article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if id:
            article_object = Article(author, title, description, url, urlToImage, publishedAt, content)
            article_results.append(article_object)


    return article_results



