import sys


def get_dict_key(d, search_value):
    for key, value in d.items():
        if value == search_value:
            return key
    return None


def put_state():
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
    if len(argv) == 2:
        state_key = get_dict_key(capital_cities, argv[1])
        if state_key:
            state = get_dict_key(states, state_key)
            if state:
                print(state)
            else:
                print('Unknown capital city')
        else:
            print('Unknown capital city')


if __name__ == '__main__':
	put_state()