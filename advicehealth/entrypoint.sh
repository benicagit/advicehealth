#!/bin/bash
set -e

if [ !"$1" ]; then
    exec "$@"
fi

echo "===================================="
echo "=== Criando migrações ==="
echo "===================================="
python manage.py makemigrations

echo "===================================="
echo "=== Aplicando migrações ==="
echo "===================================="
python manage.py migrate --no-input

echo "===================================="
echo "=== Coletando arquivos estáticos ==="
echo "===================================="
python manage.py collectstatic --no-input
