def stock_status(stock):
    total = 0

    if stock < 5:
        return "Low stock"
    elif stock < 10:
        return "Medium stock"
    else:
        return "High stock"

def process_stock(stocks):
    total_stock = 0
    for entry in stocks:
        total_stock += entry["Stock"]
        entry["Status"] = stock_status(entry["Stock"])

    return total_stock, stocks

stocks = [

    {"Fruits": "Apple", "Stock": 3},
    {"Fruits": "Banana", "Stock": 7},
    {"Fruits": "Orange", "Stock": 12},
    {"Fruits": "Grapes", "Stock": 2},
    {"Fruits": "Mango", "Stock": 15}
]


print(process_stock(stocks))