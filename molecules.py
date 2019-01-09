#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Molecules Assessment
"""
_author_ = "bomazani, Stew, with mob-coding assistance"

# import itertools


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
    pairs = [(w, h) for w in range(2,11) for h  in range(w, 11)]
    # sort from largest rectangle area to smallest rectangle area
    pairs.sort(key=lambda x : x[0] * x[1], reverse=True)
    # print pairs


def check_strings(list_of_strings):
    # print list_of_strings[:2]
    pass

# need to iterate through the strings.
# (for loop) assigns the first string as across1
# then iterates through the strings for down1
# if a match 
def find_4_unique_strings(w, h, list_of_strings):
    """ iterates through list of strings to find 4 unique strings. """
    for i in range(0, len(list_of_strings)):
        # across2 = list_of_strings[i]
        down2 = list_of_strings[i]

        for i in range(0, len(list_of_strings)):
            # down2 = list_of_strings[i]
            across2 = list_of_strings[i]

            if across2 != down2:
                for i in range(0, len(list_of_strings)):
                    # across1 = list_of_strings[i]
                    down1 = list_of_strings[i]

                    if down1 != down2 and down1 != across2:
                        for i in range(0, len(list_of_strings)):
                            # down1 = list_of_strings[i]
                            across1 = list_of_strings[i]
                            if across1 != down2 and across1 != across2 and across1 != down1:
                                # print('across1 {}, down1 {}, across2 {}, down2 {}'.format(across1, down1, across2, down2))
                                # if 4 unique strings are found, call best_fit function
                                if best_fit(w, h, across1, down1, across2, down2):
                                    
                                    print('Solved It!')
                                    print(w * h)
                                    return w * h
                                else:
                                    print('continuing')
                                    continue

                                


def best_fit(w, h, across1, down1, across2, down2):
    """ Tries to fit a rectangle into a set of 4 molecule strings returns true if a fit is found"""
    a_stop = (12 - (w + 1))
    # print('a_stop = {}'.format(a_stop))
    d_stop = (12 - (h + 1))
    # print('d_stop = {}'.format(d_stop))

    for a1 in range(1, a_stop):
        for d1 in range(1, d_stop):
            # print('a1 = {} / d1 = {}'.format(a1, d1))
            # print('across1 = {} / down1 = {}'.format(across1[a1], down1[d1]))
            if across1[a1] != down1[d1]:
                continue
            # If it comes past this continue, might have a rectangle that works.
            for a2 in range(1, a_stop):
                # print('a2 = {} / d1 = {}'.format(a2, d1 + (h +1)))
                # print('across2 = {} / down1 = {}'.format(across2[a2], down1[d1 + (h +1)]))
                if across2[a2] != down1[d1 + (h +1)]:
                    continue
                for d2 in range(1, d_stop):
                    # print('d2 = {} / a1 = {}'.format(d2, a1 + (w + 1)))
                    # print('down2 = {} / across1 = {}'.format(down2[d2], across1[a1 + (w +1)]))
                    if down2[d2] != across1[a1 + (w + 1)]:
                        continue
                    # print('d2 = {} / a2 = {}'.format(d2 + (h + 1), a2 + (w + 1)))
                    # print('down2 = {} / across2 = {}'.format(down2[d2 + (h + 1)], across2[a2 + (w + 1)]))
                    if down2[d2 + (h + 1)] == across2[a2 + (w + 1)]:
                        return True
    return False




def main():
    # strings_list = ['O I M D I H E I A F N L', 'C H J D B J M H P J K D',
                    # 'L C B J O J G I E K B O', 'K A I N L H L O L B E J']

    # strings_list2 = ['W A A D I H E I A B B W', 'X B B D B J M H P A A X',
    #                  'Z A A J O J G I E B B Z', 'Y B B N L H L O L A A Y']

    strings_list3 = ['XBFDBJMHPHDX', 'YAENLHLOLCCY', 'ZAEJOJGIEFBZ', 'WCCDIHEIAHDW']


    
    string_samples_plus = ['CDBADCBBEFEF', 'DACCBADAFEAB',
                           'EFBDCAADBDCD', 'ABCDABCDABCD',
                           'DACCBADAFEAB', 'EFBDCAADBDCD',
                           'ABCDABCDABCD', 'CDBADCBBEFEF',
                           'ABABABABABAB', 'CDCDCDCDCDCD',
                           'EEEEEEEEEEEE', 'FFFFFFFFFFFF',
                           'ABAAAAAAAABA', 'CBCCCCCCCCBC',
                           'DBDDDDDDDDBD', 'EBEEEEEEEEBE',
                           'ABBBBBBBBBBA', 'ACCCCCCCCCCA',
                           'ADDDDDDDDDDA', 'AEEEEEEEEEEA',
                           'BBBABBBABBBB', 'CCACCCACCCCC',
                           'DDDDADDADDDD', 'EEAEEAEEEEEE',
                           'WCCDIHEIAHDW', 'XBFDBJMHPHDX',
                           'ZAEJOJGIEFBZ', 'YAENLHLOLCCY']

    # string_samples = ['CDBADCBBEFEF', 'DACCBADAFEAB',
                    #   'EFBDCAADBDCD', 'ABCDABCDABCD',
                    #   'DACCBADAFEAB', 'EFBDCAADBDCD',
                    #   'ABCDABCDABCD', 'CDBADCBBEFEF',
                    #   'ABABABABABAB', 'CDCDCDCDCDCD',
                    #   'EEEEEEEEEEEE', 'FFFFFFFFFFFF',
                    #   'ABAAAAAAAABA', 'CBCCCCCCCCBC',
                    #   'DBDDDDDDDDBD', 'EBEEEEEEEEBE',
                    #   'ABBBBBBBBBBA', 'ACCCCCCCCCCA',
                    #   'ADDDDDDDDDDA', 'AEEEEEEEEEEA',
                    #   'BBBABBBABBBB', 'CCACCCACCCCC',
                    #   'DDDDADDADDDD', 
                    #   'EEAEEAEEEEEE',
                    #   'Q']

    # check_strings(strings_list)
    rectangle_tuples(12)

    # find_4_unique_strings(8, 8, strings_list)
    find_4_unique_strings(7, 7, strings_list3)

    # print('Next set of data')
    # find_4_unique_strings(8, 8, string_samples)


if __name__ == '__main__':
    main()