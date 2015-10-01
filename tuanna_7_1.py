# Simulate a person go to market to build food. There are:
# Buyer (money, bag)
# Seller (money, goods)
# Goods (name, size, price)
# Bag of buyer. (size)
# Seller has two apples(10k/each), three bottle of milks (40k/bottle), 3 Kg of beef (100k/kg).
# Let buyer buys each at least one.
# Use class to represent that.

# not enough food
# not enough monney
# not in the market
# not enough bag space
class Buyer:
    def __init__(self, monney, bag):
        self.monney = monney
        self.bag = bag
        self.limited_goods = {'apple': [2, 10000], 'milks': [3, 40000], 'beef': [3, 100000]}

    def buy(self, **kargs):
        try:
            # not enough food
            count =0
            for food in kargs:
                count += kargs[food]
                if kargs[food] > self.limited_goods[food][0]:
                    return "Not enough {0} in market".format(food)
        except KeyError:
            # food not in the market
            # not enough monney

            return "{0} not in the market".format(food.capitalize())
        if count > self.bag:
            return "Not enough bag space"
        else:
            monney = 0
            for food in kargs:
                monney += self.limited_goods[food][1] * kargs[food]
            if monney > self.monney:
                return "Not enough monney"
            elif monney <= self.monney:
                return "Successful transactions"


c = Buyer(100000, 4)
print c.buy(apple=2, milks = 3)
print c.buy(apple=2, milks = 1)
print c.buy(apple=1, milks = 3)
print c.buy(nho=2, beef=5)
# Not enough bag space
# Successful transactions
# Not enough monney
# Nho not in the market

