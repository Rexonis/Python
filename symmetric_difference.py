def symmetric_difference(A, B):
    set_A = set(A)
    set_B = set(B)
    set_C = set_A ^ set_B
    return sorted(set_C)

input_string = input()  # считываем строку с входными данными

tokens = input_string.split()  # разделяем строку на числа

index = tokens.index('0')  # находим индекс разделителя

set_A = list(map(int, tokens[:index]))  # создаем список чисел для множества А

set_B = list(map(int, tokens[index+1:]))  # создаем список чисел для множества В

result = symmetric_difference(set_A, set_B)  # вычисляем симметрическую разность

result = sorted(filter(lambda x: x != 0, result))  # фильтруем нули

if len(result) == 0:
    print(0)
else:
    print(' '.join(map(str, result)))  # выводим результат разделенный пробелами