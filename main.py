import requests

API_KEY = 'your_alpha_vantage_api_key'
BASE_URL = 'https://www.alphavantage.co/query'

portfolio = []

def get_stock_data(symbol):
    params= {
        'function' : 'Global Quote',
        'symbol' : symbol,
        'apikey' : API_KEY,

    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if 'Global Quote' in data:
        return data['Global Quote']
    else:
        print(f"Error occurred while fetching the data for {symbol}")

def add_stock():
    symbol = input("Enter a symbol: ")
    share = int(input("Enter a share: "))

    for stock in portfolio:
        if stock['symbol'] == symbol:
            print("Stock already exit!")
            stock['share'] += share
            return

    portfolio.append({'symbol': symbol,'share': share})
    print(f"Added {share} of symbol {symbol} in your portfolio")

def remove_stock():
    symbol = int(input("Enter a symbol to remove: "))

    for stock in portfolio:
        if stock['symbol'] == symbol:
            portfolio.remove(stock)
            print(f"Stock of symbol {symbol} has been removed from stock")
            return
        print("Symbol not found")

def view_stock():
    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_value = 0
    print("\nYour Portfolio:")
    print("-" * 40)
    print(f"{'Symbol':<10} {'Shares':<10} {'Price':<10} {'Value':<10}")

    for stock in portfolio:
        symbol = stock['symbol']
        shares = stock['share']
        data = get_stock_data(symbol)

        if data:
            price = float(data.get('05. price', 0))
            value = price * shares
            total_value += value
            print(f"{symbol:<10} {shares:<10} ${price:<10.2f} ${value:<10.2f}")
        else:
            print(f"{symbol:<10} {shares:<10} {'N/A':<10} {'N/A':<10}")

    print("-" * 40)
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main_menu():
    while True:
        print("\n Stock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Stock")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_stock()
        elif choice == '4':
            print("Existing the Program!!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == '__main__':
    main_menu()
