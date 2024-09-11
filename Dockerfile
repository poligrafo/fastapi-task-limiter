# Используем Python 3.10
FROM python:3.10-slim

# Устанавливаем переменные окружения для предотвращения буферизации вывода Python
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию для приложения
WORKDIR /app

# Устанавливаем Poetry и отключаем создание виртуальных окружений
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false

# Копируем файлы для установки зависимостей
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем зависимости без dev-зависимостей
RUN poetry install --no-interaction --no-ansi

# Копируем исходный код приложения
COPY . /app/

# Создаем папку для логов
RUN mkdir -p /app/logs

# Открываем порт 8000 для приложения
EXPOSE 8000

# Запускаем приложение с uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
