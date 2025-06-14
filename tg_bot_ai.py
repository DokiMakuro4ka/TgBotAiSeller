import telebot
from client import GptSalesClient
import os

# Получаем токены из переменных окружения для безопасности
api_key = os.environ.get("OPENAI_API_KEY")
TG_TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Создаём бота и GPT клиент
bot = telebot.TeleBot(TG_TOKEN)
gpt_client = GptSalesClient(api_key=api_key)

# Словарь для хранения истории сообщений для каждого пользователя
user_histories = {}
# Словарь для хранения CRM-данных каждого пользователя
user_crm = {}

def get_crm_str(crm):
    return (
        f"Имя: {crm.get('name', '—')}\n"
        f"Последняя покупка: {crm.get('last_purchase', '—')}\n"
        f"Бюджет: {crm.get('budget', '—')} ₽\n"
        f"Статус сделки: {crm.get('deal_status', '—')}"
    )

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    user_histories[user_id] = []
    user_crm[user_id] = {"step": 0, "data": {}}
    bot.send_message(
        message.chat.id,
        "👋 <b>Здравствуйте!</b>\n\n"
        "Я — ваш автомобильный AI-ассистент.\n"
        "Чтобы подобрать для вас лучший автомобиль, давайте заполним ваши данные CRM.\n\n"
        "<b>Как к вам обращаться? (Ваше имя)</b>",
        parse_mode="HTML"
    )

@bot.message_handler(commands=['reset'])
def reset_history(message):
    user_id = message.from_user.id
    user_histories[user_id] = []
    user_crm[user_id] = {"step": 0, "data": {}}
    bot.send_message(message.chat.id, "История диалога и CRM-данные сброшены. Напишите /start, чтобы начать заново.")

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    user_id = message.from_user.id

    # --- CRM заполнение ---
    if user_id in user_crm and user_crm[user_id]["step"] < 4:
        step = user_crm[user_id]["step"]
        data = user_crm[user_id]["data"]

        if step == 0:
            data["name"] = message.text.strip()
            user_crm[user_id]["step"] += 1
            bot.send_message(message.chat.id, "🚗 <b>Какую машину вы покупали последней?</b>", parse_mode="HTML")
            return
        elif step == 1:
            data["last_purchase"] = message.text.strip()
            user_crm[user_id]["step"] += 1
            bot.send_message(message.chat.id, "💸 <b>Какой у вас примерный бюджет? (в рублях)</b>", parse_mode="HTML")
            return
        elif step == 2:
            try:
                budget = int("".join(filter(str.isdigit, message.text.strip())))
                data["budget"] = budget
            except Exception:
                bot.send_message(message.chat.id, "Пожалуйста, введите бюджет числом, например: 3000000")
                return
            user_crm[user_id]["step"] += 1
            bot.send_message(message.chat.id, "📈 <b>Статус вашей сделки?</b> (например: В процессе, Завершена, Новая заявка)", parse_mode="HTML")
            return
        elif step == 3:
            data["deal_status"] = message.text.strip()
            user_crm[user_id]["step"] += 1
            bot.send_message(
                message.chat.id,
                "👏 <b>Спасибо!</b> Ваши CRM-данные сохранены:\n\n"
                f"{get_crm_str(data)}\n\n"
                "Теперь напишите, что вас интересует (например: Хочу Bentley).\n"
                "Для сброса истории и CRM-данных отправьте /reset",
                parse_mode="HTML"
            )
            return

    # --- Диалог с GPT ---
    if user_id not in user_histories:
        user_histories[user_id] = []
    if user_id not in user_crm or user_crm[user_id]["step"] < 4:
        bot.send_message(message.chat.id, "Пожалуйста, сначала заполните CRM-данные. Напишите /start.")
        return

    prompt = message.text
    history = user_histories[user_id]
    crm_record = user_crm[user_id]["data"]

    try:
        answer = gpt_client.ask(prompt, crm_record, history)
        bot.send_message(message.chat.id, answer)
        # Сохраняем историю для этого пользователя
        history.append({"role": "user", "content": prompt})
        history.append({"role": "assistant", "content": answer})
    except Exception as e:
        print(f"Ошибка: {e}")
        bot.send_message(message.chat.id, "Ошибка при обращении к ИИ. Попробуйте позже.")
        
if __name__ == "__main__":
    print("Бот запущен!")
    bot.polling(none_stop=True)
