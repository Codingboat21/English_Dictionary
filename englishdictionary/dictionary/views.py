from django.shortcuts import render
from pydictionary import Dictionary


def index(request):
    return render(request,'index.html')


def word(request):
    search=request.GET.get("search")
    dict=Dictionary(search)
    
    meaning=dict.meanings()
    synonyms_list = dict.synonyms()
    antonyms_list = dict.antonyms()

    context={
        'search':search,
        'meaning':meaning,
        'synonyms':synonyms_list,
        'antonyms':antonyms_list
    }



    return render(request,'word.html',context)
# Create your views here.
