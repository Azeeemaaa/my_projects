import streamlit as st
import requests


def get_rates(base_currency='RUB'):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        if data['result'] == 'success':
            return data['rates']
        else:
            st.warning(f"⚠️ API error: {data}")
            return None
    except Exception as e:
        st.error(f"❌ Failed to fetch rates: {e}")
        return None


def convert(amount, rate):
    return round(amount * rate, 2)


# --- Streamlit UI ---
st.set_page_config(page_title="Currency Converter", page_icon="💱")

st.title("💱 Currency Converter")

st.write("🔄 Getting latest exchange rates...")
rub_rates = get_rates('RUB')
usd_rates = get_rates('USD')
eur_rates = get_rates('EUR')
gbp_rates = get_rates('GBP')

if not all([rub_rates, usd_rates, eur_rates, gbp_rates]):
    st.error("❌ Could not load exchange rates.")
    st.stop()

options = {
    "RUB → USD": rub_rates["USD"],
    "USD → RUB": usd_rates["RUB"],
    "RUB → EUR": rub_rates["EUR"],
    "EUR → RUB": eur_rates["RUB"],
    "RUB → GBP": rub_rates["GBP"],
    "GBP → RUB": gbp_rates["RUB"]
}

choice = st.selectbox("Choose conversion:", list(options.keys()))
amount = st.number_input("Enter amount:", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert(amount, options[choice])
    st.success(f"💰 Result: {amount} {choice[:3]} = {result} {choice[-3:]}")
