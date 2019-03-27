from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    poll_list = [
        {'id': 1, 'title': 'เพื่อนๆ คิดว่าวิชาเว็ปโปรสอนรู้เร่งไหม'},
        {'id': 2, 'title': 'title2'},
        {'id': 3, 'title': 'title3'},
    ]

    context = {
        'page_title': 'Welcome to my home page.',
        'poll_list': poll_list
    }

    return render(request, template_name='poll/index.html', context=context)

def detail(request, poll_id):
    return HttpResponse("Detail is Here!! %s" %(str(poll_id)))