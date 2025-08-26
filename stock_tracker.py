# Hardcoded stock prices
stock_prices = {
    'AAPL': 175.12,
    'GOOGL': 135.86,
    'MSFT': 328.45,
    'TSLA': 249.75,
    'AMZN': 143.22,
    'NVDA': 485.89
}

# Get user input
stock_name = input("Enter the stock symbol (e.g., AAPL): ").upper()
quantity = int(input("Enter the number of shares: "))

# Calculate total investment
if stock_name in stock_prices:
    price_per_share = stock_prices[stock_name]
    total_value = price_per_share * quantity

    # Display result
    print(f"\nYou own {quantity} shares of {stock_name} at ${price_per_share:.2f} each.")
    print(f"Total investment value: ${total_value:.2f}")

    # Ask if user wants to save the result
    save_option = input("\nDo you want to save the result to a file? (yes/no): ").lower()

    if save_option == 'yes':
        file_format = input("Choose file format: 'txt' or 'csv': ").lower()
        if file_format == 'txt':
            with open('investment_result.txt', 'w') as file:
                file.write(f"Stock: {stock_name}\n")
                file.write(f"Quantity: {quantity}\n")
                file.write(f"Price per share: ${price_per_share:.2f}\n")
                file.write(f"Total investment value: ${total_value:.2f}\n")
            print("Result saved to 'investment_result.txt'")
        elif file_format == 'csv':
            with open('investment_result.csv', 'w') as file:
                file.write("Stock,Quantity,Price per Share,Total Investment\n")
                file.write(f"{stock_name},{quantity},{price_per_share:.2f},{total_value:.2f}\n")
            print("Result saved to 'investment_result.csv'")
        else:
            print("Invalid file format. Result not saved.")
else:
    print(f"\nStock symbol '{stock_name}' not found in the price list.")
