from openai import OpenAI
from token_1 import api_key

class GptSalesClient:
    """
    Класс-обёртка для общения с GPT-моделью с учётом CRM-данных.
    """

    def __init__(self, api_key, base_url="https://openrouter.ai/api/v1", model="openai/gpt-3.5-turbo"):
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key,
        )
        self.model = model

    def ask(self, prompt, crm, history=None):
        """
        Отправляет запрос в GPT с учётом CRM-данных и истории диалога.

        :param prompt: Запрос пользователя
        :param crm: Словарь с CRM-данными
        :param history: История переписки (список сообщений)
        :return: Ответ GPT
        """
        system_msg = (
            f"Ты помощник-продажник автосалона. "
            f"Тебя зовут Алексей. "
            f"Имя клиента: {crm.get('name', 'Неизвестно')}. "
            f"Последняя покупка клиента: {crm.get('last_purchase', 'нет данных')}. "
            f"Бюджет клиента: {crm.get('budget', 'неизвестно')} руб. "
            f"Статус сделки: {crm.get('deal_status', 'нет данных')}. "
            f"Отвечай дружелюбно, делай апселл, если возможно, и всегда учитывай эти параметры."
        )
        messages = [{"role": "system", "content": system_msg}]
        if history:
            messages += history
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        answer = response.choices[0].message.content.strip()
        return answer