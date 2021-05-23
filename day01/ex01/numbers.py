def put_number(filename):
    try:
        with open(filename, 'r') as f:
            numbers = f.readline().strip().split(',')
            for n in numbers:
                print(n.strip())
    except FileNotFoundError as e:
        print('"{}" not found. Error: {}'.format(filename, e))
    except PermissionError as e:
        print('You do not have sufficient permission to read "{}". Error: {}'.format(filename, e))
    except IsADirectoryError as e:
        print('"{}" is a directory, but must be a file. Error: {}'.format(filename, e))
    except Exception as e:
        print('Unknown error while reading the "{}": {}'.format(filename, e))


if __name__ == '__main__':
    put_number('numbers.txt')