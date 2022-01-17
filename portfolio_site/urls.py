from django.urls import path, include
from quote_generator import views
from exchange_rate import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #path('exchange_rate/', views.index, name='index'),
    path('blog/', include('blog.urls')),
    #path('about/', views.about, name='about'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)