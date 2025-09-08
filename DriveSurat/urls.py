from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from crudsurat.views import SuratListView,SuratDetailView,UploadSuratView,SuratUpdateView,SuratDeleteView, pdf_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SuratListView.as_view(), name='surat-list'),
    path('surat/tambah/', UploadSuratView.as_view(), name='surat-create'),
    path('surat/<int:pk>/', SuratDetailView.as_view(), name='surat-detail'),
    path('surat/<int:pk>/pdf/', pdf_view, name='surat-pdf'),
    path('surat/<int:pk>/edit/', SuratUpdateView.as_view(), name='surat-update'),
    path('surat/<int:pk>/hapus/', SuratDeleteView.as_view(), name='surat-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
