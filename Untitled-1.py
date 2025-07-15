# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import cohere
import os
import random

# CORRECTED LINE: Get the API key from the environment variable named 'COHERE_API_KEY'
COHERE_API_KEY = os.getenv('COHERE_API_KEY')

if COHERE_API_KEY is None:
    print("Помилка: API ключ Cohere не знайдено.")
    print("Будь ласка, встановіть змінну середовища COHERE_API_KEY.")
    exit()

co = cohere.Client(COHERE_API_KEY)

def generate_joke_with_cohere():
    prompt = "Напиши короткий, смішний анекдот українською мовою."
    try:
        response = co.chat(
            model="command-r-plus",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=100,
        )

        if response.message and response.message.content:
            return response.message.content
        else:
            return "Не вдалося згенерувати анекдот. Спробуйте ще раз."
    except Exception as e:
        # Print the full exception for more details
        print(f"Помилка: {e}", file=sys.stderr)
        return f"Виникла помилка при зверненні до Cohere API: {e}"

# Example of how to call the function (optional, for testing)
if __name__ == "__main__":
    joke = generate_joke_with_cohere()
    print(joke)