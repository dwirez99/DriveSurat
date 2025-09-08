from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from crudsurat.views import SuratListView,SuratDetailView,UploadSuratView,SuratUpdateView,SuratDeleteView, pdf_view, KategoriSuratListView, KategoriSuratCreateView, KategoriSuratUpdateView, KategoriSuratDeleteView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SuratListView.as_view(), name='surat-list'),
    path('surat/tambah/', UploadSuratView.as_view(), name='surat-create'),
    path('surat/<int:pk>/', SuratDetailView.as_view(), name='surat-detail'),
    path('surat/<int:pk>/pdf/', pdf_view, name='surat-pdf'),
    path('surat/<int:pk>/edit/', SuratUpdateView.as_view(), name='surat-update'),
    path('surat/<int:pk>/hapus/', SuratDeleteView.as_view(), name='surat-delete'),
    path('kategori/', KategoriSuratListView.as_view(), name='kategori-list'),
    path('kategori/tambah/', KategoriSuratCreateView.as_view(), name='kategori-create'),
    path('kategori/<int:pk>/edit/', KategoriSuratUpdateView.as_view(), name='kategori-edit'),
    path('kategori/<int:pk>/hapus/', KategoriSuratDeleteView.as_view(), name='kategori-delete'),
     path('About/', TemplateView.as_view(template_name='about.html'), name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
