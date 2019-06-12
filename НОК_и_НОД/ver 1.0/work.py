
def NOD_NOK(a: int, b: int):

    def composit_numb(number: int):
        '''Из каких чисел состоит число'''
        numbers = [1]
        half_number = number / 2 + 1
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
        divider = 1
        dividers = []
        for i in a:
            if i in b:
                b.remove(i)
                dividers.append(i)
        for i in dividers:
            divider *=i
        return divider

    def NOK(a: list, b: list):
        '''наименьшее общее кратное'''
        multiple = 1
        for let in a:
            if let in b:
                b.remove(let)
        a += b
        for i in a:
            multiple *= i
        return multiple

    print(composit_numb(a), composit_numb(b))
    NOD_ab = NOD(composit_numb(a), composit_numb(b))
    print('НОД({},{}): '.format(a, b), NOD_ab)

    NOK_ab = NOK(composit_numb(a), composit_numb(b))
    print('НОК({},{}): '.format(a, b), NOK_ab)



NOD_NOK(384, 654)
