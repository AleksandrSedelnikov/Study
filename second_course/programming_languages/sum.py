
def sum_py(X):
    summa = 0
    for i in range(1, X + 1):
        summa += i
    return summa

def main():
    try:
        X = int(input('Введите размерность диапазона: '))
        result = sum_py(X)
        print('Сумма в ведённом диапазоне чисел: {}'.format(result))
    except Exception:
        return "Ошибка в размерности."

if __name__ == "__main__":
    main()
    