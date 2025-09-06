from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Surat
from django.db.models import Q

# Tampilan untuk menampilkan daftar semua surat dengan pencarian
class SuratListView(ListView):
    model = Surat
    context_object_name = 'surat_list'
    template_name = 'arsip_surat.html' # Disesuaikan ke template yang benar
    paginate_by = 10 # Menampilkan 10 surat per halaman

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(judul__icontains=q)
        return queryset

# Tampilan untuk melihat detail satu surat
class SuratDetailView(DetailView):
    model = Surat
    context_object_name = 'surat'
    template_name = 'crudsurat/surat_detail.html' # Disesuaikan

# Tampilan untuk membuat/mengunggah surat baru
class SuratCreateView(CreateView):
    model = Surat
    fields = ['judul', 'nomor_surat', 'tanggal_surat', 'pengirim', 'penerima', 'kategori', 'file_pdf']
    template_name = 'crudsurat/surat_form.html' # Disesuaikan
    success_url = reverse_lazy('surat-list') # Disesuaikan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Unggah Surat Baru"
        return context

# Tampilan untuk memperbarui data surat yang sudah ada
class SuratUpdateView(UpdateView):
    model = Surat
    fields = ['judul', 'nomor_surat', 'tanggal_surat', 'pengirim', 'penerima', 'kategori', 'file_pdf']
    template_name = 'crudsurat/surat_form.html' # Disesuaikan
    success_url = reverse_lazy('surat-list') # Disesuaikan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Data Surat"
        return context

# Tampilan untuk menghapus surat
class SuratDeleteView(DeleteView):
    model = Surat
    context_object_name = 'surat'
    template_name = 'crudsurat/surat_confirm_delete.html' # Disesuaikan
    success_url = reverse_lazy('surat-list') # Disesuaikan
