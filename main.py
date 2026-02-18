import requests

# List of supported currency codes (can be expanded easily)
SUPPORTED_CURRENCIES = {
    "USD": "US Dollar",
    "INR": "Indian Rupee",
    "EUR": "Euro",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "SGD": "Singapore Dollar",
    "NZD": "New Zealand Dollar",
    "AED": "UAE Dirham",
    "SAR": "Saudi Riyal",
    "ZAR": "South African Rand",
    "SEK": "Swedish Krona",
    "NOK": "Norwegian Krone",
    "BRL": "Brazilian Real",
    "MXN": "Mexican Peso",
    "THB": "Thai Baht",
    "HKD": "Hong Kong Dollar"
}

API_KEY = "QHIVRmFngbrqINV6OZpC2WyPOotf9Zjj"

def show_supported_currencies():
    print("\n--- Supported Currencies ---")
    for code, name in SUPPORTED_CURRENCIES.items():
        print(f"{code}: {name}")
    print("----------------------------\n")

def get_currency_input(prompt):
    while True:
        currency = input(prompt).upper()
        if currency in SUPPORTED_CURRENCIES:
            return currency
        else:
            print("❌ Invalid currency code. Please select from the list below:")
            show_supported_currencies()

def convert_curr():
    print("🌍 Welcome to the Currency Converter!")
    show_supported_currencies()

    init_currency = get_currency_input("Enter the initial currency (e.g. USD): ")
    target_currency = get_currency_input("Enter the target currency (e.g. INR): ")

    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount <= 0:
                print("❌ Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid numeric amount.")

    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"⚠️ API Error {response.status_code}: {response.text}")
        return

    data = response.json()

    if "result" not in data:
        print("⚠️ Unexpected response format:", data)
        return

    converted_amount = data["result"]
    rate = data.get("info", {}).get("rate", "N/A")

    print(f"\n💱 Conversion Result:")
    print(f"{amount} {init_currency} = {converted_amount:.2f} {target_currency}")
    print(f"Exchange Rate: 1 {init_currency} = {rate} {target_currency}\n")

def main():
    while True:
        convert_curr()
        again = input("Do you want to perform another conversion? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thank you for using the Currency Converter!")
            break

if __name__ == "__main__":
    main()
