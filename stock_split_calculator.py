def stock_split_calculator():

    owned_shares = float(input("Enter the amount of the shares you own: "))
    split_ratio = float(input("Enter the split ratio: "))
    stock_price = float(input("Enter the stock price at the stock split: "))

    new_shares = owned_shares * (split_ratio / 100)
    total_shares_after_split = owned_shares + new_shares
    new_stock_price = stock_price / (1 + (split_ratio / 100))
    
    print(f"Awarded Shares: {new_shares} / Total Shares: {total_shares_after_split} / New Price: {new_stock_price}")

stock_split_calculator()