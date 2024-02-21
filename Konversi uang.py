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
    st.title("Konverter Mata Uang Asia Tenggara")

    currency_options = ['IDR', 'MYR', 'SGD', 'THB', 'PHP', 'VND']

    from_currency = st.selectbox("Pilih mata uang asal:", currency_options)
    to_currency = st.selectbox("Pilih mata uang tujuan:", currency_options)
    amount = st.number_input("Masukkan jumlah uang yang akan dikonversi:", value=1.0)

    if st.button("Konversi"):
        converted_amount = convert_currency(amount, from_currency, to_currency)
        st.success(f"{amount} {from_currency} setara dengan {converted_amount} {to_currency}")

if __name__ == "__main__":
    main()
