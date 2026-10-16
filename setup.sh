#!/bin/bash

echo "[*] Installing system dependencies..."
if command -v apt-get &> /dev/null; then
    sudo apt-get update -qq
    sudo apt-get install -y python3 python3-pip python3-venv jq curl
elif command -v brew &> /dev/null; then
    brew install python3 jq curl
else
    echo "[!] Unsupported package manager. Install python3, pip, jq, curl manually."
fi

echo "[*] Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "[*] Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[*] Copying env template..."
if [ ! -f .env ]; then
    cp config/.env.example .env
    echo "[+] Created .env — edit it with your keys."
fi

echo "[*] Creating logs directory..."
mkdir -p logs
touch logs/.gitkeep

echo "[✓] Setup complete. Run ./bot.sh to start."
