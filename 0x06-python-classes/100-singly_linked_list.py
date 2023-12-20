#!/usr/bin/python3
"""a linked list class."""


class Node:
    """a node class"""
    def __init__(self, data, next_node=None):
        """initialaizing the class"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """data getter"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """data setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """a singly linked list class"""
    def __init__(self):
        """initialaizing the class"""
        self.__head = None

    def __str__(self):
        """for print()"""
        items = []
        tmp = self.__head
        while tmp is not None:
            items.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(items)

    def sorted_insert(self, value):
        """adds a node to the linked list"""
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
