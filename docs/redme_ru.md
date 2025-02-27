CurrencyChecker💲
---
---

| [![ru](https://img.shields.io/badge/lng-ru-green.svg)](https://github.com/XaL9vA/CurrencyChecker/tree/main/docs/readme_ru.md) | [![eng](https://img.shields.io/badge/lng-eng-red.svg)](https://github.com/XaL9vA/CurrencyChecker/tree/main/docs/README.md) |  
|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|   

### Содержание:

- [Принцип работы](#title1);
- [Быстрый старт](#title2);
- [Пример начала работы](#title3);
- [Доп. Утилиты](#title4).

---

## Основная функция:

> 🔶 **Возможность получить курс обмена между двумя валютами на конкретную дату, записать их в базу данных, вывести в
файл или же в терминал**

---

### 🔹Ограничения: ❌

- Дата не может быть раньше 01.01.2000

---

### 🔹<a id="title1">Принцип работы</a>: 🛠

1. Ввод аргументов:
    - Валюта из;
    - Валюта в;
    - Необходимая дата конвертации;
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

На каждом уровне записи аргументов происходит их валидация для корректной работы программы. В случае записи
невалидных аргументов, будет запрошен повторный ввод и выведена причина отказа.
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
