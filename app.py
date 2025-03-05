from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys
import importlib.util

# Импортируем чат-модуль
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def import_module(module_path):
    spec = importlib.util.spec_from_file_location(module_path, f"{module_path}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

chat_module = import_module("chat_model")

# Настройка Flask
app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

# Инициализация чат-модели
chat_adapter = chat_module.SearchGPTAdapter()

# Маршрут для главной страницы
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Маршрут для статических файлов
@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

# API для чата
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        messages = data.get('messages', [])
        model = data.get('model', 'openai-large')
        is_continue = data.get('continue', False)
        previous_content = data.get('previous_content', '')
        is_continue_only = data.get('is_continue_only', False)
        random_seed = data.get('random_seed', None)
        
        if not messages:
            return jsonify({'error': 'No messages provided'}), 400

        # Устанавливаем выбранную модель и случайное число
        chat_module.MODEL = model
        if random_seed is not None:
            chat_module.RANDOM_SEED = random_seed

        if is_continue and is_continue_only:
            messages = messages[:-1]
            
            context_message = (
                f"{previous_content}\n\n"
                "[Continue writing from the last word. Add new information naturally, "
                "creating new paragraphs only when it makes sense for the content. "
                "Do not repeat anything that was written before. "
                "Start writing immediately as a direct continuation.]"
            )
            
            messages = [msg for msg in messages if msg['role'] != 'assistant'] + [{
                "role": "assistant",
                "content": context_message
            }]

        model_name, response = chat_adapter.chat_completions(messages)

        if not response:
            return jsonify({'error': 'Failed to get response from AI'}), 500

        if is_continue and is_continue_only:
            response = response.replace("[Continue writing from the last word. Add new information naturally, creating new paragraphs only when it makes sense for the content. Do not repeat anything that was written before. Start writing immediately as a direct continuation.]", "").strip()

        return jsonify({'response': response, 'model': model_name})

    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)