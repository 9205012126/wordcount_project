from django.http import HttpResponse
from django.shortcuts import render
import operator
def index(request):
    return render(request, 'index.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    worddictionary = {}


    for word in word_list:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1

    sortedword = sorted(worddictionary.items(),key= operator.itemgetter(1), reverse=True)




    return render(request,'count.html',{'count':len(word_list),'sortedword': sortedword})


def about(request):
    return render(request,'about.html')