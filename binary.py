#Convert decimal numbers into binary on 8 bit's
import math as Mh

decimal_number = int(input("Put the number you want to convert: "))

binary_number_initial = []

for i in range(decimal_number):
    if decimal_number != 0:

        modulo = decimal_number % 2
        decimal_number = Mh.floor(decimal_number/2)

        binary_number_initial.append(modulo)
    else:    
        if len(binary_number_initial) < 8:

            binary_number_initial.append(0)

        elif len(binary_number_initial) > 8:

            binary_number_initial.pop()


binary_number_initial.reverse()
final_number = ''.join([str(joined_number) for joined_number in binary_number_initial])


print(f"Your transformed number in binary form on 8 bits is: {final_number}")



