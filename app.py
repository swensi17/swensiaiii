from flask import Flask, send_from_directory
from flask_cors import CORS

# Настройка Flask
app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

# Маршрут для главной страницы
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Маршрут для статических файлов
@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)