from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from crudsurat.views import SuratListView,SuratDetailView,SuratCreateView,SuratUpdateView,SuratDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SuratListView.as_view(), name='surat-list'),
    path('surat/<int:pk>/', SuratDetailView.as_view(), name='surat-detail'),
    path('surat/tambah/', SuratCreateView.as_view(), name='surat-create'),
    path('surat/<int:pk>/edit/', SuratUpdateView.as_view(), name='surat-update'),
    path('surat/<int:pk>/hapus/', SuratDeleteView.as_view(), name='surat-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
