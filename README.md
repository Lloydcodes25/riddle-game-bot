# 🧩 Угадай загадку

Telegram-бот для игры в загадки: 4 попытки на ответ, подсказки и статистика попыток. Загадки хранятся в базе данных.

![Главный экран](screenshots/01_main.png)

## 🛠 Стек технологий

- Python 3.11+
- aiogram 3 — фреймворк для Telegram-ботов
- aiosqlite — асинхронная работа с SQLite
- python-dotenv — управление секретами через .env

## ✨ Возможности

- 🎮 Игра «угадай загадку» с 4 попытками
- 💾 Загадки хранятся в SQLite
- 🔢 Счётчик попыток на пользователя (FSM)
- ⌨️ Reply-клавиатура для быстрого доступа к новой загадке
- 🎲 Случайная загадка из базы

## 🚀 Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/USERNAME/riddle-bot.git
cd riddle-bot
```

### 2. Создать виртуальное окружение

```bash
python -m venv venv

# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Получить токен бота

- Открой Telegram → **@BotFather**
- Отправь `/newbot` → следуй инструкциям
- Скопируй полученный токен

### 5. Настроить `.env`

Скопируй `.env.example` в `.env`:

```bash
cp .env.example .env
```

Содержимое `.env`:

```
BOT_TOKEN=ваш_токен_здесь
DB_PATH=riddle_game.db
```

### 6. Создать и наполнить базу данных

```bash
python init_db.py
python seed.py
```

### 7. Запустить бота

```bash
python riddle_game_bot.py
```

## 📸 Скриншоты

| Успешная игра | С нескольких попыток | Все попытки провалились |
|---|---|---|
| ![main](screenshots/01_main.png) | ![multi](screenshots/02_multi_attempt.png) | ![failed](screenshots/03_failed.png) |

## 📁 Структура проекта

```
riddle-bot/
├── screenshots/            # скриншоты для README
│   ├── 01_main.png
│   ├── 02_multi_attempt.png
│   └── 03_failed.png
├── .env.example
├── .gitignore
├── config.py               # конфигурация
├── game_logic.py           # логика работы с загадками
├── init_db.py              # создание таблиц
├── riddles_data.py         # данные для seed
├── riddle_game_bot.py      # точка входа
├── requirements.txt
├── seed.py                 # наполнение БД
└── README.md
```

## 📄 Лицензия

MIT