import sys

def get_value(element_info, number):
    return element_info[number].split(':')[1].strip()


def get_element(line):
    line_split = line.split('=')
    d = dict()
    d['name'] = line_split[0].strip()
    element_info = line_split[1].split(',')
    i = 0
    for attr in ('position', 'number', 'small', 'molar', 'electron'):
        d[attr] = get_value(element_info, i)
        i += 1
    return(d)


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            l = list()
            for line in f:
                l.append(get_element(line))
        return(l)
    except FileNotFoundError as e:
        print('"{}" not found. Error: {}'.format(filename, e))
        sys.exit(1)
    except PermissionError as e:
        print('You do not have sufficient permission to read "{}". Error: {}'.format(filename, e))
        sys.exit(1)
    except IsADirectoryError as e:
        print('"{}" is a directory, but must be a file. Error: {}'.format(filename, e))
        sys.exit(1)
    except Exception as e:
        print('Unknown error while reading the "{}": {}'.format(filename, e))
        sys.exit(1)


def get_table(elements):
    position = 0
    position_prev = 0
    text = '<table>'
    for el in elements:
        if el['position'].isdigit():
            position = int(el['position'])
        else:
            print('Error!: position element must be a number')
            exit(1)
        if position == 0:		
            text += '<tr>'
        if position - position_prev > 1:		
            text += '<td class="empty" colspan="' + str(position - position_prev - 1) + '"></td>'
        text += '<td><h4>' + el['name']+ '</h4>'
        text += '<ul><li>No ' + el['number'] + '</li>'
        text += '<li>' + el['small'] + '</li>'
        text += '<li>' + el['molar'] + '</li>'
        text += '<li>' + el['electron'] + ' electron</li></ul>'
        text += '</td>'
        if position == 17:
            position = 0
            text += '</tr>\n'
        position_prev = position
    text += '</table>\n'
    return text


def make_html(filename, elements):
    text = '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
    text += '<meta charset="utf-8"/>\n'
    text += '<title>Periodic table of the elements</title>\n' 
    text += '<style>\n'
    text += 'table {\nwidth: 80%;\n}'
    text += 'td {border: 1px solid black; padding:10px; vertical-align:top;}\n'
    text += '.empty {border-width: 0px}\n'	
    text += '</style></head>\n<body>\n'
    text += get_table(elements)
    text += '</body>\n</html>\n'
    try:
        with open(filename, 'w') as f:
            f.write(text)
    except FileNotFoundError as e:
        print('"{}" not found. Error: {}'.format(filename, e))
        sys.exit(1)
    except PermissionError as e:
        print('You do not have sufficient permission to write "{}". Error: {}'.format(filename, e))
        sys.exit(1)
    except Exception as e:
        print('Unknown error while writing the "{}": {}'.format(filename, e))
        sys.exit(1)


if __name__ == '__main__':
    elements = read_file('periodic_table.txt')
    if elements:
        make_html('periodic_table.html', elements)