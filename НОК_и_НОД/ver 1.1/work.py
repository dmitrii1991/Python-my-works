
def NOD_NOK(a: int, b: int):

    def composit_numb(number: int):
        '''Возращает список простых чиселБ из кторых состоит данное вводимое число'''
        numbers = [1]
        i = 2
        while i <= number:
            if number % i == 0:
                number = number / i
                numbers.append(i)
            else:
                i += 1
        return numbers

    def NOD(a: list, b: list):
        '''Наибольщий общий делитель'''
        list_a = a.copy()
        list_b = b.copy()
        divider = 1
        dividers = []
        for i in list_a:
            if i in list_b :
                list_b.remove(i)
                dividers.append(i)
        for i in dividers:
            divider *=i
        return divider

    def NOK(a: list, b: list):
        '''Наименьшее общее кратное'''
        list_a = a.copy()
        list_b = b.copy()

        multiple = 1
        for let in list_a :
            if let in list_b:
                list_b.remove(let)
        list_a += list_b
        for i in list_a:
            multiple *= i
        return multiple

    num_a = composit_numb(a)
    num_b = composit_numb(b)

    NOD_ab = NOD(num_a, num_b)
    print('НОД({},{}): '.format(a, b), NOD_ab)

    NOK_ab = NOK(num_a, num_b)
    print('НОК({},{}): '.format(a, b), NOK_ab)



NOD_NOK(384, 654)
