import json
import os

FILENAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    with open(FILENAME, 'w') as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses):
    category = input("Введите категорию расхода (например, еда, транспорт): ")
    amount = input("Введите сумму: ")
    try:
        amount = float(amount)
    except ValueError:
        print("❌ Ошибка: нужно ввести число.")
        return
    expenses.append({'category': category, 'amount': amount})
    print(f"✅ Добавлено: {category} — {amount} руб.")


def show_expenses(expenses):
    if not expenses:
        print("📭 Пока нет расходов.")
        return

    print("\n📒 Ваши расходы:")
    total = 0
    for e in expenses:
        print(f"- {e['category']}: {e['amount']} руб.")
        total += e['amount']
    print(f"\n💰 Всего потрачено: {total} руб.")


def main():
    expenses = load_expenses()

    while True:
        print("\n=== Меню ===")
        print("1. Показать расходы")
        print("2. Добавить расход")
        print("3. Выход")

        choice = input("Выберите действие (1–3): ")

        if choice == "1":
            show_expenses(expenses)
        elif choice == "2":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "3":
            print("👋 Выход из программы.")
            break
        else:
            print("⚠️ Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
