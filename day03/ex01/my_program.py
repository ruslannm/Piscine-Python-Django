#!/usr/bin/python3

from path import Path

if __name__ == '__main__':
    my_path = Path('.') / 'my_dir'
    if my_path.isfile():
        print('Error: {} is file'.format(my_path))
        exit(1)
    try:
        if not my_path.isdir():
            my_path.mkdir()
        my_file = my_path / 'my_file.txt'
        if my_file.isdir():
            print('Error: {} is dir'.format(my_file))
            exit(1)
        if not my_file.isfile():
            my_file.touch()
        my_file.write_text('INSTRUCTION:\n')
        my_file.write_lines(('1. Create folder',
            '2. Create file inside this folder',
            '3. Write something in this file',
            '4. Read and display its content'),
            append=True)
        print(my_file.read_text())
    except Exception as e:
        print("Unknown error. Error description: {}".format(e))        
