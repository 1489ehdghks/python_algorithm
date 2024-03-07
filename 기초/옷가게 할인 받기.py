price = 580000


def solution(price):
    if 300000 > price >= 100000:
        price = price - price*0.05
    elif 500000 > price >= 300000:
        price = price - price*0.1
    elif price >= 500000:
        price = price - price*0.2
    pass
    return int(price)


a = solution(price)
print(a)


# 다른 사람 풀이

def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
