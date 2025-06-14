from django.shortcuts import render
from ..models import UploadedFile  # models.py에서 UploadedFile import

def upload_file(request):
    uploaded_file_url = None
    title = None

    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']  
        title = request.POST.get('title', '') 

        uploaded = UploadedFile.objects.create(title=title, file=file)
        uploaded_file_url = uploaded.file.url

    return render(request, 'pybo/upload.html', {
        'uploaded_file_url': uploaded_file_url,
        'title': title
    })