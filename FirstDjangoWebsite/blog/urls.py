from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Sylwester Ejkszto - portfolio'),
    path('marketscaner/', views.dj_bs, name="django_bs"),
    path('listofprograms/', views.listofprograms, name='example'),
    path('NicknameGenerator/', views.NicknameGenerator, name="NicknameGenerator"),
    path('sudoku/', views.sudoku, name = "sudoku")
]