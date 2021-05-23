def my_var():
    var_int = 42
    var_int_str = "42"
    var_str = 'quarante-deux'
    var_float = 42.0
    var_bool = True
    var_list = [42]
    var_dict = {42: 42}
    var_tuple = (42,)
    var_set = set()
    print('{} has a type {}'.format(var_int, type(var_int)))
    print('{} has a type {}'.format(var_int_str, type(var_int_str)))
    print('{} has a type {}'.format(var_str, type(var_str)))
    print('{} has a type {}'.format(var_float, type(var_float)))
    print('{} has a type {}'.format(var_bool, type(var_bool)))
    print('{} has a type {}'.format(var_list, type(var_list)))
    print('{} has a type {}'.format(var_dict, type(var_dict)))
    print('{} has a type {}'.format(var_tuple, type(var_tuple)))
    print('{} has a type {}'.format(var_set, type(var_set)))


if __name__ == '__main__':
    my_var()