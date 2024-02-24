import streamlit as st
import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"][target_currency]
    return exchange_rate

def convert_currency(amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    st.title("Konversi Mata Uang yang Menarik")
    st.image("https://cdn.icon-icons.com/icons2/317/PNG/512/coins_icon_191276.png", use_column_width=True)

    currency_options = ['IDR', 'MYR', 'SGD', 'THB', 'PHP', 'VND']

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Mata Uang Asal")
        from_currency = st.selectbox("", currency_options)
    with col2:
        st.subheader("Mata Uang Tujuan")
        to_currency = st.selectbox("", currency_options)

    amount = st.number_input("Jumlah Uang yang Akan Dikonversi", value=1.0, min_value=0.01)

    if st.button("Konversi"):
        converted_amount = convert_currency(amount, from_currency, to_currency)
        st.success(f"{amount} {from_currency} setara dengan {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
