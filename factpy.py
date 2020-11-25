def calculate_factorial_multi_half(number):

        if number == 1 or number == 0:
            return 1

        handle_odd = False
        upto_number = number

        if number & 1 == 1:
            upto_number -= 1
            handle_odd = True

        next_sum = upto_number
        next_multi = upto_number
        factorial = 1

        while next_sum >= 2:
            factorial *= next_multi
            next_sum -= 2
            next_multi += next_sum
            print(factorial)

        if handle_odd:
            factorial *= number
##        print(factorial)
        return factorial
calculate_factorial_multi_half(100)
