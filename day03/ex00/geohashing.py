#!/usr/bin/python3

import sys
import antigravity


def put_usage():
    print('Usage: geohashing.py latitude longitude date-dow\n',
        '      date format: yyyy-mm-dd\n',
        '      dow: that date\'s (or most recent) DOW opening\n',
        '      example: geohashing.py 37.421542 -122.085589 2005-05-26-10458.68\n')
    sys.exit(1)


def ft_isdate(date):
    l = date.split('-')
    check = 0
    if len(l) == 3:
        if len(l[0]) == 4 and l[0].isdigit():
            check += 1
        if len(l[1]) == 2 and l[1].isdigit():
            check += 1
        if len(l[1]) == 2 and l[1].isdigit():
            check += 1
        if check == 3:
            return True            
    return False


def get_geohash():
    argv = sys.argv
    len_argv = len(argv)
    if len_argv == 4:
        try:
            latitude = float(argv[1])
            longitude = float(argv[2])
            if len(argv[3]) > 11:
                dash = argv[3][10]
                if dash != '-':
                    put_usage()
                date = argv[3][:10]
                if ft_isdate(date) == False:
                    put_usage()
                dow = float(argv[3][11:])
                datedow = '{}{}{}'.format(date, dash, str(dow)).encode()
                antigravity.geohash(latitude, longitude, datedow)
            else:
                put_usage()
        except ValueError as e:
            print("Error parsing arguments. Error description: {}".format(e))
            put_usage()  
        except Exception as e:
            print("Unknown error. Error description: {}".format(e))
            put_usage()  
    else:
        put_usage()


if __name__ == '__main__':
    get_geohash()
