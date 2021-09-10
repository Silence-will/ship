from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_data', views.update_data, name='update_data'),
    path('get_data', views.get_data, name='get_data'),
    path('order_ship', views.order_ship, name='order_ship'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
