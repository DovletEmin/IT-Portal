# IT-Portal Backend

Backend API для портала новостей (текстовых и видео), реализованный на Django и Django REST Framework с использованием PostgreSQL.

---

## Описание проекта

**IT-Portal** — это REST API, предоставляющее функциональность для публикации и получения новостей:
- Текстовые новости (с заголовком, описанием, фото, категорией, датой и просмотрами)
- Видео новости (с заголовком, видеофайлом, категорией, датой и просмотрами)

Проект реализован с современным подходом:  
- Используется PostgreSQL как база данных  
- REST API с CRUD операциями для обеих моделей  
- Документация API через Swagger  
- Оптимизация запросов и структура кода для удобного расширения

---

## Установка и запуск

### Клонирование репозитория

```bash
git clone [<URL_репозитория>](https://github.com/DovletEmin/IT-Portal.git)
cd it-portal

python -m venv venv
source venv/bin/activate        # Linux / MacOS
venv\Scripts\activate           # Windows

pip install -r requirements.txt

Настройка базы данных
  1. Убедитесь, что PostgreSQL запущен и создана база данных, пользователь с правами.
  2. Отредактируйте settings.py для подключения к вашей БД.

python manage.py migrate

python manage.py runserver
```
---

## Использование API
  Документация доступна по адресу: http://localhost:8000/swagger/

### Основные эндпоинты:

  /api/text-news/ — Текстовые новости (GET, POST, PUT, DELETE)

  /api/video-news/ — Видео новости (GET, POST, PUT, DELETE)

