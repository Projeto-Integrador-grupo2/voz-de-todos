import qrcode
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.db.models import Count, Q, F

from .models import Sala, Questao, Resposta
from .forms import SalaForm, QuestaoForm


def home(request):
    return render(request, 'home.html')


# AUTH
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Login inválido")

    return render(request, 'professor/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


# DASHBOARD
@login_required
def dashboard(request):
    salas = request.user.salas.all()
    return render(request, 'professor/dashboard.html', {'salas': salas})


# SALAS
@login_required
def salas(request):
    salas = request.user.salas.all()
    return render(request, 'professor/salas.html', {'salas': salas})


@login_required
def sala_create(request):
    form = SalaForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            sala = form.save(commit=False)
            sala.professor = request.user
            sala.full_clean()
            sala.save()
            
            messages.success(request, "Sala criada!")
            return redirect('salas')
        else:
            print(form.errors)
    return render(request, 'professor/sala_form.html', {'form': form})


@login_required
def sala_edit(request, id):
    sala = get_object_or_404(Sala, id=id, professor=request.user)
    form = SalaForm(request.POST or None, instance=sala)

    if request.method == "POST":
        if form.is_valid():
            sala = form.save(commit=False)
            sala.full_clean()
            sala.save()
            messages.success(request, "Sala atualizada!")
            return redirect('salas')
        else:
            print(form.errors)
    return render(request, 'professor/sala_form.html', {'form': form})


# QUESTÕES
@login_required
def questoes(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id, professor=request.user)

    return render(request, 'professor/questoes.html', {
        'sala': sala,
        'questoes': sala.questoes.all()
    })


@login_required
def questao_create(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id, professor=request.user)
    form = QuestaoForm(request.POST or None)

    if form.is_valid():
        q = form.save(commit=False)
        q.sala = sala
        q.full_clean()
        q.save()

        messages.success(request, "Questão criada!")
        return redirect('questoes', sala_id=sala.id)

    return render(request, 'professor/questao_form.html', {'form': form})


@login_required
def questao_edit(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id, professor=request.user)
    form = QuestaoForm(request.POST or None, instance=q)

    if form.is_valid():
        q = form.save(commit=False)
        q.sala = sala
        q.full_clean()
        q.save()

        messages.success(request, "Questão editada!")
        return redirect('questoes', sala_id=sala.id)

    return render(request, 'professor/questao_form.html', {'form': form})



# QR CODE
@login_required
def qrcode_sala(request, id):
    sala = get_object_or_404(Sala, id=id, professor=request.user)

    url = request.build_absolute_uri(f"/responder/{sala.codigo}")

    try:
        img = qrcode.make(url)
    except Exception:
        return HttpResponse("Erro ao gerar QR", status=500)

    response = HttpResponse(content_type='image/png')
    img.save(response)
    return response


# ALUNO
def aluno_login(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        codigo = request.POST.get('codigo')

        if not nome or not codigo:
            return render(request, 'aluno/login.html', {'erro': 'Preencha tudo'})

        request.session['aluno'] = nome
        return redirect('responder', codigo=codigo)

    return render(request, 'aluno/login.html')


def responder(request, codigo):
    sala = get_object_or_404(Sala, codigo=codigo, ativa=True)

    aluno = request.session.get('aluno')
    if not aluno:
        return redirect('aluno_login')

    questoes = sala.questoes.all()

    if request.method == 'POST':
        with transaction.atomic():
            for q in questoes:
                resp = request.POST.get(f'q{q.id}')

                if resp and resp.isdigit() and int(resp) in [1,2,3,4]:
                    Resposta.objects.update_or_create(
                        aluno_nome=aluno,
                        questao=q,
                        defaults={'resposta': int(resp)}
                    )

        request.session.flush()
        return redirect('home')

    return render(request, 'aluno/responder.html', {'questoes': questoes})


# STATS
@login_required
def stats_json(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id, professor=request.user)

    qs = sala.questoes.annotate(
        total=Count('respostas'),
        acertos=Count('respostas', filter=Q(respostas__resposta=F('correta')))
    )

    data = [
        {
            'questao': q.texto[:40],
            'acertos': q.acertos,
            'erros': q.total - q.acertos
        }
        for q in qs
    ]

    return JsonResponse(data, safe=False)