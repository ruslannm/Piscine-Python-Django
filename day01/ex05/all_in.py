import sys


def get_dict_value(d, search_key):
    search_key = search_key.lower()
    for key, value in d.items():
        if key.lower() == search_key:
            return value
    return None


def get_dict_key(d, search_value):
    search_value = search_value.lower()
    for key, value in d.items():
        if value.lower() == search_value:
            return key
    return None


def put_info():
    states = {
        "OregoN" : "OR", 
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
        search_list = argv[1].strip().split(',')
        for search_str in search_list:
            search_str = search_str.strip().split()
            search_str = ' '.join(search_str)
            if search_str:
                state = get_dict_value(states, search_str)
                if state:
                    state_name = get_dict_key(states, state)
                    capital = get_dict_value(capital_cities, state)
                    if capital:
                        print('{} is the capital of {}'.format(capital, state_name))
                else:
                    state = get_dict_key(capital_cities, search_str)
                    if state:
                        capital = get_dict_value(capital_cities, state)
                        state_name = get_dict_key(states, state)
                        if state_name:
                            print('{} is the capital of {}'.format(capital, state_name))
                    else:
                        print('{} is neither a capital city nor a state'.format(search_str))


if __name__ == '__main__':
	put_info()