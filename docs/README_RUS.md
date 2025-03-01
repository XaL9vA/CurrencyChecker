CurrencyChecker💲
---
---

<div style="margin-bottom: 20px;">
  <button style="background: linear-gradient(to right, #444 45%, #4CAF50 50%); color: white; padding: 5px 5px; border: none; border-radius: 5px; cursor: pointer; font-family: Arial, sans-serif; font-size: 16px; transition: all 0.3s ease;" onclick="window.location.href='README_RUS.md'">
    <span style="padding: 5px;">lang</span> <span style="padding: 5px;">RU</span>
  </button>
  <button style="background: linear-gradient(to right, #444 45%, #f44336 50%); color: white; padding: 5px 5px; border: none; border-radius: 2px; cursor: pointer; font-family: Arial, sans-serif; font-size: 16px; transition: all 0.3s ease;" onclick="window.location.href='README.md'">
    <span style="padding: 5px;">lang</span> <span style="padding: 5px;">ENG</span>
  </button>
</div>

### Содержание:

- [Принцип работы](#title1);
- [Быстрый старт](#title2);
- [Пример начала работы](#title3);
- [Доп. Утилиты](#title4).

---

## Главная функция:

> 🔶 **Возможность получить курс обмена между двумя валютами на определенную дату, записать их в базу данных,
вывести их в файл или терминал**

---

### 🔹Ограничения: ❌

- Дата не может быть раньше 01.01.2000

---

### 🔹<a id="title1">Принцип работы</a>: 🛠

1. Ввод данных:
    - Валюта из;
    - Валюта в;
    - Необходимая дата;
    - Канал вывода.
2. Основная логика:
    - Получение значения конвертации;
    - Вывод в указанный канал.

---

### 🔹<a id="title2">Быстрый старт</a>:🧩

```bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python src/main.py
```

---

### 🔹<a id="title3">Пример начала работы</a>:

```
Hi user, this program converts currencies
Here is the current list:
-------------------------------------------
AUD BGN BRL CAD CHF CNY CZK DKK EUR GBP HKD HRK HUF IDR ILS
INR ISK JPY KRW MXN MYR NOK NZD PHP PLN RON RUB SEK SGD THB
TRY USD ZAR
----------------------------------------------------------------------------
Enter the date in the format - day.month.year   Example: 10.10.2010
The date can't be “today”
The date cannot be less than 01.01.2000
Input:
```

#### Примечание:

На каждом уровне записи аргументов они автоматически проходят проверку на корректность. Если записаны недопустимые
аргументы, программа запросит повторный ввод и выведет причину отказа

---

### 🔹<a id="title4">Доп. Утилиты</a>:💡

#### Линтер:

```bash
flake8 ./ -v
```

---

#### Типизатор:

```bash
mypy ./
```

---

#### Тесты:

```bash
pytest -v
```

---
