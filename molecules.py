#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Molecules Assessment
"""
_author_ = "bomazani, Stew, with mob-coding assistance"

import itertools


def string_length(list_of_strings):
    # calculates the length of an individual string in the list_of_strings 
    # see comment in the rectangle_tuples function
    str_len = len(list_of_strings[0])
    return str_len

def rectangle_tuples(x):
    """ return list of unique (w,h) tuple combinations """
    # ??? instead of hard coding the range, should we use range(2, len(string)-2) ???
    # def rectangle_tuples(str_len):
    # pairs = [(w, h) for w in range(2, str_len - 1) for h in range(w, ((str_len - 1) - w))]
    pairs = [(w, h) for w in range(2,11) for h  in range(w, 11-w)]
    # sort from largest rectangle area to smallest rectangle area
    pairs.sort(key=lambda x : x[0] * x[1], reverse=True)
    print pairs


def check_strings(list_of_strings):
    # print list_of_strings[:2]
    pass

# need to iterate through the strings.
# (for loop) assigns the first string as across1
# then iterates through the strings for down1
# if a match 
def first_match(w, h, list_of_strings):
    """ iterates through list of strings to find 4 unique strings. """
    for l in list_of_strings:
        across1 = list_of_strings[l]
        for l in list_of_strings:
            down1 = list_of_strings[l]
            if down1 != across1:
                for l in list_of_strings:
                    across2 = list_of_strings[l]
                    if across2 != across1 and across2 != down1:
                        for l in list_of_strings:
                            down2 = list_of_strings[l]
                            if down2 != across1 and down2 != down1 and down2 != across2:
                                print(across1, down1, across2, down2)
                                # if 4 unique strings are found, call best_fit function
                                if best_fit(w, h, across1, down1, across2, down2):
                                    return w * h


def best_fit(w, h, across1, down1, across2, down2):
    """ Tries to fit a rectangle into a set of 4 molecule strings returns true if a fit is found"""
    for a1 in range(1, 12 - (w + 1)):
        for d1 in range(1, 12 - (h + 1)):
            if across1[a1] != down1[d1]:
                continue
            # If it comes past this continue, might have a rectangle that works.
            for a2 in range(1, 12 - (w + 1)):
                if across2[a2] != down1[d1 + (h +1)]:
                    continue
                for d2 in range(1, 12 - (h + 1)): 
                    if down2[d2] != across2[a2 + (w +1)]:
                        continue
                        if down2[d2] == across1[a1]:
                            return True
    return False




def main():
    strings_list = ['O I M D I H E I A F N L', 'C H J D B J M H P J K D',
                    'L C B J O J G I E K B O', 'K A I N L H L O L B E J']

    check_strings(strings_list)
    rectangle_tuples(12)


if __name__ == '__main__':
    main()