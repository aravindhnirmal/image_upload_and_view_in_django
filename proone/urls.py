from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from  import hotel_image_view, success, show_images
from appone.views import hotel_image_view, success, show_images

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hotel_image_view, name='image_upload'),
    path('success/', success, name='success'),
    path('show/', show_images, name='show_images'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
