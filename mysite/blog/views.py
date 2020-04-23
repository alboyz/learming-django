from django.shortcuts import HttpResponse
from blog.models import News

def Index(request):
    return HttpResponse("<h1>Hello, world. You're at the blog index.</h1>")

def Home (request):
    return HttpResponse("<h1>This is a Home Page</h1>")

def Contact (request):
    return HttpResponse ("<h1>This is a Contact Page</h1>")

def Crud (request):
    #create
    datNews = News(
        author = 'Ali',
        title = 'Ali Title',
        description = 'lorem lipsum gfgfgre5' 
    )
    datNews.save()

    #Read    
    objects = News.objects.all()

    res = 'Print All Data <br>'
    
    for do in objects:
        res +='Author is'+ do.author+'<br>'
        res +='Tittle is'+ do.title+'<br>'
        res +='Description is'+ do.description+'<br>'
        
    #update
    res += 'upadte author Ali to Taufiq <br>'
    do = News.objects.get(author = 'Ali')
    do.author = 'Taufiq'
    do.save()
    
    #DELETE
    res += 'Delete Author Taufiq'
    do = News.objects.get(author = 'Taufiq')
    do.delete()
    return HttpResponse(res)