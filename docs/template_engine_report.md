# 📘 Создание собственного шаблонизатора HTML (Template Engine)

## 1. Введение

В данном проекте реализован простой шаблонизатор HTML, который позволяет генерировать страницы на основе шаблонов и JSON-данных.

Такие системы используются в реальных фреймворках (Jinja2, Django Templates, Handlebars), где логика отделена от представления.

---

## 2. Цель проекта

Создать собственный template engine, который:

- читает HTML-шаблон
- подставляет данные из JSON
- генерирует готовый HTML-файл

---

## 3. Архитектура проекта

### Общая схема работы

```
JSON данные → engine.py → шаблон HTML → result.html
```

---

### Структура проекта

```
src/
├── data/
│ └── page.json
├── templates/
│ └── page.html
├── output/
│ └── result.html
├── engine.py
└── generate.py
```


---

## 4. Исследование предметной области

Перед разработкой были изучены:

- шаблонизаторы (Jinja2)
- подстановка переменных в строки
- регулярные выражения в Python
- работа с файлами
- парсинг текста

---

## 5. Реализация проекта

---

## 5.1 Формат шаблона

Используется синтаксис:

```html
<h1>{{title}}</h1>
<p>{{description}}</p>
```

## 5.2 JSON данные
```json
{
  "title": "Говори. Учись. Играй",
  "description": "Telegram-бот для изучения русского языка"
}
```

## 5.3 Шаблонизатор (engine.py)
```python
import json
import re

class TemplateEngine:
    def load_json(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def load_template(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def render(self, template, data):
        def replace(match):
            key = match.group(1)
            return str(data.get(key, ""))

        pattern = r"{{\s*(\w+)\s*}}"
        return re.sub(pattern, replace, template)
```

## HTML Шаблон

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
</head>
<body>

<h1>{{title}}</h1>
<p>{{description}}</p>

</body>
</html>
```
---
## 6. Принцип работы
Алгоритм:
- Загрузка JSON
- Загрузка HTML-шаблона
- Поиск переменных {{...}}
- Замена значений
- Сохранение результата
---
## 7. Диаграмма процесса
page.json → engine.py → page.html → result.html

---
## 8. Результат
```html
<h1>Говори. Учись. Играй</h1>
<p>Telegram-бот для изучения русского языка</p>
```
---
## 9. Вывод

Создан упрощённый шаблонизатор, который демонстрирует:

- работу с текстовыми шаблонами
- парсинг данных
- генерацию HTML