import os

BASE_DIR = os.path.dirname(__file__)

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "site")

PAGES = [
    ("index.html", "Главная"),
    ("about.html", "О проекте"),
    ("team.html", "Участники"),
    ("journal.html", "Журнал"),
    ("partner.html", "Партнёр"),
    ("resources.html", "Ресурсы"),
    ("game.html", "Игра"),
]

def load(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def render(template, context):
    for key, value in context.items():
        template = template.replace("{{" + key + "}}", value)
    return template

base = load(os.path.join(TEMPLATES_DIR, "base.html"))
header = load(os.path.join(TEMPLATES_DIR, "header.html"))
nav = load(os.path.join(TEMPLATES_DIR, "nav.html"))
footer = load(os.path.join(TEMPLATES_DIR, "footer.html"))

for filename, title in PAGES:
    content = load(os.path.join(DATA_DIR, filename))

    context = {
        "title": title,
        "year": "2026"
    }

    page = render(base, context)

    page = page.replace("{{header}}", header)
    page = page.replace("{{nav}}", nav)
    page = page.replace("{{footer}}", footer)
    page = page.replace("{{content}}", content)

    output_path = os.path.join(OUTPUT_DIR, filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(page)

print("Сайт собран 🚀")