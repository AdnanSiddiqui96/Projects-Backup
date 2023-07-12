from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os
import cv2

ALLOWED_EXTENSIONS = {'png', 'webp', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def processImage(filename, operation):
    print(f"the operation is {operation} and filename is {filename}")

    img = cv2.imread(f"{settings.MEDIA_ROOT}/{filename}")
    if operation == "cgray":
        imgProcessed = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        newFilename = f"{filename.split('.')[0]}.webp"
        cv2.imwrite(f"{settings.MEDIA_ROOT}/{newFilename}", imgProcessed)

    elif operation == "cwebp":
        newFilename = f"{filename.split('.')[0]}.webp"
        cv2.imwrite(f"{settings.MEDIA_ROOT}/{newFilename}", img)

    elif operation == "cpng":
        newFilename = f"{filename.split('.')[0]}.png"
        cv2.imwrite(f"{settings.MEDIA_ROOT}/{newFilename}", img)

    elif operation == "cjpg":
        newFilename = f"{filename.split('.')[0]}.jpg"
        cv2.imwrite(f"{settings.MEDIA_ROOT}/{newFilename}", img)

    return newFilename

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def how(request):
    return render(request, "how.html")

def cont(request):
    return render(request, "cont.html")

def edit(request):
    if request.method == 'POST':
        operation = request.POST.get("operation")
        # check if the post request has the file part
        if 'file' not in request.FILES:
            messages.error(request, 'No file part')
            return redirect("home")
        file = request.FILES['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.name == '':
            messages.error(request, 'No selected file')
            return redirect("home")
        if file and allowed_file(file.name):
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            new = processImage(filename, operation)
            messages.success(request, f"Your image has been processed and is available <a href='{settings.MEDIA_URL}{new}' target='_blank'>here</a>", extra_tags='safe')
            return redirect("home")
    return render(request, "index.html")

