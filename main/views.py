from django.shortcuts import render, redirect
from .forms import SorveteForm
from .models import Sorvete
from django.http import JsonResponse

def sorvete_pedido(request):
    if request.method == 'POST':
        form = SorveteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido')# redireciona para a pagina de sucesso após salvar
    else:
        form = SorveteForm()
    return render(request, 'main/index.html', {'form':form})



def pedidos(request):
    query = Sorvete.objects.all()
    return render (request, 'main/lista.html', {'query': query})

def delete_item(request, item_id):
    # Here, you would implement the logic to delete the item from the database based on the item_id.
    # Replace 'YourModel' with your actual Django model class representing the data.
    try:
        item_to_delete = Sorvete.objects.get(id=item_id)
        item_to_delete.delete()
        return JsonResponse({'success': True})
    except Sorvete.DoesNotExist:
        return JsonResponse({'success': False})
