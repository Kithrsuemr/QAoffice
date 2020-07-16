from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Question, Answer


def index(request):
    return HttpResponse("Welcome to QA Office.<br/>"
                        "This is the page to manage posts.<br />"
                        "Empty Now.")


# ToDo: Here should be a method to the List of Questions
# -- Assigned to Yamamoto-san
#  <----- Nomura-san's idea will be installed in this class.
#  <----- Searching Logic will be installed here: Uemura-san, and Kobayashi-san
class QuestionListView(generic.ListView):
    model = Question
    queryset = Question.objects.all()
    template_name = "post/question_list.html"
    success_url = "post:list_question"

    # ListView has 'object_list' default attribute, and it is set
    # by default.  However, it will select all questions.
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        tag = self.kwargs.get('tag')
        if tag is not None:
            chosen_question = Question.objects.filter(tag=tag)
        else:
            chosen_question = Question.objects.all()
        context.update(
            {'object_list': chosen_question},
        )
        return context

#
# class QuestionListView(generic.ListView):
#     model = Question
#
#     def get_context_data(self, **kwargs):
#         context = super(QuestionListView, self).get_context_data(**kwargs)
#         return context


class QuestionCreateView(generic.CreateView):
    model = Question


class QuestionUpdateView(generic.UpdateView):
    model = Question


# ToDo: classes to register Answers
# -- Assigned to Tao-san
class AnswerListView(generic.ListView):
    model = Answer


class AnswerCreateView(generic.CreateView):
    model = Answer


class AnswerUpdateView(generic.UpdateView):
    model = Answer
