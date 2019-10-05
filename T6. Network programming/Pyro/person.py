from __future__ import print_function
import sys


class Person(object):
    def __init__(self, name):
        self.name = name

    def visit(self, warehouse, deposit, retrive):
        print("This is {0}.".format(self.name))
        self.deposit(warehouse, deposit)
        self.retrieve(warehouse, retrive)
        print("Thank you, come again!")

    def deposit(self, warehouse, item):
        print("The warehouse contains:", warehouse.list_contents())
        if item:
            warehouse.store(self.name, item)

    def retrieve(self, warehouse, item):
        print("The warehouse contains:", warehouse.list_contents())
        if item:
            warehouse.take(self.name, item)
