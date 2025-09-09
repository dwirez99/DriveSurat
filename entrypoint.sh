#!/bin/sh
set -e

echo "[entrypoint] Start"

if [ "$SQL_HOST" ] && [ "$SQL_DATABASE" ]; then
  echo "[entrypoint] Waiting for database $SQL_HOST:${SQL_PORT:-5432} ..."
  until python - <<'PY'
import os, psycopg2
try:
    psycopg2.connect(
        host=os.environ['SQL_HOST'],
        port=os.environ.get('SQL_PORT','5432'),
        user=os.environ['SQL_USER'],
        password=os.environ['SQL_PASSWORD'],
        dbname=os.environ['SQL_DATABASE']
    )
except Exception:
    raise SystemExit(1)
PY
  do
    echo "[entrypoint] DB not ready, retrying..."; sleep 2;
  done
  echo "[entrypoint] DB ready."
else
  echo "[entrypoint] Using SQLite fallback (no SQL_* env)."
fi

echo "[entrypoint] Migrating..."
python manage.py migrate --noinput

FIXTURE=crudsurat/fixtures/initial_data.json
AUTO_DUMP=${AUTO_DUMP_FIXTURE:-0}

COUNT_KAT=$(python manage.py shell -c "from crudsurat.models import KategoriSurat; print(KategoriSurat.objects.count())" 2>/dev/null || echo 0)
COUNT_SURAT=$(python manage.py shell -c "from crudsurat.models import Surat; print(Surat.objects.count())" 2>/dev/null || echo 0)
echo "[entrypoint] Counts -> Kategori=$COUNT_KAT Surat=$COUNT_SURAT"

if [ "$COUNT_KAT" = "0" ] && [ "$COUNT_SURAT" = "0" ]; then
  if [ -f "$FIXTURE" ]; then
    echo "[entrypoint] Empty DB, loading fixture $FIXTURE ..."
    if python manage.py loaddata "$FIXTURE"; then
      echo "[entrypoint] Fixture loaded."
    else
      echo "[entrypoint] WARNING: Fixture load failed" >&2
    fi
  else
    echo "[entrypoint] No fixture file found to load."
  fi
else
  echo "[entrypoint] DB not empty; skipping auto-load."
fi

if [ "$AUTO_DUMP" = "1" ]; then
  if [ "$COUNT_KAT" != "0" ] || [ "$COUNT_SURAT" != "0" ]; then
    echo "[entrypoint] AUTO_DUMP_FIXTURE=1 -> dumping current data to $FIXTURE"
    python manage.py dumpdata crudsurat.KategoriSurat crudsurat.Surat --indent 2 -o "$FIXTURE" || echo "[entrypoint] WARNING: dump failed" >&2
  else
    echo "[entrypoint] AUTO_DUMP_FIXTURE=1 but no data to dump."
  fi
fi

echo "[entrypoint] Launching server..."
exec uvicorn DriveSurat.asgi:application --host 0.0.0.0 --port 8000 --reload
