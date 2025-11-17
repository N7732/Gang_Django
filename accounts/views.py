from django.shortcuts import render, redirect
from .form import account

# Create your views here.
def custom_form(request):
    if request.method == 'POST':
        form = account(request.POST)

        if form.is_valid():
            form.save()   # save to database
            return redirect('success')  #

    else:
        form = account()
    return render(request, 'main.html', {'form': form})