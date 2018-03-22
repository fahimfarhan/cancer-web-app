from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from analytics.forms import SearchByNumForm, SearchByPkForm
from analytics.querycontroller import QueryController
from chemotherapy.models import ChemoTherapy
from patientbasicinfo.models import Identity, Profile
from radiotherapy.models import RadioTherapy


qc = QueryController()

@login_required
def form_handle(request):
    # form = SearchByNumForm()
    # if request.method == 'POST':
    form = SearchByNumForm(request.POST)
    if form.is_valid():
        n = form.cleaned_data['mobile']

    num = Identity.objects.all().filter(mobileNo=n)

    context = {'form': form, 'n': n, 'num': num}
    return render(request, 'analytics/result.html', context)

@login_required
def form_handle_pk(request):
    n = 0
    by_p_id = None
    form = SearchByPkForm(request.POST)
    if form.is_valid():
        n = form.cleaned_data['p_id']
        by_p_id = get_object_or_404(Identity, pk=n)
    context = {'form': form, 'n': n,'by_p_id':by_p_id }
    return render(request, 'analytics/result.html', context)


@login_required
def nact(request):
    nact = qc.SelectAllWithNact()
    context = {'nact': nact}
    return render(request, 'analytics/result.html', context)

@login_required
def act(request):
    act = qc.SelectAllWithAct()
    context = {'act': act}
    return render(request, 'analytics/result.html', context)

@login_required
def concurrent(request):
    concurrent = qc.SelectAllWithConcurrent()
    context = {'concurrent': concurrent}
    return render(request, 'analytics/result.html', context)

@login_required
def palliative(request):
    palliative = qc.SelectAllWithPalliative()
    context = {'palliative': palliative}
    return render(request, 'analytics/result.html', context)


# linac cobalt brachy
@login_required
def brachy(request):
    brachy = qc.SelectAllWithBrachy()
    context = {'brachy': brachy}
    return render(request, 'analytics/result.html', context)

@login_required
def cobalt(request):
    cobalt = qc.SelectAllWithCobalt()
    context = {'cobalt': cobalt}
    return render(request, 'analytics/result.html', context)

@login_required
def linac(request):
    linac = qc.SelectAllWithLinac()
    context = {'linac': linac}
    return render(request, 'analytics/result.html', context)


@login_required
def stage_one(request):
    # qc = QueryController()
    context = qc.selectAllWithStage1()
    return render(request, 'analytics/result.html', context)

@login_required
def stage_two(request):
    context = qc.selectAllWithStage2()
    return render(request, 'analytics/result.html', context)

@login_required
def stage_three(request):
    context = qc.selectAllWithStage3()
    return render(request, 'analytics/result.html', context)

@login_required
def stage_four(request):
    context = qc.selectAllWithStage4()
    return render(request, 'analytics/result.html', context)

