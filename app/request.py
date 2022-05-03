import urllib.request,json
from .models import Headlines,Sources

# Headlines = headlines.Headlines
# Sources = headlines.Sources

api_key = None
base_url = None
# source_url = None

def configure_request(app):
    global api_key,base_url,source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['HEADLINES_API_BASE_URL']
    source_url = app.config['SOURCES_URL']

def get_headlines():
    '''
    method to get all the headlines
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
    '''
    function to process the acquired headlines
    '''
    
    headlines_results =[]
    for headline_item in headlines_list:
        source = headline_item.get('source')
        author = headline_item.get('author')
        title = headline_item.get('title')
        description = headline_item.get('description')
        url = headline_item.get('url')
        urlToImage = headline_item.get('urlToImage')
        publishedAt = headline_item.get('publishedAt')
        
        
        if urlToImage and author and description:
            headlines_instance = Headlines(source,author, title, description, url, urlToImage, publishedAt)
            # headlines_instance = Headlines(headlines['name'],headlines['author'],headlines['url'],headlines['urlToImage'],headlines['title'],headlines['description'],headlines['publishedAt'])
            headlines_results.append(headlines_instance)
        # print(headlines_instance)
        # print(headlines_results)   
    return headlines_results
        
def get_sources():
    '''
    function to sources
    '''
    get_sources_url = source_url.format(api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        # print(get_headlines_response)
        
        sources_results = None
        
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
            
    return sources_results

def process_sources(sources_list):
    '''
    create method to process fetched sources
    '''    
    sources_results =[]
    for sources_item in sources_list:
        
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        
        if description and name :
            sources_instance = Sources(name,description, url)
            sources_results.append(sources_instance)  
            
    return sources_results
    
        
     
    
    
    