from django.shortcuts import redirect, render
from .models import Pessoas
from django.contrib import messages

def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

    if not nome or not email or not senha:
        messages.error(request, "por favor, preencha todos os campos")
        return redirect("cadastro")
    
    if len(nome) >=2 or len(nome)<=201:
        messages.error(request, "maximo de letras é 200 e o minimo é de 3")
        return redirect("cadastro")
    
    if len(senha) < 4 or len(senha) > 20:
        messages.error(request,
            "senha deve ter no mínimo 4 caracteres e no máximo 20 caracteres",)
        return redirect("cadastro")
    
    if " " in senha:
        messages.error(request, "a senha não pode ter espaço")
        return redirect("cadastro")
    
    if Pessoas.objects.filter(email=email).exists():
        messages.error(request, "Usuario ja existe")
        return redirect("cadastro")
    
    try:
        pessoas = Pessoas.objects.create_user(
            nome=nome,
            email=email,
            senha=senha)
        messages.success(request, "Usuario criado com sucesso")
        return redirect("cadastro")
    except Exception as e:
        messages.error(request, "erro ao criar a conta")
        return redirect("cadastro")
