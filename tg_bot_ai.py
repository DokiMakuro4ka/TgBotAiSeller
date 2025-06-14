import telebot
from client import GptSalesClient
from token_1 import api_key
from token_2 import TG_TOKEN

# Симуляция CRM-записи клиента (в реальном проекте — брать из БД/CRM)
crm_record = {
    "name": "Алексей",
    "last_purchase": "Audi Q7",
    "budget": 20000000,
    "deal_status": "В процессе"
}

# Создаём бота и GPT клиент
bot = telebot.TeleBot(TG_TOKEN)
gpt_client = GptSalesClient(api_key=api_key)

# Словарь для хранения истории сообщений для каждого пользователя
user_histories = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
        f"Здравствуйте! Я ваш автомобильный помощник. "
        f"Ваши данные CRM: {crm_record}\n"
        f"Напишите, что вас интересует (например: Хочу Bentley).\n"
        f"Для сброса истории отправьте /reset"
    )

@bot.message_handler(commands=['reset'])
def reset_history(message):
    user_histories[message.from_user.id] = []
    bot.send_message(message.chat.id, "История диалога сброшена.")

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    user_id = message.from_user.id
    if user_id not in user_histories:
        user_histories[user_id] = []

    prompt = message.text
    history = user_histories[user_id]

    try:
        answer = gpt_client.ask(prompt, crm_record, history)
        bot.send_message(message.chat.id, answer)
        # Сохраняем историю для этого пользователя
        history.append({"role": "user", "content": prompt})
        history.append({"role": "assistant", "content": answer})
    except Exception as e:
        print(f"Ошибка: {e}")  # <-- Это выведет текст ошибки в консоль
        bot.send_message(message.chat.id, "Ошибка при обращении к ИИ. Попробуйте позже.")
        
if __name__ == "__main__":
    print("Бот запущен!")
    bot.polling(none_stop=True)