import os
import pickle

def write_file(string, filename):
    '''
    Write file without encoding than read file
    :param string: str
    :param filename: str
    :return: str
    '''
    with open(os.path.join(os.path.curdir, filename), 'w+') as file:
        file.write(string)
    with open(os.path.join(os.path.curdir, filename), 'r') as file:
        result = file.readline()
    return result


def write_file_utf(string, filename):
    '''
    Write file with utf-8 encoding than read file
    :param string: str
    :param filename: str
    :return: str
    '''
    with open(os.path.join(os.path.curdir, filename), 'w+', encoding='utf-8') as file:
        file.write(string)
    with open(os.path.join(os.path.curdir, filename), 'r') as file:
        result = file.readline()
    return result


def write_binary_file(string, filename):
    '''
    Write binary file with utf-8 encoding than read file
    :param string: str
    :param filename: str
    :return: str
    '''
    with open(os.path.join(os.path.curdir, filename), 'wb') as file:
        file.write(bytes(string.encode('utf-8')))
    with open(os.path.join(os.path.curdir, filename), 'rb') as file:
        result = file.readline()
    return result.decode('utf-8')

def write_latin_file(string, filename):
    '''
    Write file with latin-1 encoding than read file
    :param string: str
    :param filename: str
    :return: str
    '''
    with open(os.path.join(os.path.curdir, filename), 'w+', encoding='latin-1') as file:
        file.write(string)
    with open(os.path.join(os.path.curdir, filename), 'r') as file:
        result = file.readline()
    return result

def image_date(filename):
    # TODO *Определить, какой из jpg-файлов был создан раньше всех.
    pass


if __name__ == '__main__':
    print(write_file(filename='foobar', string='Hello World!'))
    print(write_file_utf(filename='utf-8', string='Hello World! (utf-8)'))
    print(write_binary_file(filename='binary', string='Hello World! (binary)'))
    print(write_latin_file(filename='latin', string='Hello World! (latin-1)'))
