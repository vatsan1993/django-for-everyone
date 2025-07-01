from django.shortcuts import get_object_or_404, render
# from django.http import Http404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
# from django.template import loader
# Create your views here.g

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     # template = loader.get_template('polls/index.html')
#     # return HttpResponse(template.render(context, request))
#     # The render function from the shortcuts returns a HttpResponse object
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # # return HttpResponse("Your'r looking at the question %s." %question_id)

#     # this will raise an error if the question does not exist
#     question = get_object_or_404(Question, pk = question_id)
#     # render will return a HttpResponse
#     return render(request, "polls/detail.html", {"question": question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {
#             "question" : question
#         })

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last 5 published questions."""
        return Question.objects.order_by("pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def owner(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello, world. f5efd30f is the polls index.")
    return response

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice"
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

