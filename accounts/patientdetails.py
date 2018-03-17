from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from patientbasicinfo.models import Identity, Comorbidity, Profile


@login_required
def view_patientdetails(request, p_id):
    patient = get_object_or_404(Identity, pk=p_id)
    if not Profile.objects.filter(identity=p_id).exists():
        profile = None
    else:
        profile = get_object_or_404(Profile, identity=p_id)

    if not Comorbidity.objects.filter(identity=p_id).exists():
        comorbidity = None
    else:
        comorbidity = get_object_or_404(Comorbidity, identity=p_id)
    context = {'patient': patient,'comorbidity':comorbidity,'profile':profile}
    return render(request, 'accounts/patientdetails.html', context)
