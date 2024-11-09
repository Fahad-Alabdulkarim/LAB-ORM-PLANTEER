from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('all/', views.all_plants, name='all_plants'),
    path('<int:plant_id>/detail/', views.plant_detail, name='plant_detail'),
    path('new/', views.add_plant, name='add_plant'),
    path('<int:plant_id>/update/', views.update_plant, name='update_plant'),
    path('<int:plant_id>/delete/', views.delete_plant, name='delete_plant'),
    path('search/', views.search_plants, name='search_plants'),
]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)