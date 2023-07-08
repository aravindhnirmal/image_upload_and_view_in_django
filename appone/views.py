from django.shortcuts import render, redirect
from .forms import HotelForm
from .models import Hotel

def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
        return render(request, 'appone/hotel_image_form.html', {'form': form})

def success(request):
    return render(request, 'appone/success.html')

def show_images(request):
    images = Hotel.objects.all()
    return render(request, 'appone/show_images.html', {'images': images})
