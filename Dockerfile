# Используем официальный образ Python 3.10
FROM python:3.10-slim

# Устанавливаем переменную окружения для предотвращения буферизации вывода
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем Poetry и зависимости проекта
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Копируем весь код приложения в контейнер
COPY . /app/

# Создаем директорию для логов
RUN mkdir -p /app/logs

# Открываем порт 8000 для приложения
EXPOSE 8000

# Запуск pytest и приложения uvicorn через Poetry
CMD ["sh", "-c", "poetry run pytest && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000"]
