from django.shortcuts import redirect

def redirect_articles(request):
    return redirect('articles_list_url', permanent=True)