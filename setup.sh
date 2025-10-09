#!/bin/bash

read -rp "Bot token: " bot_token

cat > .env <<EOF
BOT_TOKEN='$bot_token'
EOF

read -rp "Create Python venv? [Y/n]: " create_venv

if [[ "$create_venv" =~ ^[Yy]$ ]]; then
    python3 -m venv bot-env
    source bot-env/bin/activate
    pip install -r requirements.txt
fi
