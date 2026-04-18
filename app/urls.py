from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # professor
    path('dashboard/', views.dashboard, name='dashboard'),
    path('salas/', views.salas, name='salas'),
    path('sala/nova/', views.sala_create, name='nova_sala'),
    path('sala/<int:id>/editar/', views.sala_edit, name='editar_sala'),
    path('sala/<int:sala_id>/questoes/', views.questoes, name='questoes'),
    path('questao/nova/<int:sala_id>/', views.questao_create, name='nova_questao'),
    path('questao/<int:id>/editar/', views.questao_edit, name='editar_questao'),
    path('qrcode/<int:id>/', views.qrcode_sala, name='qrcode'),

    # aluno
    path('aluno/', views.aluno_login, name='aluno_login'),
    path('responder/<str:codigo>/', views.responder, name='responder'),

    # api
    path('stats/<int:sala_id>/', views.stats_json, name='stats_json'),
]