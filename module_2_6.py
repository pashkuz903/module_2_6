n = int(input('Введите рандомное число от 3 до 20:'))
result = []
for i in range(1,n):
    for j in range(1,n):
        key = [i, j]
        if i == j:
            continue
        if i > j:
            continue
        if n % sum(key) == 0:
            result.extend(key)

print(f'Пароль: ', *result)