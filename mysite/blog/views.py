from django.shortcuts import HttpResponse, render

from .models import News


def Index(request):
    context = {
        "name": "Ali"
    }

    return render(request, "index.html",  context)


def Home(request):
    obj = News.objects.filter()
    context = {
        "list": ["Django", "Flask", "Oddo"],
        "data": obj
    }
    return render(request, "home.html", context)


def Contact(request):
    return render(request, "contact.html")

def NewsDate(request, year):
    article_list = News.objects.filter(pub_date__year = year)
    context ={
        'year' : year,
        'article_list' : article_list
    }
    return render(request, "NDate.html", context)

def Crud(request):
    # create
    datNews = News(
        author='Ali',
        title='Ali Title',
        description='lorem lipsum gfgfgre5'
    )
    datNews.save()

    # Read
    objects = News.objects.all()

    res = 'Print All Data <br>'

    for do in objects:
        res += 'Author is' + do.author+'<br>'
        res += 'Tittle is' + do.title+'<br>'
        res += 'Description is' + do.description+'<br>'
    '''    
    #update
    res += 'upadte author Ali to Taufiq <br>'
    do = News.objects.get(author = 'Ali')
    do.author = 'Taufiq'
    do.save()
    
    #DELETE
    res += 'Delete Author Taufiq'
    do = News.objects.get(author = 'Taufiq')
    do.delete()
    '''
    return HttpResponse(res)


