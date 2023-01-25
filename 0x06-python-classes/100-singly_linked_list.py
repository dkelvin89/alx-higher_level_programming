#!/usr/bin/python3
# 100-singly_linked_list.py
"""Define classes for a singly-linked list."""

class Node:
    """Represent a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next Node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the Node.
        Args:
            value (int): The new data of the Node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next Node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next Node in the list.
        Args:
            value (Node): The new next Node in the list.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.head = None

    def __str__(self):
        """Return a string representation of the entire list."""
        current = self.head
        result = ""
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """Insert a new Node with the given value in the correct sorted position in the list."""
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
