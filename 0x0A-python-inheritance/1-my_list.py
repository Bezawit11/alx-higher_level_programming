#!/usr/bin/python3
'''class MyList that inherits from list'''


class MyList(list):
    '''
    class MyList that inherits from list
    '''
    def __init__(self):
        list.__init__(self)
    def print_sorted(self):
        my_list.sort()
        print(my_list)
