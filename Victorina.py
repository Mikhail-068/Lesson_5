import random

# Знаменитости
celebrities = {"Гайдна": '31.03.1732', "Паганини": '27.10.1782',
               "Брамса": '07.05.1833', "Генделя": '23.02.1685',
               "Бетховена": '16.12.1770', "Рахманинова": '01.04.1873',
               'Вивальди': '04.03.1678', "Верди": "10.10.1813",
               "Моцарта": '27.01.1756', "Баха": "31.03.1685"}
people = [i for i in celebrities.keys()]

best_celeb = random.sample(people, 5)

celebrities_error = {"Гайдна": 'тридцать первое марта 1732 года',
                     "Паганини": 'двадцать седьмое октября 1782 года',
                     "Брамса": 'седьмое мая 1833 года',
                     "Генделя": 'двадцать третье февраля 1685 года',
                     "Бетховена": 'шестнадцатое декабря 1770 года',
                     "Рахманинова": 'первое апреля 1873 года',
                     'Вивальди': 'четвертое марта 1678 года',
                     "Верди": "десятое октября 1813 года",
                     "Моцарта": 'двадцать седьмое января 1756 года',
                     "Баха": "тридцать первое марта 1685 года"}

def vic():

    res = 'да'
    while res != 'нет':
        best_celeb = random.sample(people, 5)
        print('-' * 99)
        print('=' * 40, 'В И К Т О Р И Н А', '=' * 40, )
        print('-' * 99)

        list_errors = []

        for surname in best_celeb:
            data_ = input(f'Введите дату рождения в формате "dd.mm.yyyy" {surname}\n')
            answer = celebrities[surname]

            if data_ != answer:
                list_errors.append(1)
                print('Правильный ответ:', celebrities_error[surname])
            else:
                list_errors.append(0)

        error = sum(list_errors)
        correct = len(list_errors) - error

        print()
        print(f'Количество правильных ответов: {correct}')
        print(f'Количество ошибок: {error}')
        print(f'Процент правильных ответов: {correct * 100 / len(list_errors)}%')

        print('-' * 99)
        res = input('Не хотите ли ещё сыграть?\n').lower()

if __name__ == '__main__':
    vic()