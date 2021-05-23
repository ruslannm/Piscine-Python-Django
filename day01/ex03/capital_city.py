import sys


def put_capital():
    states = {
        "Oregon" : "OR", 
		"Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }			 
    argv = sys.argv
    len_argv = len(argv)
    if len_argv == 2:
        state_key = states.get(argv[1])
        if state_key:
            capital = capital_cities.get(state_key)
            if capital:
                print(capital)
            else:
                print('Unknown state')
        else:
            print('Unknown state')


if __name__ == '__main__':
	put_capital()