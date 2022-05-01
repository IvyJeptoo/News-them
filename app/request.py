from app import app
import urllib.request,json
from .model import news

News = news.News

api_key = app.config['NEWS_API_KEY']
base_url = app.config['HEADLINES_API_BASE_URL']

def get_headlines():
    get_headlines_url = base_url.format(api_key)
    
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.load(get_headlines_data)
        
        headlines_results = None
        
        if get_headlines_response['totalResults']:
            headlines_results_list = get_headlines_response['totalResults']
            headlines_results = process_results(headlines_results_list)
            
    return headlines_results
    
def process_results(headlines_list):
    
    headlines_results =[]
    for item in headlines_list:
        name = item.get('name')
        author = item.get('author')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        title = item.get('title')
        description = item.get('description')
        publishedAt = item.get('publishedAt')
        
        if urlToImage:
            headlines_object = News(name,author,url,urlToImage,title,description,publishedAt)
            headlines_list.append(headlines_object)
            
    return headlines_results
        
        
    
    
    