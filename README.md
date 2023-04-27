# Double It Until Millionaire 💰

This fun little Python script was inspired by the social media challenge: "Do you want (insert amount of money) or double it and give it to the next person ?" 🤑
E.g. https://www.youtube.com/shorts/e4V4juaD-2I

With the power of Python, we can quickly find out how many times we need to double our initial amount to reach the millionaire status! 💸

## Setup

1. Sign up for a free API key at [apilayer.com/marketplace/exchangerates_io](https://apilayer.com/marketplace/exchangerates_io/)
2. Replace `YOUR_API_KEY` in the following line in the `millionarie.py` script with your actual API key:

``python
url = f"https://api.exchangeratesapi.io/latest?base={from_currency}&access_key=YOUR_API_KEY"
```

## How it works

1. Enter an initial amount and the currency symbol.
2. The script will double the amount until it reaches 1 million or more.
3. It will then display how many times it doubled and the final amount.
4. Finally, it will convert the final amount into USD, EUR, and GBP using the latest exchange rates.

## Usage

Before running the script, make sure to install the required module:

```bash
pip install requests

Simply run the `double_until_million.py` script and follow the prompts!

```bash
python double_until_million.py
