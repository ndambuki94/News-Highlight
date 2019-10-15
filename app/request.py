from app import app
import urllib.request,json
from .models import news,article

Article=article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

News = news.News

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
article_base_url=app.config['ARTICLE_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)
            
    return source_results



