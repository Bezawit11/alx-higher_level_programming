#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
        def next_node(self, value):
            if not isinstance(value, None):
                raise TypeError("data must be an integer")
            self.__next_node = value
class SinglyLinkedList:
        def __init__(self):
            self.__head = None
        def sorted_insert(self, value):
            if self.__head is None:
                new.next_node = None
                self.__head = new
            elif self.__head.data >= value:
                new.next_node = self.__head
                self.__head = new
                return self.__head
            else:
                tra = self.__head
                while (tra.next_node is not None and tra.next_node.data < value):
                    tra = tra.next_node
                new.next_node = tra.next_node
                tra.next_node = new
        def __str__(self):
            list = []
            tra = self.__head
            while tra is not None:
                list.append(str(tra.data))
                tra = tra.next_node
            return ('\n'.join(list))            
