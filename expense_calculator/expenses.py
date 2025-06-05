import streamlit as st
import json
import os

FILENAME = "expenses.json"


# Загрузка данных из файла
def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            return json.load(f)
    return []


# Сохранение данных в файл
def save_expenses(expenses):
    with open(FILENAME, 'w') as f:
        json.dump(expenses, f, indent=2)


# Интерфейс Streamlit
st.set_page_config(page_title="Учёт расходов 💸")

st.title("💸 Учёт расходов")
st.write("Добавляй расходы, и приложение посчитает общую сумму!")

# Загружаем текущие расходы
if "expenses" not in st.session_state:
    st.session_state.expenses = load_expenses()

# Форма для добавления нового расхода
with st.form("add_expense"):
    category = st.text_input("Категория (еда, транспорт и т.д.)")
    amount = st.text_input("Сумма")
    submitted = st.form_submit_button("Добавить")

    if submitted:
        try:
            amount = float(amount)
            st.session_state.expenses.append(
                {"category": category, "amount": amount})
            save_expenses(st.session_state.expenses)
            st.success(f"✅ Добавлено: {category} — {amount} $.")
        except ValueError:
            st.error("❌ Ошибка: сумма должна быть числом.")

# Показать все расходы
st.subheader("📒 Ваши расходы:")

if not st.session_state.expenses:
    st.info("Пока нет ни одного расхода.")
else:
    total = 0
    for item in st.session_state.expenses:
        st.write(f"- {item['category']}: {item['amount']} руб.")
        total += item['amount']

    st.markdown(f"### 💰 Всего потрачено: **{total} $.**")
