from django.shortcuts import render, redirect
from .models import SavedForm

def form_view(request):
    if request.method == "POST":
        form_data = {k: v for k, v in request.POST.items() if k != 'csrfmiddlewaretoken'}
        SavedForm.objects.create(payload=form_data)
        return redirect('results_view')
    return render(request, 'app/form.html')

def results_view(request):
    records = SavedForm.objects.all().order_by('-created_at')
    return render(request, 'app/results.html', {'records': records})
