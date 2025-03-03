def get_price(is_vip=False):
    if is_vip == True:
        return 10000
    else:
        return 15000

price = get_price(True)
print(price)