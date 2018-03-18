from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from filetransfers.api import serve_file
from history.forms import HistoryForm, UploadForm
from history.models import HistoryModel, HistoryModelFile
from patientbasicinfo.controller import autocomplete
from patientbasicinfo.models import Identity


class HistoryController:
    def edit_history(self, request, p_id):
        pid = p_id
        if not HistoryModel.objects.filter(identity_fk=p_id).exists():
            return self.new_history(request, p_id)
        else:
            p_history = get_object_or_404(HistoryModel, identity_fk=p_id)
            if request.method == "POST":
                form = HistoryForm(request.POST, instance=p_history)
                if form.is_valid():
                    p_history = form.save()
                    return redirect('view_patientdetails', p_id=pid)
            else:
                form = HistoryForm(instance=p_history)
            ac = autocomplete()
            z = {'form': form, 'p_history': p_history}
            context = {**z, **ac}
            return render(request, 'history/EditHistory.html', context)

    def new_history(self, request, p_id):
        pid = p_id
        if request.method == "POST":
            form = HistoryForm(request.POST)
            if form.is_valid():
                p_history = form.save(commit=False)
                p_history.identity_fk = Identity.objects.get(pk=p_id)
                p_history.save()
            return redirect('view_patientdetails', p_id=pid)
        else:
            form = HistoryForm()
        ac = autocomplete()
        z = {'form': form}
        context = {**z, **ac}
        return render(request, 'history/EditHistory.html', context)

    # return HttpResponse("new radiotherapy")

    def delete_historyfile(self,request, p_id, num):
        pid = p_id
        p = get_object_or_404(HistoryModelFile, identity_fk=p_id, fnum=num)
        p.delete()
        return redirect('view_patientdetails', p_id=pid)

    def download_file(self, request, p_id, num):
        upload = get_object_or_404(HistoryModelFile, identity_fk=p_id, fnum=num)
        return serve_file(request, upload.file)

    def upload_handler(self, request, p_id):
        pid = p_id
        fnum=1
        try:
            fnum = 1 + HistoryModelFile.objects.filter(identity_fk=p_id).latest('fnum').fnum
        except: # num = 1 + Investigations.objects.filter(identity_fk=p_id, type=data.type).count()
            print("Exception at upload handler history/views.py")
        if request.method == "POST":
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                p_upload = form.save(commit=False)
                p_upload.identity_fk = get_object_or_404(Identity, pk=p_id)  # Investigations.
                p_upload.file = form.cleaned_data['file']
                p_upload.fnum = fnum
                p_upload.name = form.cleaned_data['file'].name
                p_upload.save()
                return redirect('view_patientdetails', p_id=pid)
        else:
            form = UploadForm()
        context = {'form': form}
        return render(request, 'uploadfile/uploadfile.html', context)
