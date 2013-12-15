#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A LL in Python doesn't make much sense and is very rare.
You're better off using a list or deque.
"""

class Node(object):
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList(object):
    """Singly linked list."""
    def __init__(self):
        self.head = None

    def __str__(self):
        ll = []
        node = self.head
        while node:
            ll.append('{}'.format(node.data))
            if node.next:
                ll.append(' →  ')
            node = node.next
        return ''.join(ll)

    def push_front(self, d):
        new_node = Node(d)
        new_node.next = self.head
        self.head = new_node

    def push_back(self, d):
        new_node = Node(d)
        node = self.head
        while node:
            if node.next is None:
                node.next = new_node
                new_node.next = None
                #new_node.data = d
            node = node.next

    def find(self, d):
        node = self.head
        while node:
            if node.data == d:
                return True
            node = node.next
        return False

    def remove(self, d):
        """Removes the first instance found."""
        node = self.head
        if node.data == d:
            self.head = node.next  # Move head (same as self.head.next)
            return
        while node.next:
            if node.next.data == d:
                node.next = node.next.next
                return
            node = node.next

ll = LinkedList()
ll.push_front(1)
ll.push_front(2)
ll.push_front(3)
ll.push_back(4)
print(ll)
print ll.find(2)
print ll.find(10)
print ll.find(3)
ll.remove(3)  # Remove first node
print(ll)
ll.remove(1) # Remove middle node
print(ll)
