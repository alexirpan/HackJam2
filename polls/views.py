# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from polls.models import Image

def index(request):
    img = Image.objects.get(pk=1)
    template = loader.get_template('polls/index.html')
    context = Context({
        'img': img
    })
    return HttpResponse(template.render(context))
    
def rename(request):
    img = Image.objects.get(pk=1)
    img.name = "POTATO"
    template = loader.get_template('polls/rename.html')
    context = Context({
        'img': img
    })
    return HttpResponse(template.render(context))
    
def detail(request, poll_id):
    return HttpResponse("Looking at poll %s." % poll_id)
    
def results(request, poll_id):
    return HttpResponse("Results of poll %s." % poll_id)
    
def vote(request, poll_id):
    return HttpResponse("Voting on poll %s." % poll_id)