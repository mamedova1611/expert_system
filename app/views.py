from random import random

from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render
from django.views import generic, View

from app.forms import *
from app.models import *


class UserLoginView(LoginView):
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    template_name = 'logout.html'


def index(request):
    return render(request, 'index.html')


def view(request):
    if request.method == 'POST':
        score = request.POST.get('answer')
        question = request.POST.get('score')
        print(score)
        id = request.POST.get('id')
        Answer.objects.create(question=question, score=score)
        if request.POST.get('form'):
            last = Questions.objects.last()
            if question == last.question:
                summa = 0
                answers = Answer.objects.all()
                for ans in answers:
                    summa += ans.score
                results = Result.objects.all()
                for res in results:
                    if summa >= res.min_score and summa <= res.max_score:
                        return render(request, 'recommendation.html', {'recommendation': res.recommendation})
            else:
                return render(request, 'form.html',
                          {'i': Questions.objects.get(id=int(id) + 1), 'answer': Options.objects.all()})
        if request.POST.get('rec'):
            summa = 0
            answers = Answer.objects.all()
            for ans in answers:
                summa += ans.score
            results = Result.objects.all()
            for res in results:
                if summa >= res.min_score and summa <= res.max_score:
                    return render(request, 'recommendation.html', {'recommendation': res.recommendation})
    return render(request, 'form.html', {'i': Questions.objects.first(), 'answer': Options.objects.all()})


def expert(request):
    return render(request, 'expert.html')


class QuestionsListView(generic.ListView):
    model = Questions
    template_name = 'question.html'
    context_object_name = 'question'


class QuestionsFormView(View):
    def get(self, request):
        question_form = QuestionsForm()
        return render(request, 'question_form.html', {'question_form': question_form})

    def post(self, request):
        question_form = QuestionsForm(request.POST)
        if question_form.is_valid():
            Questions.objects.create(**question_form.cleaned_data)
            return render(request, "question_form.html")
        return render(request, 'question_form.html', {'question_form': question_form})


class QuestionsEditFormView(View):
    def get(self, request, pk):
        question = Questions.objects.get(pk=pk)
        question_form = QuestionsForm(instance=question)
        return render(request, 'question_edit.html', {'question_form': question_form, 'question_id': pk})

    def post(self, request, pk):
        question = Questions.objects.get(pk=pk)
        question_form = QuestionsForm(request.POST, instance=question)
        if question_form.is_valid():
            question.save()
        return render(request, 'question_edit.html', {'question_form': question_form, 'question_id': pk})


class QuestionsDelFormView(View):
    def post(self, request, pk):
        Questions.objects.filter(pk=pk).delete()
        return render(request, "question.html")


class ResultListView(generic.ListView):
    model = Result
    template_name = 'result.html'
    context_object_name = 'result'


class ResultFormView(View):
    def get(self, request):
        result_form = ResultForm()
        return render(request, 'result_form.html', {'result_form': result_form})

    def post(self, request):
        result_form = ResultForm(request.POST)
        if result_form.is_valid():
            Result.objects.create(**result_form.cleaned_data)
            return render(request, "result.html")
        return render(request, 'result_form.html', {'result_form': result_form})


class ResultEditFormView(View):
    def get(self, request, pk):
        result = Result.objects.get(pk=pk)
        result_form = ResultForm(instance=result)
        return render(request, 'result_edit.html', {'result_form': result_form, 'result_id': pk})

    def post(self, request, pk):
        result = Result.objects.get(pk=pk)
        result_form = ResultForm(request.POST, instance=result)
        if result_form.is_valid():
            result.save()
        return render(request, 'result_edit.html', {'result_form': result_form, 'result_id': pk})


class ResultDelFormView(View):
    def post(self, request, pk):
        Result.objects.filter(pk=pk).delete()
        return render(request, "result.html")


class OptionsListView(generic.ListView):
    model = Options
    template_name = 'options.html'
    context_object_name = 'options'


class OptionsFormView(View):
    def get(self, request):
        options_form = OptionsForm()
        return render(request, 'options_form.html', {'options_form': options_form})

    def post(self, request):
        options_form = OptionsForm(request.POST)
        if options_form.is_valid():
            Options.objects.create(**options_form.cleaned_data)
            return render(request, "options.html")
        return render(request, 'options_form.html', {'options_form': options_form})


class OptionsEditFormView(View):
    def get(self, request, pk):
        options = Options.objects.get(pk=pk)
        options_form = OptionsForm(instance=options)
        return render(request, 'options_edit.html', {'options_form': options_form, 'options_id': pk})

    def post(self, request, pk):
        options = Options.objects.get(pk=pk)
        options_form = OptionsForm(request.POST, instance=options)
        if options_form.is_valid():
            options.save()
        return render(request, 'options_edit.html', {'options_form': options_form, 'options_id': pk})


class OptionsDelFormView(View):
    def post(self, request, pk):
        Options.objects.filter(pk=pk).delete()
        return render(request, "options.html")
