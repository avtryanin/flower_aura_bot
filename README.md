# Flower Aura Bot

## Описание
Телеграм-бот для заказа цветов.

# Технологии
- Aiogram
- PostgreSQL

## Требования
- Docker
- Docker Compose

## Запуск

1. Клонировать репозиторий:
```bash
git clone https://github.com/yourusername/flower_aura_bot.git
cd flower_aura_bot
```

2. Создать `.env` файл, пример:
```env
BOT_TOKEN='bot_token'
ADMIN_IDS=000000000,111111111,222222222
DATABASE_URL=postgresql+asyncpg:/postgres:postgres@db:5432flower_aura_bot
```

3. Запустить Docker Compose:
```bash
docker-compose up --build
```

4. Бот запустится и автоматически применит миграции.

## Git команды для заливки

В корне проекта выполни:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/flower_aura_bot.git
git push -u origin main
