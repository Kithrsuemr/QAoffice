# entry/urls.py
from django.urls import path

from . import views

from post.views import QuestionListView, TagListView, index

urlpatterns = [
    path('', views.index, name="index"),
    path('ky0141/', views.ky_0141_1, name="ky_0141"),
    path('ky0141/question_post/', views.ky_0141_2, name="ky_0141_2"),
    path('ky0141/question_post/KY_0141.css', views.ky_0141_css, name="ky_0141_css"),
    path('ky0141/question_post/KY_0141.js', views.ky_0141_js, name="ky_0141_js"),
    path('ky0141/pdf', views.ky_0141_pdf, name="ky_0141_pdf"),
    
    path('ry0011/', views.ry_0011_1, name="ry_0011"),
    path('ry0011/RY-pdf/', views.ry_0011_2, name="ry_0011_2"),
    path('yh0010/', views.yh_0010_1, name="yh_0010"),
    path('yh0010/YH-pdf/', views.yh_0010_2, name="yh_0010_2"),

    path('ku0001/', QuestionListView.as_view(), name="ku_0001_1"),
    path('ku0001/<str:tag>/', TagListView.as_view(), name="ku_0001_2"),
]
