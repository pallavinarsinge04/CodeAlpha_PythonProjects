import csv

def stock_portfolio():
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 310}
    portfolio = {}
    total_value = 0

    print("📈 Welcome to Stock Portfolio Tracker")
    while True:
        stock = input("Enter stock symbol (AAPL, TSLA, GOOG, MSFT or 'done'): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Invalid stock symbol.")
            continue
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty

    print("\n💰 Investment Summary:")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        total_value += value
        print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

    print(f"\n📊 Total Investment Value = ${total_value}")

    save = input("Save results to CSV? (y/n): ").lower()
    if save == 'y':
        with open("portfolio.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for s, q in portfolio.items():
                writer.writerow([s, q, stock_prices[s], stock_prices[s]*q])
            writer.writerow(["Total", "", "", total_value])
        print("✅ Portfolio saved to portfolio.csv")

stock_portfolio()
