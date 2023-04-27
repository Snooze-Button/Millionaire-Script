import requests

# This function converts the given amount from one currency to another
def currency_converter(amount, from_currency, to_currency):
    # Fetch the exchange rate data from the internet
    url = f"https://api.exchangeratesapi.io/latest?base={from_currency}&access_key=YOUR_API_KEY"
    response = requests.get(url)

    # If the data is not fetched successfully, show an error message
    if response.status_code != 200:
        print(f"Unable to fetch exchange rates. Error {response.status_code}")
        return None

    # Get the exchange rates from the data
    rates = response.json().get('rates', {})

    # Calculate and return the converted amount
    return round(amount * rates[to_currency], 2) if to_currency in rates else None

# This function doubles the given amount until it reaches 1 million or more
def double_until_million():
    # Ask the user to enter a number and a currency code
    value_to_double = float(input("Enter a number: "))
    currency_code = input("Enter a currency code (e.g., USD, EUR, GBP): ").upper()

    # Dictionary to map currency codes to their corresponding symbols
    currency_symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£'
    }

    # Get the currency symbol for the entered currency code
    currency_symbol = currency_symbols.get(currency_code, '')

    counter = 0  # This variable keeps track of how many times we have doubled the amount

    # Keep doubling the amount until it reaches 1 million or more
    while value_to_double < 1000000:
        value_to_double = value_to_double * 2
        counter += 1
        print(f' {counter}.  {currency_symbol}{value_to_double}')

    # Show how many times we have doubled the amount and the final amount
    print(f"\nIt doubled {counter} times to reach {currency_symbol}{value_to_double} million")

    # Convert the final amount to USD, EUR, and GBP
    usd_value = currency_converter(value_to_double, currency_code, 'USD')
    eur_value = currency_converter(value_to_double, currency_code, 'EUR')
    gbp_value = currency_converter(value_to_double, currency_code, 'GBP')

    # If the conversion is successful, show the converted amounts
    if usd_value is not None and eur_value is not None and gbp_value is not None:
        print(f"\nCurrency conversion for {currency_symbol}{value_to_double}:")
        print(f"USD: ${usd_value}")
        print(f"EUR: €{eur_value}")
        print(f"GBP: £{gbp_value}")
    else:
        # If the conversion fails, show an error message
        print("\nCurrency conversion failed. Please check your input and try again.")

# Start the program by calling the double_until_million function
if __name__ == "__main__":
    double_until_million()
