fix_price, changeble_price, sell_price = map(int, input().split())
profit = sell_price-changeble_price
if sell_price <= changeble_price:
    print(-1)
else:
    print(fix_price//profit+1)