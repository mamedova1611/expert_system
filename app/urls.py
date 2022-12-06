from django.urls import path
from .views import *

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('', index, name='index'),
    path('question',view,name='form'),
    path('expert', expert,name='expert'),
    path('questions', QuestionsListView.as_view(), name='questions'),
    path('questions/add', QuestionsFormView.as_view(), name='question_form'),
    path('questions/edit/<int:pk>', QuestionsEditFormView.as_view(), name='question_edit'),
    path('questions/del/<int:pk>', QuestionsDelFormView.as_view(), name='question_del'),
    path('options', OptionsListView.as_view(), name='options'),
    path('options/add', OptionsFormView.as_view(), name='options_form'),
    path('options/edit/<int:pk>', OptionsEditFormView.as_view(), name='options_edit'),
    path('options/del/<int:pk>', OptionsDelFormView.as_view(), name='options_del'),
    path('result', ResultListView.as_view(), name='result'),
    path('result/add', ResultFormView.as_view(), name='result_form'),
    path('result/edit/<int:pk>', ResultEditFormView.as_view(), name='result_edit'),
    path('result/del/<int:pk>', ResultDelFormView.as_view(), name='result_del'),
]