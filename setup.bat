@echo off
setlocal

set /p bot_token="Enter telegram-bot API: "

(
echo BOT_TOKEN='%bot_token%'
) > .env

set /p create_venv="Create Python venv? [Y/n]: "

if /I "%create_venv%"=="Y" (
    python -m venv bot-env
    call bot-env\Scripts\activate
    pip install -r requirements.txt
)

endlocal
