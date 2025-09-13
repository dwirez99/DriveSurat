# Gunakan base image Python resmi
FROM python:3.9-slim

# Set environment variables untuk mencegah pembuatan file .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Memastikan output dari Python langsung tampil di terminal (penting untuk logs)
ENV PYTHONUNBUFFERED 1

# --- PERUBAHAN DIMULAI ---
# Install uv, package installer Python yang sangat cepat
RUN pip install uv
# --- PERUBAHAN SELESAI ---

# Set direktori kerja di dalam container
WORKDIR /app

# Salin file requirements
COPY requirements.txt /app/

# Install dependensi menggunakan uv
RUN uv pip install --no-cache --system -r requirements.txt

# Salin seluruh kode proyek ke direktori kerja
COPY . /app/

# Add entrypoint
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
