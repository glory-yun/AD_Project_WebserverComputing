from django.urls import path

from .views import base_views, question_views, answer_views, comment_views, vote_views
from pybo.views import upload_views
from pybo.views import api_views
from pybo.views import book_views
from pybo.views import profile_views
from pybo.views import request_views

app_name = 'pybo'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),

    # comment_views.py
    path('comment/create/question/<int:question_id>/',
         comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/',
         comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/',
         comment_views.comment_delete_question, name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/',
         comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/',
         comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/',
         comment_views.comment_delete_answer, name='comment_delete_answer'),

    # vote_views.py
    path('vote/question/<int:question_id>/',
         vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/',
         vote_views.vote_answer, name='vote_answer'),
]

urlpatterns += [
    path('upload/', upload_views.upload_file, name='upload_file'),
]

urlpatterns += [
    path('api/sample/', api_views.sample_api, name='sample_api'),
]

urlpatterns += [
    path('books/', book_views.book_list, name='book_list'),
    path('books/<int:book_id>/history/',
         book_views.book_history, name='book_history'),
]

urlpatterns += [
    path('profile/', profile_views.profile, name='profile'),
]


urlpatterns += [
    path('request-info/', request_views.request_info, name='request_info'),
]