CurrencyChecker💲
---
---

[![en](https://img.shields.io/badge/🌐_lang-ENG-2ECC71.svg?style=for-the-badge&logo=globe&logoColor=white)](./README.md)
[![ru](https://img.shields.io/badge/🌐_lang-RU-E74C3C.svg?style=for-the-badge&logo=globe&logoColor=white)](./README_RUS.md)

### Contents:

- [Principle of operation](#title1);
- [Quick start](#title2);
- [Example of the start of work](#title3);
- [Add. Utilities](#title4).

---

## Main function:

> 🔶 **The ability to get the exchange rate between two currencies for a specific date, record them in the database,
output them to a file or to the terminal**

---

### 🔹Limitations: ❌

- The date cannot be earlier than 01.01.2000

---

### 🔹<a id="title1">Principle of operation</a>: 🛠

1. Argument input:
    - Currency from;
    - Currency in;
    - The required conversion date;
    - Output channel.
2. Basic logic:
    - Receipt of the conversion value;
    - Output to the specified channel.

---

### 🔹<a id="title2">Quick start</a>:🧩

```bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python src/main.py
```

---

### 🔹<a id="title3">Example of the start of work</a>:

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

#### Note:

At each level of writing arguments, they are validated for correct operation of the program. If invalid arguments are
written, a re-entry will be requested and the reason for the failure will be displayed.

---

### 🔹<a id="title4">Add. Utilities</a>:💡

#### Linter:

```bash
flake8 ./ -v
```

---

#### Typitizer:

```bash
mypy ./
```

---

#### Tests:

```bash
pytest -v
```

---
