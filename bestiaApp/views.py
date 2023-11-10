from django.shortcuts import render, redirect, get_object_or_404
from bestiaApp.models import bestia
from .forms import Newbestia, Editbestia

# Create your views here.
def base(request):
    bestias = bestia.objects.filter()[0:4]
    roar = bestia.objects.all()
    
    return render(request, 'core/base.html', {
        'bestias': bestias,
        'roar': roar,
    })

#Registrar bestia
def register_user(request):
    if request.method == 'POST':
        form = Newbestia(request.POST, request.FILES)
        
        if form.is_valid():
            bestias = form.save()
            bestias.created_by = request.user
            bestias.save()
            
            return redirect('base')
    else:
        form = Newbestia

        
     
    return render(request, 'core/register.html', {
        'form':form
        
    })

#Delete bestia
def delete(request, pk):
    bestias = get_object_or_404(bestia, pk=pk)
    bestias.delete()
    return redirect('core/base.html')


#Edit bestia
def edit(request, pk):
    bestias = get_object_or_404(bestia, pk=pk)
   
    if request.method == "POST":
        form = Editbestia(request.POST, request.FILES, instance=bestias)
        
        if form.is_valid():
            bestias.save()
            
            pk = bestias.pk
            return redirect('edit', pk=pk)
        
    else:
        form = Editbestia(instance=bestias)
        
    return render(request, 'core/register.html', {
        'form': form,
        'title': 'Edit bestia'
    })


    
    

        
    
   