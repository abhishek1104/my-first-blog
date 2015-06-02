from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    context_dict ={'babaji': "I am rocking dude."}
    return render(request, 'blog/post_default.html', context_dict)
   