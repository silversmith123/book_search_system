from django.http.response import HttpResponse
from django.shortcuts import render
from elasticsearch import Elasticsearch
from django.conf import settings

# Create your views here.
def index(request):
	return render(request, 'index.html')

def result(request):
	keyword = request.GET.get(('keyword'))
	es = Elasticsearch(settings.ESURL)
	body = {"query" : {"match" : { "title":keyword } } }
	result = es.search(index='books', body=body, size=5)
	books = [doc['_source'] for doc in result['hits']['hits']]
	print(books)
	context={"books":books}
	return render(request, 'result.html', context=context)