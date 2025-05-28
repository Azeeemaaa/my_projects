import requests


def get_rates(base_currency="RUB"):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        if data["result"] == "success":
            return data["rates"]
        else:
            print("⚠️ API error:", data)
            return None
    except Exception as e:
        print("❌ Failed to fetch rates:", e)
        return None


def convert(amount, rate):
    return round(amount * rate, 2)


def show_menu():
    print("\n=== Currency Converter ===")
    print("1. RUB → USD")
    print("2. USD → RUB")
    print("3. RUB → EUR")
    print("4. EUR → RUB")
    print("5. RUB → GBP")
    print("6. GBP → RUB")
    print("7. Exit")


def main():
    print("🔄 Fetching latest rates...")
    rub_rates = get_rates("RUB")
    usd_rates = get_rates("USD")
    eur_rates = get_rates("EUR")
    gbp_rates = get_rates("GBP")

    if not all([rub_rates, usd_rates, eur_rates, gbp_rates]):
        print("❌ Could not load exchange rates.")
        return

    while True:
        show_menu()
        choice = input("Choose an option (1–7): ")

        if choice == '7':
            print("👋 Exiting the program.")
            break

        amount_input = input("Enter amount to convert: ")

        try:
            amount = float(amount_input)
        except ValueError:
            print("❌ Invalid number. Try again.")
            continue

        if choice == '1':
            print(f"{amount} RUB = {convert(amount, rub_rates['USD'])} USD")
        elif choice == '2':
            print(f"{amount} USD = {convert(amount, usd_rates['RUB'])} RUB")
        elif choice == '3':
            print(f"{amount} RUB = {convert(amount, rub_rates['EUR'])} EUR")
        elif choice == '4':
            print(f"{amount} EUR = {convert(amount, eur_rates['RUB'])} RUB")
        elif choice == '5':
            print(f"{amount} RUB = {convert(amount, rub_rates['GBP'])} GBP")
        elif choice == '6':
            print(f"{amount} GBP = {convert(amount, gbp_rates['RUB'])} RUB")
        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
