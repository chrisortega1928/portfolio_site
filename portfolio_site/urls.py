from django.urls import path
from quote_generator import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #path('about/', views.about, name='about'),
]
