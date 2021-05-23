#!/usr/bin/python3


class Intern():
    def __init__(
            self, name = 'My name? I’m nobody, an intern, I have no name.'):
        self.Name = name

    def __str__(self):
        return self.Name


    class Coffee():
        def __str__(self):
            return 'This is the worst coffee you ever tasted.'

    def work(self):
        raise Exception('I’m just an intern, I can’t do that...')

    def make_coffee(self):
        coffee = self.Coffee()
        return coffee


if __name__ == '__main__':
    first_intern = Intern()
    second_intern = Intern('Mark')      
    print(first_intern)
    print(second_intern)
    print(second_intern.make_coffee())
    try:
        first_intern.work()
    except Exception as e:
        print(e)
