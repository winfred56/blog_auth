from django.shortcuts import redirect, render
from .forms import Registeration

def registeration(request):
    if request.method == 'POST':
        form = Registeration(request.POST)
        if form.is_valid():
            form.save()
            print('New user has been created')
            return redirect('login')
    else:
        form = Registeration()
    context = {
        'form':form
        }
    return render(request, 'users/registeration.html', context)
