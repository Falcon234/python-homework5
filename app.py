from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Головна сторінка</title>
        <style>
            body { font-family: Arial, sans-serif; background: #0f111a; color: white; text-align: center; padding: 50px; }
            h1 { color: #00d2ff; }
            nav a { color: #ff5500; margin: 0 15px; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Головна</a> | <a href="/about/">Про нас</a> | <a href="/services/">Послуги</a> | <a href="/contact/">Контакти</a>
        </nav>
        <hr style="border-color: #333; margin: 30px 0;">
        <h1>Вітаємо на нашому Flask-сайті!</h1>
        <p>Це головна сторінка веб-додатка, створена повністю на Python без використання сторонніх шаблонів.</p>
    </body>
    </html>
    """

@app.route('/about/')
def about():
    return """
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Про нас</title>
        <style>
            body { font-family: Arial, sans-serif; background: #0f111a; color: white; text-align: center; padding: 50px; }
            h1 { color: #00d2ff; }
            nav a { color: #ff5500; margin: 0 15px; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Головна</a> | <a href="/about/">Про нас</a> | <a href="/services/">Послуги</a> | <a href="/contact/">Контакти</a>
        </nav>
        <hr style="border-color: #333; margin: 30px 0;">
        <h1>Про нас</h1>
        <p>Ми — команда незалежних розробників та ентузіастів, які створюють інтерактивні веб-платформи та інструменти автоматизації.</p>
    </body>
    </html>
    """

@app.route('/services/')
def services():
    return """
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Наші послуги</title>
        <style>
            body { font-family: Arial, sans-serif; background: #0f111a; color: white; text-align: center; padding: 50px; }
            h1 { color: #00d2ff; }
            nav a { color: #ff5500; margin: 0 15px; text-decoration: none; font-weight: bold; }
            ul { list-style: none; padding: 0; }
            li { margin: 10px 0; font-size: 1.1rem; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Головна</a> | <a href="/about/">Про нас</a> | <a href="/services/">Послуги</a> | <a href="/contact/">Контакти</a>
        </nav>
        <hr style="border-color: #333; margin: 30px 0;">
        <h1>Опис послуг</h1>
        <ul>
            <li>🚀 Розробка кастомних веб-застосунків на Python / Flask</li>
            <li>📊 Створення інтерактивних інтерфейсів (JavaScript, CSS)</li>
            <li>🤖 Програмування мікроконтролерів та систем автоматизації</li>
        </ul>
    </body>
    </html>
    """

@app.route('/contact/')
def contact():
    return """
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Контакти</title>
        <style>
            body { font-family: Arial, sans-serif; background: #0f111a; color: white; text-align: center; padding: 50px; }
            h1 { color: #00d2ff; }
            nav a { color: #ff5500; margin: 0 15px; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Головна</a> | <a href="/about/">Про нас</a> | <a href="/services/">Послуги</a> | <a href="/contact/">Контакти</a>
        </nav>
        <hr style="border-color: #333; margin: 30px 0;">
        <h1>Зв'язок із нами</h1>
        <p>Email для запитів: <strong>support@example.com</strong></p>
        <p>Telegram: <strong>@dev_team_hub</strong></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
