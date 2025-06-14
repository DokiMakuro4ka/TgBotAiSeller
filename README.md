<div align="center">

# Telegram AI Seller Bot

</div>

<div align="center">

<table width="100%">
<tr>
<td align="center" width="50%"><b>🇷🇺 Описание</b></td>
<td align="center" width="50%"><b>🇬🇧 Description</b></td>
</tr>
<tr>
<td align="justify" width="50%" style="text-align:justify;">

Этот проект — Telegram-бот-продавец, использующий искусственный интеллект (GPT/OpenAI) для автоматизации диалогов с клиентами и повышения эффективности продаж. Бот анализирует запросы пользователей, использует данные CRM для персонализации предложений, сохраняет историю диалогов и может выполнять апселл услуг или товаров. Проект легко адаптируется под различные ниши (авто, недвижимость, услуги и др.).

</td>
<td align="justify" width="50%" style="text-align:justify;">

This project is a Telegram AI sales bot that leverages GPT/OpenAI to automate customer interactions and boost sales efficiency. The bot analyzes user requests, utilizes CRM data for personalized offers, stores conversation history, and can upsell products or services. The project is easily adaptable for various domains (automotive, real estate, services, etc.).

</td>
</tr>
</table>

---

<table width="100%">
<tr>
<td align="center" width="50%"><b>🇷🇺 Файлы проекта</b></td>
<td align="center" width="50%"><b>🇬🇧 Project Files</b></td>
</tr>
<tr>
<td align="justify" width="50%" style="text-align:justify;">

- <b>main.py</b> — основной файл с логикой Telegram-бота и интеграцией с AI.
- <b>gpt_client.py</b> — модуль для работы с OpenAI/GPT API.
- <b>crm_data.py</b> — пример модели или интерфейса для подгрузки CRM-данных.
- <b>token.py</b> — файл с токенами API (Telegram и OpenAI).
- <b>requirements.txt</b> — зависимости для запуска проекта.

</td>
<td align="justify" width="50%" style="text-align:justify;">

- <b>main.py</b> — main file with Telegram bot logic and AI integration.
- <b>gpt_client.py</b> — module for interaction with OpenAI/GPT API.
- <b>crm_data.py</b> — example model or interface for CRM data loading.
- <b>token.py</b> — file with API tokens (Telegram and OpenAI).
- <b>requirements.txt</b> — dependencies for running the project.

</td>
</tr>
</table>

---

<table width="100%">
<tr>
<td align="center" width="50%"><b>🇷🇺 Быстрый старт</b></td>
<td align="center" width="50%"><b>🇬🇧 Quick Start</b></td>
</tr>
<tr>
<td align="justify" width="50%" style="text-align:justify;">

<b>1. Клонируйте репозиторий</b>

```sh
git clone https://github.com/DokiMakuro4ka/TgBotAiSeller
cd TgBotAiSeller
```

<b>2. Установите зависимости</b>

```sh
pip install -r requirements.txt
```

<b>Минимальный requirements.txt:</b>
```
pyTelegramBotAPI
openai
```

<b>3. Настройте ключи</b>

- В <code>token.py</code> укажите ваши ключи:
  ```python
  OPENAI_API_KEY = "your-openai-api-key"
  TELEGRAM_TOKEN = "your-telegram-bot-token"
  ```

<b>4. Запустите бота</b>

```sh
python main.py
```

</td>
<td align="justify" width="50%" style="text-align:justify;">

<b>1. Clone the repository</b>

```sh
git clone https://github.com/DokiMakuro4ka/TgBotAiSeller
cd TgBotAiSeller
```

<b>2. Install dependencies</b>

```sh
pip install -r requirements.txt
```

<b>Minimal requirements.txt:</b>
```
pyTelegramBotAPI
openai
```

<b>3. Configure keys</b>

- In <code>token.py</code>, set your keys:
  ```python
  OPENAI_API_KEY = "your-openai-api-key"
  TELEGRAM_TOKEN = "your-telegram-bot-token"
  ```

<b>4. Run the bot</b>

```sh
python main.py
```

</td>
</tr>
</table>

---

<table width="100%">
<tr>
<td align="center" width="50%"><b>🇷🇺 Как работает бот</b></td>
<td align="center" width="50%"><b>🇬🇧 How the bot works</b></td>
</tr>
<tr>
<td align="justify" width="50%" style="text-align:justify;">

- После запуска бот приветствует пользователя и может показать пример CRM-записи.
- Пользователь отправляет текст — бот отвечает с учётом CRM-информации.
- Для сброса истории диалога используйте команду <b>/reset</b>.
- История диалога индивидуальна для каждого пользователя (по user_id), хранится в памяти или базе (зависит от реализации).
- Бот может быть расширен для интеграции с реальной CRM.

</td>
<td align="justify" width="50%" style="text-align:justify;">

- After launch, the bot greets the user and can show a sample CRM record.
- The user sends text — the bot replies using CRM information.
- Use the <b>/reset</b> command to reset the dialog history.
- Dialog history is stored per user (by user_id) in memory or database (implementation-dependent).
- The bot can be extended to integrate with a real CRM.

</td>
</tr>
</table>

---

<table width="100%">
<tr>
<td align="center" colspan="2"><b>🇬🇧 Sample CRM record used in the bot</b></td>
</tr>
<tr>
<td align="left" colspan="2" style="text-align:left;">

```python
crm_record = {
    "name": "Иван",
    "last_purchase": "Tesla Model 3",
    "budget": 5000000,
    "deal_status": "Lead"
}
```

</td>
</tr>
</table>

---

<table width="100%">
<tr>
<td align="center" width="50%"><b>🇷🇺 Безопасность</b></td>
<td align="center" width="50%"><b>🇬🇧 Security</b></td>
</tr>
<tr>
<td align="justify" width="50%" style="text-align:justify;">

<b>Не публикуйте ваши реальные API-ключи и токены в публичных репозиториях!</b>
- Добавьте <code>token.py</code> в <code>.gitignore</code> перед публикацией.
- Для production используйте переменные окружения для хранения ключей.

</td>
<td align="justify" width="50%" style="text-align:justify;">

<b>Do not publish your real API keys or tokens in public repositories!</b>
- Add <code>token.py</code> to <code>.gitignore</code> before publishing.
- Use environment variables for key storage in production.

</td>
</tr>
</table>

---

<table width="100%">
<tr>
<td align="center" width="50%"><b>🇷🇺 Возможные доработки</b></td>
<td align="center" width="50%"><b>🇬🇧 Possible Improvements</b></td>
</tr>
<tr>
<td align="justify" width="50%" style="text-align:justify;">

- Интеграция с реальной CRM и базой данных.
- Хранение истории диалогов в базе.
- Обработка вложений (фото, файлы).
- Расширение логики апселла и рекомендаций.
- Мультиаккаунтная поддержка.
- Мультиязычность.

</td>
<td align="justify" width="50%" style="text-align:justify;">

- Integration with a real CRM and database.
- Store dialog history in DB.
- Attachments (photos, files) support.
- Extended upsell/recommendation logic.
- Multi-account support.
- Multilingual support.

</td>
</tr>
</table>

</div>
