# ============================================================
# CodeAlpha Internship — Task 2: Stock Portfolio Tracker
# Author  : CHIDEK PATTANAIK | ID: CA/DF1/86102
# Domain  : Python Programming
# ============================================================

import csv
import os

# ── Hardcoded stock prices (USD) ───────────────────────────
STOCK_PRICES = {
    "AAPL":  180.0,   # Apple
    "TSLA":  250.0,   # Tesla
    "GOOGL": 140.0,   # Alphabet
    "AMZN":  185.0,   # Amazon
    "MSFT":  415.0,   # Microsoft
    "NFLX":  630.0,   # Netflix
    "META":  510.0,   # Meta
    "NVDA":  875.0,   # NVIDIA
}

OUTPUT_FILE = "portfolio_result.csv"


def show_available_stocks():
    """Print all available stocks and their prices."""
    print("\n  Available Stocks:")
    print("  " + "-" * 30)
    for ticker, price in STOCK_PRICES.items():
        print(f"  {ticker:<8}  ${price:>8.2f}")
    print("  " + "-" * 30)


def get_portfolio():
    """Prompt the user to enter stocks and quantities."""
    portfolio = {}
    print("\n  Enter stock ticker and quantity (type 'done' to finish).")

    while True:
        ticker = input("\n  Stock ticker (e.g. AAPL): ").strip().upper()
        if ticker == "DONE":
            break
        if ticker not in STOCK_PRICES:
            print(f"  ⚠  '{ticker}' not found. Choose from the list above.")
            continue

        try:
            qty = int(input(f"  Quantity of {ticker}: ").strip())
            if qty <= 0:
                print("  ⚠  Quantity must be a positive number.")
                continue
        except ValueError:
            print("  ⚠  Please enter a valid whole number.")
            continue

        # Accumulate quantity if stock entered more than once
        portfolio[ticker] = portfolio.get(ticker, 0) + qty
        print(f"  ✅  Added {qty} share(s) of {ticker}.")

    return portfolio


def display_portfolio(portfolio):
    """Display a formatted summary and return the total value."""
    if not portfolio:
        print("\n  No stocks in portfolio.")
        return 0.0

    print("\n" + "=" * 50)
    print("         📊  YOUR PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"  {'Ticker':<8} {'Qty':>6} {'Price':>10} {'Value':>12}")
    print("  " + "-" * 40)

    total = 0.0
    rows  = []

    for ticker, qty in portfolio.items():
        price = STOCK_PRICES[ticker]
        value = price * qty
        total += value
        print(f"  {ticker:<8} {qty:>6} ${price:>9.2f} ${value:>11.2f}")
        rows.append((ticker, qty, price, value))

    print("  " + "-" * 40)
    print(f"  {'TOTAL':>27}  ${total:>11.2f}")
    print("=" * 50)

    return total, rows


def save_to_csv(rows, total):
    """Save portfolio data to a CSV file."""
    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Ticker", "Quantity", "Price (USD)", "Value (USD)"])
        for row in rows:
            writer.writerow(row)
        writer.writerow([])
        writer.writerow(["TOTAL", "", "", f"{total:.2f}"])
    print(f"\n  💾  Portfolio saved to '{OUTPUT_FILE}'.")


def main():
    print("\n" + "=" * 50)
    print("   💼  CodeAlpha Stock Portfolio Tracker")
    print("=" * 50)

    show_available_stocks()
    portfolio = get_portfolio()

    if not portfolio:
        print("\n  No stocks entered. Exiting.")
        return

    result = display_portfolio(portfolio)
    if not result:
        return

    total, rows = result

    save = input("\n  Save results to CSV? (y/n): ").strip().lower()
    if save == "y":
        save_to_csv(rows, total)

    print("\n  Thank you for using the Stock Portfolio Tracker!\n")


if __name__ == "__main__":
    main()
