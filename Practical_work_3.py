seq_num = input('Введите последовательность целых чисел через пробел: ')
user_num = int(input('Введите любое число: '))
error = 'Перезапустите программу!'


# Функция для определения цифр в строке.
def is_int(str_seq):
    str_seq = str_seq.replace(' ', '')
    try:
        int(str_seq)
        return True
    except ValueError:
        return False


# Проверка соответствия условиям при вводе данных.
if " " not in seq_num:
    print("\nПри вводе последовательности целых чисел отсутствовал пробел!")
    seq_num = input('Введите последовательность целых чисел через пробел: ')
if not is_int(seq_num):
    print('\nВвод не содержит целых чисел!\n')
    print(error)
else:
    seq_num = seq_num.split()

# Преобразование введённой последовательности в список.
list_seq_num = [int(item) for item in seq_num]


# Сортировка списка по возрастанию элементов в нем.
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


list_seq_num = merge_sort(list_seq_num)


# Устанавливается номер позиции элемента,
# который меньше введённого пользователем числа,
# а следующий за ним больше или равен этому числу.

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Целое число выходит за диапазон списка! Введите меньшее число.'


print(f'Упорядоченный список по возрастанию: {list_seq_num}')

if not binary_search(list_seq_num, user_num, 0, len(list_seq_num)):
    rI = min(list_seq_num, key=lambda x: (abs(x - user_num), x))
    ind = list_seq_num.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_num:
        print(f'''В списке нет введённого элемента! 
Ближайший меньший элемент: {rI} с индексом - {ind}
Ближайший больший элемент: {list_seq_num[max_ind]} с индексом - {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введённого элемента!
Ближайший больший элемент: {rI} с индексом - {list_seq_num.index(rI)}
В списке нет меньшего элемента''')
    elif rI > user_num:
        print(f'''В списке нет введённого элемента!
Ближайший больший элемент: {rI} с индексом - {list_seq_num.index(rI)}
Ближайший меньший элемент: {list_seq_num[min_ind]} с индексом - {min_ind}''')
    elif list_seq_num.index(rI) == 0:
        print(f'Индекс ввёденного элемента: {list_seq_num.index(rI)}')
else:
    print(f'Индекс введённого элемента: {binary_search(list_seq_num, user_num, 0, len(list_seq_num))}')

