#!/usr/bin/python3
import sys
import os
import re
from settings import *


class ReadFile():
    def __init__(self, filename):
        self.filename = filename
        self.text = None

    def read_file(self):
        try:
            with open(self.filename, 'r') as f:
                self.text = f.read()
        except FileNotFoundError as e:
            print('"{}" not found. Error: {}'.format(self.filename, e))
            sys.exit(1)
        except PermissionError() as e:
            print('You do not have sufficient permission to read "{}". Error: {}'.format(self.filename, e))
            sys.exit(1)
        except IsADirectoryError() as e:
            print('"{}" is a directory, but must be a file. Error: {}'.format(self.filename, e))
            sys.exit(1)
        except Exception as e:
            print('Unknown error while reading the "{}": {}'.format(self.filename, e))
            sys.exit(1)
            

def write_html(filename, template, params):
    html = template.text
    for key in params:
        html = re.sub("{" + key + "}", params[key], html)
    try:
    	with open(filename, "w") as f:
            f.write(html)
    except FileNotFoundError as e:
        print('"{}" not found. Error: {}'.format(filename, e))
        sys.exit(1)
    except PermissionError() as e:
        print('You do not have sufficient permission to write "{}". Error: {}'.format(filename, e))
        sys.exit(1)
    except Exception as e:
        print('Unknown error while writing the "{}": {}'.format(filename, e))
        sys.exit(1)
    

def get_file(extention):
    argv = sys.argv
    len_argv = len(argv)
    if len_argv == 2:
        template = argv[1].strip()
        filename, file_extention = os.path.splitext(template)
        if file_extention == extention:
            return template, filename + ".html"
        else:
            print('Error: wrong file extension')
            sys.exit(1)
    else:
        print('Usage: render.py <*.template>')
        sys.exit(1)


if __name__ == '__main__':
    params = {key : str(value) for key, value in globals().items() if key in
        ('title', 'position', 'name', 'surname', 'age', 'address',
        'profession')}
    template, html = get_file('.template')
    if template:
        template = ReadFile(template)
        template.read_file()
        write_html(html, template, params)
