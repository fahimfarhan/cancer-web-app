from patientbasicinfo.models import Medicine, Dose, Timetable, Bangla


def autocomplete():
    bangla = []
    bangla_array = Bangla.objects.values_list('bangla', flat=True)
    for i in bangla_array:
        bangla.append(i)

    medicine = []
    medicine_array = Medicine.objects.values_list('name', flat=True)
    for i in medicine_array:
        medicine.append(i)

    dose = []
    dose_array = Dose.objects.values_list('dose', flat=True)
    for i in dose_array:
        dose.append(i)

    timetable = []
    timetable_array = Timetable.objects.values_list('time', flat=True)
    for i in timetable_array:
        timetable.append(i)
    context = {'bangla': bangla, 'medicine': medicine, 'dose': dose, 'timetable': timetable}
    return context
