from django.shortcuts import render, HttpResponse
from django.core.files.storage import default_storage

# Create your views here.
def say_hello(request):
  # return HttpResponse('Hello world');
  return render(request, 'hello.html', {'name' : 'Shamonti'})

def file_upload(request):
  # return HttpResponse('Hello world');
  return render(request, 'upload.html')


def upload_file(request):
  if request.method == 'POST':
    uploaded_file = request.FILES['file']
    # File validation (optional):
    # Check for supported file types, size limits, etc.

    # Save uploaded file:
    filename = default_storage.save(uploaded_file.name, uploaded_file)
    # Alternatively, use a custom storage backend for specific locations
    # filepath = os.path.join(settings.MEDIA_ROOT, filename)
    # with open(filepath, 'wb+') as destination:
    #     for chunk in uploaded_file.chunks():
    #         destination.write(chunk)

    # Database connection and information storage (optional)
    # ... (implement your database logic here) ...

    return HttpResponse("File uploaded successfully!")
  else:
    return HttpResponseBadRequest("Invalid request method")
  
  if uploaded_file:
        filename = uploaded_file.name
        filepath = default_storage.save(uploaded_file.name, uploaded_file)
        # Save to database
        new_file = UploadedFile(filename=filename, filepath=filepath)
        new_file.save()
