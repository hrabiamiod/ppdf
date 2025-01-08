#!/usr/bin/env bash
# deploy.sh

echo "=== Rozpoczynam deployment ==="

# Przejdź do katalogu aplikacji (zakładamy, że skrypt wywoływany jest z katalogu projektu)
cd "$(dirname "$0")" || exit

# (Opcjonalnie) Jeżeli pracujesz bezpośrednio na klonie repo:
# echo "Pulling latest changes from Git..."
# git pull origin main

# Aktywuj wirtualne środowisko
echo "Activating virtual environment..."
source venv/bin/activate

# Zainstaluj/aktualizuj zależności
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# (Opcjonalnie) Migracje bazy – jeśli np. używasz Django
# python manage.py migrate

# Restart usługi (Gunicorn, Flask, itp. – zależnie od konfiguracji)
echo "Restarting systemd service..."
sudo systemctl restart myflaskapp

echo "=== Deployment zakończony pomyślnie! ==="
