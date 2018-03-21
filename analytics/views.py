from django.shortcuts import render

# Create your views here.
from analytics.forms import SearchByNumForm, SearchByPkForm
from patientbasicinfo.models import Identity


def form_handle(request):
    # form = SearchByNumForm()
    # if request.method == 'POST':
    form = SearchByNumForm(request.POST)
    if form.is_valid():
        n = form.cleaned_data['mobile']

    num = Identity.objects.all().filter(mobileNo=n)

    context = {'form': form, 'n': n, 'num': num}
    return render(request, 'analytics/result.html', context)

def form_handle_pk(request):
    n=0
    key=0
    form = SearchByPkForm(request.POST)
    if form.is_valid():
        n = form.cleaned_data['p_id']
        key = Identity.objects.all().filter(pk=n)
    context = {'form':form, 'n':n, 'key':key}