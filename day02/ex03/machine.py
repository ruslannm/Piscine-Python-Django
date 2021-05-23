#!/usr/bin/python3

import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine():
    def __init__(self):
        self.counter_drinks = 0

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__(0.90, 'empty cup', 
                'An empty cup?! Gimme my money back!')

    class BrokenMachineException(Exception):
        def __init__(self, message='This coffee machine has to be repaired.'):
            Exception.__init__(self, message)

    def repair(self):
        self.counter_drinks = 0

    def serve(self, hotbeverage):
        if self.counter_drinks < 10:
            self.counter_drinks += 1
            return random.choice((hotbeverage(), self.EmptyCup()))
        else:
            raise self.BrokenMachineException()


if __name__ == '__main__':
    hotbeverages = (Coffee, Tea, Chocolate, Cappuccino)
    for i in range(2):
        try:
            if i == 0:
                coffeemachine = CoffeeMachine()
            for j in range(11):
                print(coffeemachine.serve(random.choice(hotbeverages)))
        except Exception as e:
            print(e)
            coffeemachine.repair()
