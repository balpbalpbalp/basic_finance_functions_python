def capital_increase_calculator():

    owned_shares = float(input("Enter the amount of shares you own: "))
    split_ratio = float(input("Enter the split ratio: "))
    stock_rights_price = float(input("Enter the price of the stock rights: "))
    stock_price = float(input("Enter the stock price at split: "))

    new_shares = owned_shares * (split_ratio / 100)
    total_shares = owned_shares + new_shares

    capital_paid = new_shares * stock_rights_price
    new_stock_price = stock_price / (1 + (split_ratio / 100))

    print(f"Shared Gained: {new_shares} / Total Shares: {total_shares} / Cash Capital Paid: {capital_paid} / New Price: {new_stock_price}")

capital_increase_calculator()