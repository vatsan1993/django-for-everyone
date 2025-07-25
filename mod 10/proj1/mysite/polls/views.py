from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from .models import Question
# from django.template import loader
# Create your views here.g

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    context = {
        "latest_question_list": latest_question_list,
    }
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    # The render function from the shortcuts returns a HttpResponse object
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # # return HttpResponse("Your'r looking at the question %s." %question_id)

    # this will raise an error if the question does not exist
    question = get_object_or_404(Question, pk = question_id)
    # render will return a HttpResponse
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


