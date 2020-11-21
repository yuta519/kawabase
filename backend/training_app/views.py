from django.http import HttpResponse
from .models import Training
from django.template import loader
from django.http import Http404
from django.shortcuts import render


def index(request):
    latest_training_list = Training.objects.order_by('-date')[:5]
    template = loader.get_template('training_app/index.html')
    context = {'latest_training_list': latest_training_list,}
    return HttpResponse(template.render(context, request))

def next_depth(request):
    return HttpResponse("This is a Yuta orriginal message. Hey.")

def detail(request, training_id):
    try:
        training = Training.objects.get(pk=training_id)
    except Training.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'training_app/detail.html', {'training': training})

def results(request, training_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % training_id)

def vote(request, training_id):
    return HttpResponse("You're voting on question %s." % training_id)

def timeline(request):
    return render(request, 'training_app/timeline.html')
