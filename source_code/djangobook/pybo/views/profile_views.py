from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from pybo.models import Question, Answer, Comment


@login_required
def profile(request):
    user = request.user

    questions = Question.objects.filter(author=user).order_by('-create_date')
    answers = Answer.objects.filter(author=user).order_by('-create_date')
    comments = Comment.objects.filter(author=user).order_by('-create_date')

    context = {
        'user_profile': user,
        'questions': questions,
        'answers': answers,
        'comments': comments,
    }
    return render(request, 'pybo/profile.html', context)
