from app import app
import urllib.request,json
from .model import headlines

Headlines = headlines.Headlines

api_key = app.config['NEWS_API_KEY']
base_url = app.config['HEADLINES_API_BASE_URL']

def get_headlines():
    '''
    
    '''
    get_headlines_url = base_url.format(api_key)
    
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)
        # print(get_headlines_response)
        
        headlines_results = None
        
        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_headlines(headlines_results_list)
            
    return headlines_results
    
def process_headlines(headlines_list):
    
    headlines_results =[]
    for headline_item in headlines_list:
        # name = headline_item.get('name')
        author = headline_item.get('author')
        title = headline_item.get('title')
        description = headline_item.get('description')
        url = headline_item.get('url')
        urlToImage = headline_item.get('urlToImage')
        publishedAt = headline_item.get('publishedAt')
        
        
        if urlToImage and author:
            headlines_instance = Headlines(author, title, description, url, urlToImage, publishedAt)
            # headlines_instance = Headlines(headlines['name'],headlines['author'],headlines['url'],headlines['urlToImage'],headlines['title'],headlines['description'],headlines['publishedAt'])
            headlines_results.append(headlines_instance)
        # print(headlines_instance)
        # print(headlines_results)   
    return headlines_results
        
        
    
    
    