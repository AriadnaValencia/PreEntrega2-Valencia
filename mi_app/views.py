from django.shortcuts import render, redirect
from .forms import ClienteForm, ProductoForm, PedidoForm, BuscarClienteForm
from .models import Cliente

def crear_cliente(request):
    #Creación de un nuevo cliente
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save() #Guardar cliente en la base de datos
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'mi_app/crear_cliente.html', {'form': form})

def buscar_cliente(request):
    if request.method == "GET":
        form = BuscarClienteForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            resultados = Cliente.objects.filter(nombre__icontains=nombre)
            return render(request, 'mi_app/buscar_cliente.html', {'form': form, 'resultados': resultados})
    else:
        form = BuscarClienteForm()
    return render(request, 'mi_app/buscar_cliente.html', {'form': form})
