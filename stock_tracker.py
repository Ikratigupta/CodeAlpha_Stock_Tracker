import tkinter as tk
from tkinter import ttk, messagebox
import csv
import json
import logging
import matplotlib.pyplot as plt

# -------------------------------------------------
# LOGGING SYSTEM
# -------------------------------------------------
logging.basicConfig(
    filename="portfolio_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Application Started")

# -------------------------------------------------
# Load or Create Stock File
# -------------------------------------------------
try:
    with open("stocks.json", "r") as file:
        stock_prices = json.load(file)
except:
    stock_prices = {
        'AAPL': 175.12,
        'GOOGL': 135.86,
        'MSFT': 328.45,
        'TSLA': 249.75,
        'AMZN': 143.22,
        'NVDA': 485.89
    }
    with open("stocks.json", "w") as file:
        json.dump(stock_prices, file, indent=4)

portfolio = {}  # Store calculated investments

# -------------------------------------------------
# Functions
# -------------------------------------------------
def calculate_investment():
    stock_name = stock_var.get().upper()

    try:
        quantity = int(quantity_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid number for quantity.")
        logging.error("Invalid quantity entered")
        return

    if stock_name not in stock_prices:
        messagebox.showerror("Error", "Stock not found.")
        logging.error(f"Stock {stock_name} not found")
        return

    price = stock_prices[stock_name]
    total = price * quantity

    result_label.config(text=f"{quantity} shares of {stock_name} @ ${price:.2f}\nTotal: ${total:.2f}")

    portfolio[stock_name] = {"quantity": quantity, "price": price, "total": total}

    global last_result
    last_result = (stock_name, quantity, price, total)

    logging.info(f"Calculated investment for {stock_name} | Quantity: {quantity} | Total: {total}")

def save_result(file_type):
    if not last_result:
        messagebox.showwarning("No Data", "Calculate first.")
        return

    stock_name, quantity, price, total = last_result

    if file_type == "txt":
        with open("investment_result.txt", "w") as f:
            f.write(f"Stock: {stock_name}\nQuantity: {quantity}\nPrice: {price}\nTotal: {total}")
        messagebox.showinfo("Saved", "Saved as TXT")
        logging.info("Saved result as TXT")

    elif file_type == "csv":
        with open("investment_result.csv", "w", newline='') as f:
            w = csv.writer(f)
            w.writerow(["Stock", "Quantity", "Price", "Total"])
            w.writerow([stock_name, quantity, price, total])
        messagebox.showinfo("Saved", "Saved as CSV")
        logging.info("Saved result as CSV")

    elif file_type == "json":
        with open("investment_result.json", "w") as f:
            json.dump({"Stock": stock_name, "Quantity": quantity, "Price": price, "Total": total}, f, indent=4)
        messagebox.showinfo("Saved", "Saved as JSON")
        logging.info("Saved result as JSON")

def add_stock():
    new_symbol = new_stock_entry.get().upper()
    new_price = new_price_entry.get()

    try:
        new_price = float(new_price)
    except:
        messagebox.showerror("Invalid Price", "Enter a valid number.")
        return

    stock_prices[new_symbol] = new_price

    with open("stocks.json", "w") as f:
        json.dump(stock_prices, f, indent=4)

    stock_menu["values"] = list(stock_prices.keys())

    messagebox.showinfo("Added", f"{new_symbol} added successfully!")
    logging.info(f"Added new stock {new_symbol} with price {new_price}")

def show_portfolio():
    if not portfolio:
        messagebox.showinfo("Empty", "No investments yet.")
        return
    
    window = tk.Toplevel(root)
    window.title("Portfolio Summary")

    tree = ttk.Treeview(window, columns=("price", "qty", "total"), show="headings")
    tree.heading("price", text="Price")
    tree.heading("qty", text="Quantity")
    tree.heading("total", text="Total Value")

    for stock, data in portfolio.items():
        tree.insert("", tk.END, values=(data["price"], data["quantity"], data["total"]))

    tree.pack(padx=10, pady=10)

def show_graph():
    if not portfolio:
        messagebox.showinfo("Empty", "No data to display.")
        return

    labels = list(portfolio.keys())
    values = [portfolio[s]["total"] for s in portfolio]

    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Portfolio Distribution")
    plt.show()

# -------------------------------------------------
# UI Setup
# -------------------------------------------------
root = tk.Tk()
root.title("📊 Advanced Stock Portfolio Tracker")
root.geometry("500x520")
root.config(bg="#f2f6ff")

title_label = tk.Label(root, text="Stock Portfolio Tracker", font=("Arial", 18, "bold"), bg="#f2f6ff")
title_label.pack(pady=15)

# Stock selection
stock_var = tk.StringVar(value=list(stock_prices.keys())[0])
tk.Label(root, text="Select Stock:", bg="#f2f6ff", font=("Arial", 12)).pack()
stock_menu = ttk.Combobox(root, textvariable=stock_var, values=list(stock_prices.keys()))
stock_menu.pack(pady=5)

# Quantity
tk.Label(root, text="Enter Shares:", bg="#f2f6ff", font=("Arial", 12)).pack()
quantity_entry = tk.Entry(root, font=("Arial", 12))
quantity_entry.pack(pady=5)

# Calculate Button
tk.Button(root, text="Calculate", font=("Arial", 12), bg="#4CAF50", fg="white",
          command=calculate_investment).pack(pady=10)

result_label = tk.Label(root, text="", bg="#f2f6ff", font=("Arial", 12))
result_label.pack(pady=10)

# Save buttons
tk.Button(root, text="Save TXT", command=lambda: save_result("txt")).pack(pady=2)
tk.Button(root, text="Save CSV", command=lambda: save_result("csv")).pack(pady=2)
tk.Button(root, text="Save JSON", command=lambda: save_result("json")).pack(pady=2)

# Add new stock
tk.Label(root, text="Add New Stock", font=("Arial", 14, "bold"), bg="#f2f6ff").pack(pady=10)
new_stock_entry = tk.Entry(root)
new_price_entry = tk.Entry(root)

tk.Label(root, text="Stock Symbol:").pack()
new_stock_entry.pack()

tk.Label(root, text="Stock Price:").pack()
new_price_entry.pack()

tk.Button(root, text="Add Stock", command=add_stock, bg="#2196F3", fg="white").pack(pady=5)

# Portfolio buttons
tk.Button(root, text="View Portfolio Table", command=show_portfolio).pack(pady=5)
tk.Button(root, text="Show Graph", command=show_graph).pack(pady=5)

last_result = None
root.mainloop()
logging.info("Application Closed")

