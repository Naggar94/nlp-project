from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	template = loader.get_template('polls/index.html')
	if request.method == 'POST':
		name = request.POST.get(
			'sentence'
	           , '')
		context = {
			'name': name,
		}
	else:
		context = {}
	return HttpResponse(template.render(context, request))
