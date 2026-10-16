#!/bin/bash

if [ ! -f .env ]; then
    echo "[!] .env not found. Run ./setup.sh first."
    exit 1
fi

source .venv/bin/activate 2>/dev/null
source .env

python3 src/main.py --config config/config.yaml
