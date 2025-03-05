# 🤖 AI Creative Hub

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-lightgrey.svg)](https://flask.palletsprojects.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow.svg)](https://www.ecma-international.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://html.spec.whatwg.org/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/)

## 📝 Описание

Современный веб-сайт для взаимодействия с искусственным интеллектом, предоставляющий расширенные возможности общения с AI в различных ролях. Проект включает в себя чат с ИИ с поддержкой множества моделей и настраиваемых ролей.

## ✨ Особенности

### 🎨 Дизайн и интерфейс
- Современный адаптивный дизайн
- Темная тема с неоморфическими элементами
- Плавные анимации и переходы
- Поддержка мобильных устройств
- Интуитивно понятный интерфейс

### 💬 Чат с ИИ
- Множество доступных AI моделей
- Различные роли ИИ:
  - 👨‍💼 Обычный ассистент
  - 👨‍💻 Программист
  - ✍️ Писатель
  - 👨‍🏫 Учитель
  - 🎭 Без ограничений (18+)
  - 🎨 Креативный режим
- Сохранение контекста беседы
- Markdown форматирование
- Подсветка синтаксиса кода

### ⚙️ Функциональность
- Копирование сообщений
- Регенерация ответов
- Продолжение генерации
- Оценка ответов (лайки/дислайки)
- Настройка параметров чата
- Сохранение настроек в localStorage

## 🛠️ Технологии

### Frontend
- HTML5 с семантической разметкой
- CSS3 (Flexbox, Grid, Animations)
- JavaScript (ES6+)
- Font Awesome иконки
- Google Fonts (Montserrat)

### Backend
- Python 3.9+
- Flask 3.0.0
- Flask-CORS
- Requests
- Python-dotenv
- OpenAI API

## 📦 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/swensi17/swensiaiii.git
cd swensiaiii
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Запустите сервер:
```bash
python app.py
```

5. Откройте браузер и перейдите по адресу:
```
http://localhost:5000
```

## 📁 Структура проекта

```
swensiaiii/
├── app.py                 # Основной файл сервера Flask
├── chat_model.py          # Модуль работы с AI моделями
├── chat.html             # Главная страница чата
├── requirements.txt      # Зависимости Python
├── styles/
│   └── chat.css         # Стили интерфейса
├── scripts/
│   └── chat.js          # Клиентская логика
└── .gitignore           # Игнорируемые файлы Git
```

## ⚡ Возможности AI моделей

- OpenAI GPT-4o-mini
- OpenAI GPT-4o
- OpenAI o1-mini
- Qwen 2.5 Coder 32B
- Llama 3.3 70B
- Mistral Nemo
- Unity with Mistral Large
- Midijourney musical transformer
- Rtist image generator
- SearchGPT with realtime search
- DeepSeek-V3
- Claude Hybridspace
- DeepSeek-R1
- Llamaguard 7B AWQ
- Gemini 2.0 Flash
- И многие другие...

## 🔧 Настройка

### Параметры чата
- Память контекста
- Автопрокрутка
- Звуковые уведомления
- Выбор роли AI
- Выбор модели

### Роли AI
Каждая роль имеет свои особенности и стиль общения:
- Обычный ассистент: Четкие и вежливые ответы
- Программист: Технические термины, код, объяснения
- Писатель: Богатый язык, художественные приемы
- Учитель: Простые объяснения, примеры
- Без ограничений: Прямые и честные ответы
- Креативный режим: Уникальные идеи

## 🚀 Использование

1. Выберите модель AI из выпадающего списка
2. Настройте роль AI в настройках
3. Введите сообщение в поле ввода
4. Используйте кнопки действий для управления диалогом
5. Настройте параметры чата под свои предпочтения

## 📄 Лицензия

Проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции
3. Зафиксируйте изменения
4. Отправьте пулл-реквест

## ⭐ Поддержка проекта

Если вам нравится проект, не забудьте поставить звезду на GitHub! 