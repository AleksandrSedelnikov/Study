def animals_k(list):
    f = open('animals.txt', 'w')
    for i in list:
        if (list.index(i) in [0,3,4] and i[0].lower() == "к"):
            f.write('[ID {}] Животное: {}\n'.format(list.index(i) + 1, i))
        else:
            pass
    f.close()
    return 0



def main():
    animals = []
    print('Сейчас будет начат ввод...')
    for i in range(6):
        animals.append(input('Введите животное номер {}: '.format(i + 1)))
    animals_k(animals)
    print('Скрипт закончил работу...')
    return 0

if __name__ == "__main__":
    main()