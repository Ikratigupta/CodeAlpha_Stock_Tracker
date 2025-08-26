# Stock Portfolio Tracker

This is a simple **Python** project developed as part of my internship at **CodeAlpha**. It allows users to calculate their total investment in stocks based on predefined stock prices using basic Python features.

---

## Project Objective

Build a console-based stock tracker that:
- Accepts user input for stock symbol and quantity
- Uses a hardcoded dictionary of stock prices
- Calculates the total investment value
- Optionally saves the result to a `.txt` or `.csv` file

---

## Technologies & Concepts Used

- Python (standard library)
- Dictionaries for storing stock prices
- Input/output operations
- Basic arithmetic calculations
- File handling for saving results
- Conditional statements for logic flow

---

## How It Works

1. User inputs a stock symbol (e.g., `AAPL`) and number of shares.
2. The program looks up the stock price from a hardcoded dictionary.
3. Calculates the total investment value.
4. Asks the user if they want to save the result.
5. Saves the result in `.txt` or `.csv` format if requested.

---

## Example Stock Prices

```python
stock_prices = {
    'AAPL': 175.12,
    'GOOGL': 135.86,
    'MSFT': 328.45,
    'TSLA': 249.75,
    'AMZN': 143.22,
    'NVDA': 485.89
}
## Sample output

Enter the stock symbol (e.g., AAPL): TSLA
Enter the number of shares: 10

You own 10 shares of TSLA at $249.75 each.
Total investment value: $2497.50

Do you want to save the result to a file? (yes/no): yes
Choose file format: 'txt' or 'csv': txt

Result saved to 'investment_result.txt'
