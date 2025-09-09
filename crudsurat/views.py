from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Surat, KategoriSurat
from .forms import SuratForm
# Kategori Surat CRUD Views
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class KategoriSuratListView(ListView):
    model = KategoriSurat
    context_object_name = 'kategori_list'
    template_name = 'kategori_surat.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nama__icontains=q)
        return queryset

class KategoriSuratCreateView(CreateView):
    model = KategoriSurat
    fields = ['nama']
    template_name = 'form_kategori_surat.html'
    success_url = reverse_lazy('kategori-list')

class KategoriSuratUpdateView(UpdateView):
    model = KategoriSurat
    fields = ['nama']
    template_name = 'form_kategori_surat.html'
    success_url = reverse_lazy('kategori-list')

class KategoriSuratDeleteView(DeleteView):
    model = KategoriSurat
    context_object_name = 'kategori'
    template_name = 'kategori_surat_confirm_delete.html'
    success_url = reverse_lazy('kategori-list')
from django.db.models import Q
from django.http import FileResponse, Http404
from django.views.decorators.clickjacking import xframe_options_exempt
import mimetypes
import os

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
    template_name = 'lihat_surat.html'

# Tampilan untuk membuat/mengunggah surat baru
class UploadSuratView(CreateView):
    model = Surat
    form_class = SuratForm
    template_name = 'upload_surat.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # file wajib pada create
        form.fields['file_pdf'].required = True
        return form

    def form_valid(self, form):
        file_pdf = self.request.FILES.get('file_pdf')
        if file_pdf and file_pdf.name.lower().endswith('.pdf'):
            self.object = form.save()
            messages.success(self.request, "Data Berhasil Disimpan")
            # Redirect ke halaman create agar form baru (kosong) ditampilkan
            return redirect('surat-create')
        else:
            messages.error(self.request, "File harus berformat PDF")
            return self.form_invalid(form)

# Tampilan untuk memperbarui data surat yang sudah ada
class SuratUpdateView(UpdateView):
    model = Surat
    form_class = SuratForm
    template_name = 'upload_surat.html'
    success_url = reverse_lazy('surat-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Pada update, file_pdf tidak wajib
        form.fields['file_pdf'].required = False
        return form

    def form_valid(self, form):
        # Simpan file lama sebelum update
        old_file = None
        if self.object.file_pdf:
            old_file = self.object.file_pdf.path
        
        # Cek jika ada file PDF baru yang di-upload
        file_pdf = self.request.FILES.get('file_pdf')
        if file_pdf:
            if file_pdf.name.lower().endswith('.pdf'):
                # Hapus file lama jika ada
                if old_file and os.path.isfile(old_file):
                    os.remove(old_file)
                
                # Simpan dengan file baru
                response = super().form_valid(form)
                messages.success(self.request, "Data Berhasil Diperbarui")
                return response
            else:
                messages.error(self.request, "File harus berformat PDF")
                return self.form_invalid(form)
        else:
            # Update tanpa mengubah file
            response = super().form_valid(form)
            messages.success(self.request, "Data Berhasil Diperbarui")
            return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Data Surat"
        # Ensure form is bound to the instance for pre-filled fields
        if 'form' not in context:
            context['form'] = self.get_form()
        return context

# Tampilan untuk menghapus surat
class SuratDeleteView(DeleteView):
    model = Surat
    context_object_name = 'surat'
    template_name = 'crudsurat/surat_confirm_delete.html' # Disesuaikan
    success_url = reverse_lazy('surat-list') # Disesuaikan

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        # Hapus file PDF terkait sebelum menghapus objek dari DB
        if self.object.file_pdf:
            if os.path.isfile(self.object.file_pdf.path):
                os.remove(self.object.file_pdf.path)
        
        messages.success(request, f"Surat '{self.object.judul}' berhasil dihapus")
        return super().delete(request, *args, **kwargs)


# View khusus untuk menampilkan PDF agar bisa di-embed dalam iframe/object
@xframe_options_exempt
def pdf_view(request, pk: int):
    try:
        surat = Surat.objects.get(pk=pk)
    except Surat.DoesNotExist:
        raise Http404("Surat tidak ditemukan")

    if not surat.file_pdf:
        raise Http404("File PDF tidak ditemukan")

    # Buka file dan kirim sebagai respon inline
    file_handle = surat.file_pdf.open('rb')
    # Gunakan content-type PDF secara eksplisit untuk konsistensi render
    response = FileResponse(file_handle, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{os.path.basename(surat.file_pdf.name)}"'
    # Pastikan bisa di-embed di iframe/object
    response['X-Frame-Options'] = 'ALLOWALL'
    return response
