# Используем официальный образ Python
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /code

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем проект
COPY . .

# Открываем порт
EXPOSE 8000

# Команда по умолчанию
CMD sh -c "python manage.py migrate && \
           python manage.py runserver 0.0.0.0:8000"
