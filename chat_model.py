import json
import requests
import logging

BASE_URL = "https://text.pollinations.ai"

# ТЕКУЩАЯ МОДЕЛЬ
MODEL = "openai-large"
RANDOM_SEED = None

class SearchGPTAdapter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.api_url = f"{BASE_URL}/openai"
        self.headers = {
            "Content-Type": "application/json",
        }

    def chat_completions(self, messages):
        try:
            # Проверяем наличие системного сообщения
            has_system_message = any(msg.get('role') == 'system' for msg in messages)
            
            # Если системного сообщения нет, добавляем стандартное
            if not has_system_message:
                messages.insert(0, {
                    "role": "system",
                    "content": "Ты обычный AI ассистент. Отвечай четко и по делу, будь вежливым и полезным."
                })

            payload = {
                "model": MODEL,
                "messages": messages,
                "seed": RANDOM_SEED
            }

            response = requests.post(
                self.api_url,
                headers=self.headers,
                data=json.dumps(payload),
                timeout=60.0
            )
            response.raise_for_status()
            api_response = response.json()

            model_name = api_response.get("model")
            response_content = api_response["choices"][0]["message"]["content"]

            return model_name, response_content

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request error: {e}")
            return None, None
        except (KeyError, IndexError) as e:
            self.logger.error(f"Error parsing API response: {e}")
            return None, None
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON response: {e}")
            return None, None