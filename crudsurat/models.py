import os
from django.db import models
from django.urls import reverse

class KategoriSurat(models.Model):
    nama = models.CharField(max_length=100, unique=True, help_text="Nama kategori surat")
    judul = models.CharField(max_length=200, blank=True, null=True, help_text="Judul atau perihal surat (opsional)")

    def __str__(self):
        return self.nama

class Surat(models.Model):
    """
    Model ini merepresentasikan sebuah surat yang diarsipkan.
    """
    nomor_surat = models.CharField(max_length=100, unique=True, default="", help_text="Nomor resmi surat")
    kategori = models.CharField(max_length=100, default="Umum", help_text="Kategori atau jenis surat")
    judul = models.CharField(max_length=200, help_text="Judul atau perihal surat")
    # FileField untuk mengunggah file PDF
    file_pdf = models.FileField(upload_to='media/', help_text="File surat dalam format PDF")
    
    tanggal_unggah = models.DateTimeField(auto_now_add=True, help_text="Waktu pengarsipan")
    
    class Meta:
        ordering = ['-tanggal_unggah'] # Urutkan berdasarkan waktu pengarsipan terbaru
        verbose_name = "Surat"
        verbose_name_plural = "Daftar Surat"

    def __str__(self):
        return f"{self.judul} ({self.nomor_surat or 'No-Number'})"

    def get_absolute_url(self):
        """
        Mengembalikan URL untuk melihat detail surat ini.
        """
        return reverse('surat-detail', kwargs={'pk': self.pk})

    def delete(self, *args, **kwargs):
        """
        Override metode delete untuk menghapus file fisik dari disk
        ketika objek surat dihapus dari database.
        """
        # Hapus file PDF terkait sebelum menghapus objek dari DB
        if self.file_pdf:
            if os.path.isfile(self.file_pdf.path):
                os.remove(self.file_pdf.path)
        
        super().delete(*args, **kwargs)
