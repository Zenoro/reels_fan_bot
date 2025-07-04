# Используем официальный образ Python 3.11 slim для уменьшения размера контейнера
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Отключаем буферизацию Python
ENV PYTHONUNBUFFERED=1

CMD ["python3", "src/bot.py"]
