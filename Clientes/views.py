from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages  # Para mensagens de feedback
from .models import Cliente, Carro
import re


def clientes(request):
    if request.method == "GET":
        clientes_list = Cliente.objects.all()
        return render(request, 'Clientes/clientes.html', {'clientes': clientes_list})

    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        cliente = Cliente.objects.filter(cpf=cpf)

        # Verifica se o cliente já existe
        if cliente.exists():
            messages.error(request, "CPF já cadastrado! Verifique os dados ou atualize o cliente existente.")
            return render(request, 'Clientes/clientes.html', {
                'nome': nome,
                'sobrenome': sobrenome,
                'email': email,
                'cpf': cpf,
                'carros': zip(carros, placas, anos),
                'clientes': Cliente.objects.all()  # Passa a lista de clientes novamente
            })

        # Valida o email com regex
        email_pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(email_pattern, email):
            messages.error(request, "E-mail inválido! Digite um e-mail válido.")
            return render(request, 'Clientes/clientes.html', {
                'nome': nome,
                'sobrenome': sobrenome,
                'cpf': cpf,
                'carros': zip(carros, placas, anos),
                'clientes': Cliente.objects.all()  # Passa a lista de clientes novamente
            })

        # Valida o CPF
        if len(cpf) != 11 or not cpf.isdigit():
            messages.error(request, "CPF inválido! Certifique-se de que ele possui 11 dígitos numéricos.")
            return render(request, 'Clientes/clientes.html', {
                'nome': nome,
                'sobrenome': sobrenome,
                'email': email,
                'carros': zip(carros, placas, anos),
                'clientes': Cliente.objects.all()  # Passa a lista de clientes novamente
            })

        # Cria o cliente
        cliente = Cliente(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            cpf=cpf
        )
        cliente.save()

        # Cria os carros associados ao cliente
        for carro, placa, ano in zip(carros, placas, anos):
            if carro and placa and ano:
                Carro.objects.create(carro=carro, placa=placa, ano=ano, cliente=cliente)
            else:
                messages.warning(request,
                                 "Informações incompletas de alguns carros. Certifique-se de preencher todos os campos.")

        messages.success(request, f"Cliente {nome} {sobrenome} cadastrado com sucesso!")
        return render(request, 'Clientes/clientes.html', {
            'clientes': Cliente.objects.all()  # Atualiza a lista de clientes
        })

    # Garante que o método sempre retorna uma resposta
    return HttpResponse("Método HTTP não permitido.", status=405)


def att_clientes(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=id)
    return JsonResponse({'teste': 1})
    