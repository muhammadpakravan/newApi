# NewsApi
simple application for news with Django and Django-rest-framwork 


## list of all valid get requests
    #get all Articles
    get('api/Article')
    
    # get on query based on pk
    get("api/Article/<int:pk>/")
    
    # get all category lists
    get("api/category/")
    
    # get all articles based on category 
    get("api/category/<str:category>/")
    
    # get all of source list
    get ("api/source/")
    
    # get  articles based on sorce 
    get("api/source/<str:source>")
    
    # filter with source and category
    path("api/filter/<str:source>/<str:category>")
    
    # search based on title and content of articles
    path("api/search/<str:search>")
        
