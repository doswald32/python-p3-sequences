#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        new_list = [0, 1]
        i = 0
        while i <=7:
            new_item = new_list[i] + new_list[i + 1]
            new_list.append(new_item)
            i += 1
        print (new_list)