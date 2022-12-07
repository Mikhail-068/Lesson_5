import os, shutil

menu = '''---------------------------------------------------
=== Выберите нужный пункт ===
---------------------------------------------------
1. создать папку
2. удалить (файл/папку)
3. копировать (файл/папку)
4. просмотр содержимого рабочей директории
5. посмотреть только папки
6. посмотреть только файлы
7. просмотр информации об операционной системе
8. создатель программы
9. играть в викторину
10. мой банковский счет
11. смена рабочей директории 
12. выход
'''
def create_file(name, text):
    with open(f'{name}.txt', 'w', encoding='utf-8') as f:
        f.write(text)

def select():
    '''
    "Консольный файловый менеджер"
    :return:
    '''
    while True:
        user = int(input(menu))

# 1 Создание файла и папки
        if user == 1:
            num = int(input('1. Создать файл\n2. Создать папку\n'))
            if num == 1:
                name_file = input('Введите имя файла:\n')
                text_ = input('Создержимое файла:\n')
                create_file(name_file, text_)
            elif num == 2:
                name_folder = input('Введите имя папки:\n')
                os.mkdir(name_folder)

# Удаление файла и папки
        elif user == 2:
            num = int(input('1. Удалить файл\n2. Удалить папку\n'))
            if num == 1:
                del_file = input('Введите имя файла:\n')
                os.remove(f'{del_file}.txt')
            elif num == 2:
                del_folder = input('Введите имя папки:\n')
                shutil.rmtree(del_folder)

# Копирование файла и папки
        elif user == 3:
            num = int(input('1. Копировать файл\n2. Копировать папку\n'))
            if num == 1:
                path, path2 = input('Откуда?\n'), input('Куда?\n')
                shutil.copy(path, path2)
            elif num == 2:
                path, path2 = input('Откуда?\n'), input('Куда?\n')
                shutil.copytree(path, f'{path2}/{path}')
        else:
            break



if __name__ == '__main__':
    # shutil.copytree('msi', 'Car/msi')
    select()

