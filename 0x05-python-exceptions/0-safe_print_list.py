#!/usr/bin/python3
safe_print_list(my_list=[], x=0):
    amount = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            amount += 1
        except:
            print('')
            return amount
    print('')
    return amount
