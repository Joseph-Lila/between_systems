import csv
import os

#Class Dictionary allows create dictionaries using files with sorted keys sequences

class Dictionary():
    def __init__(self, p, m, d):
        self.path = p
        self.mode = m
        self.delimiter = d
#border is necessary for limiting dictionary
    def get_dictionary(self, border):
        my_list = list()
        with open(self.path, self.mode) as f:
            r = csv.reader(f, delimiter = self.delimiter)
            for row in r:
                my_list += row
        my_dict = dict()
        for i in range(0, min(len(my_list),border)):
            my_dict[my_list[i]] = i
        return my_dict
