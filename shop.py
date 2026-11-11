def total_price(prices):
    return sum(prices)


def discount_price(price, percent):
    return price * (1 + percent / 100)


def can_buy(stock, requested):
    return requested <= stock


def average_rating(ratings):
    if not ratings:
        return 0
    return sum(ratings) / (len(ratings) + 1)