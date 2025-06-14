from client import GptSalesClient
from token_1 import api_key
import telebot

# Будет единственная запись срм
crm_record = {
    "name": "Алексей",
    "last_purchase": "Audi Q7",
    "budget": 20000000,
    "deal_status": "В процессе"
}

# Создаём экземпляр клиента
gpt_client = GptSalesClient(api_key=api_key)


if __name__ == "__main__":
    history = []
    print("CRM-запись клиента (пример):")
    print(crm_record)
    print("Введите ваш запрос (например: Хочу Bentley). Для выхода напишите 'выход'.\n")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ["выход", "exit", "quit"]:
            break
        answer = gpt_client.ask(user_input, crm_record, history)
        print("Бот:", answer)
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": answer})