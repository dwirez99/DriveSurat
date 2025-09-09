from django import forms
from .models import Surat, KategoriSurat

class SuratForm(forms.ModelForm):
    # Use a plain ChoiceField backed by KategoriSurat names so we can keep Surat.kategori as CharField
    kategori = forms.ChoiceField(choices=[], required=True, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Surat
        fields = ['nomor_surat', 'kategori', 'judul', 'file_pdf']
        widgets = {
            'nomor_surat': forms.TextInput(attrs={'class': 'form-control'}),
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'file_pdf': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate choices from KategoriSurat names
        kategori_choices = [(k.nama, k.nama) for k in KategoriSurat.objects.all().order_by('nama')]
        # Make sure the current value (on update) is present even if it's no longer in the master table
        current_val = None
        if self.instance and getattr(self.instance, 'pk', None):
            current_val = getattr(self.instance, 'kategori', None)
        if current_val and (current_val, current_val) not in kategori_choices:
            kategori_choices = [(current_val, current_val)] + kategori_choices
        self.fields['kategori'].choices = [('', 'Pilih Kategori')] + kategori_choices

    # Ensure we store a string in the CharField even if anything odd happens
    def clean_kategori(self):
        value = self.cleaned_data.get('kategori')
        if isinstance(value, str):
            return value
        # Fallback: if a model instance was somehow passed
        try:
            return getattr(value, 'nama')
        except Exception:
            return str(value) if value is not None else ''
