📊 Stock Portfolio Tracker

A simple yet advanced Tkinter-based desktop application that allows users to track stock investments, calculate portfolio values, visualize data with graphs, and save results in multiple formats.

This project includes:

GUI built with Tkinter

Data persistence with JSON

Logging system

CSV/TXT/JSON export options

Portfolio visualization using Matplotlib

Ability to add custom stocks manually

🚀 Features
✅ 1. Select & Calculate Investment

Choose a stock from dropdown

Enter the number of shares

App calculates total investment value

Displays detailed result instantly

✅ 2. Auto-Saving & Loading Stock Prices

Loads prices from stocks.json

If file doesn’t exist, it creates one with default stock prices

✅ 3. Export Results

You can export the latest calculation to:

TXT (investment_result.txt)

CSV (investment_result.csv)

JSON (investment_result.json)

✅ 4. Add New Stocks

You can manually add new stock symbols and prices.
Changes are saved permanently in stocks.json.

✅ 5. View Portfolio Summary

Displays all investments in a TreeView table including:

Price

Quantity

Total value

✅ 6. Portfolio Graph

Visualizes your holdings through a pie chart using Matplotlib.

✅ 7. Logging System

All important activities are recorded in portfolio_log.txt:

App start/close

Calculation logs

Errors

Stock additions

📂 Project Structure
|-- main.py                  # Main TKinter Application
|-- stocks.json              # Stock price storage
|-- portfolio_log.txt        # Auto-generated logs
|-- investment_result.txt    # Saved TXT output
|-- investment_result.csv    # Saved CSV output
|-- investment_result.json   # Saved JSON output
|-- README.md                # Documentation

🧩 Technologies Used

Python

Tkinter – GUI

Matplotlib – Graphs

JSON – Data storage

CSV – Export

Logging – Activity tracking

🤝 Contributing

Feel free to submit issues or pull requests!
