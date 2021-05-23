#!/usr/bin/python3

class HotBeverage():

    def __init__(self, price=0.30, name='hot beverage', 
            desc = 'Just some hot water in a cup.'):
        self.price = price
        self.name = name
        self.desc = desc

    def description(self):
        return self.desc

    def __str__(self):
        return 'name: {}\nprice: {}\ndescription: {}\n'.format(
            self.name, "%0.2f" % self.price, self.description())


class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(0.40, 'coffee', 'A coffee, to stay awake.')


class Tea(HotBeverage):
    def __init__(self):
        super().__init__(0.30, 'tea', 'Just some hot water in a cup.')


class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__(0.50, 'chocolate', 'Chocolate, sweet chocolate...')


class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__(0.45, 'cappuccino', 'Un po’ di Italia nella sua tazza!')


if __name__ == "__main__":
    hotbeverage = HotBeverage()
    print(hotbeverage)
    coffee = Coffee()
    print(coffee)
    tea = Tea()
    print(tea)
    chocolate = Chocolate()
    print(chocolate)
    cappuccino = Cappuccino()
    print(cappuccino)
