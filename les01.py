import os
import exifread

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
    with open(os.path.join(os.path.curdir, filename), 'r', encoding='utf-8') as file:
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

def image_data(dirname):
    # TODO *Определить, какой из jpg-файлов был создан раньше всех.
    # TODO дописать сравнение дат
    img_folder = os.path.join(os.path.curdir, dirname)
    images = os.listdir(img_folder)
    img_dates = dict()
    for image in images:
        with open(os.path.join(img_folder, image), 'rb') as img_file:
            tags = exifread.process_file(img_file)
            try:
                img_dates.append(str(tags['Image DateTime']).split(' ')[0])
            except KeyError:
                print('Error: Image %s haven\'t date info' % (image))
    return min(img_dates)


if __name__ == '__main__':
    print(write_file(filename='foobar', string='Hello World!'))
    print(write_file_utf(filename='utf-8', string='Hello World! (utf-8)'))
    print(write_binary_file(filename='binary', string='Hello World! (binary)'))
    print(write_latin_file(filename='latin', string='Hello World! (latin-1)'))
    print('Минимальная дата: %s' % (image_data('images')))
