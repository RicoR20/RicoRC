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
    print("Selamat datang di konverter mata uang Asia Tenggara!")
    print("Mata uang yang tersedia: IDR (Rupiah Indonesia), MYR (Ringgit Malaysia), SGD (Dolar Singapura), THB (Baht Thailand), PHP (Peso Filipina), VND (Dong Vietnam)")
    from_currency = input("Masukkan kode mata uang asal: ").upper()
    to_currency = input("Masukkan kode mata uang tujuan: ").upper()
    amount = float(input("Masukkan jumlah uang yang akan dikonversi: "))
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} setara dengan {converted_amount} {to_currency}")

if __name__ == "__main__":
    main()
