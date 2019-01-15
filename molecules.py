#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations
"""
Molecules Assessment
"""
_author_ = "bomazani, davidstewy, with mob-coding assistance"

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


def rectangle_tuples(X):
    """ return list of unique (w,h) tuple combinations """
    # ??? instead of hard coding the range, should we use range(2, len(string)-2) ???
    # def rectangle_tuples(str_len):
    # pairs = [(w, h) for w in range(2, str_len - 1) for h in range(w, ((str_len - 1) - w))]
    pairs = [(w, h) for w in range(2,11) for h in range(w, 11)]
    # sort from largest rectangle area to smallest rectangle area
    pairs.sort(key=lambda x : x[0] * x[1], reverse=True)
    print pairs

def rectangle_tuples(list_of_strings):
    str_length = len(list_of_strings[0])
    pairs = [(w, h) for w in range(2, (str_length - 1)) for h in range(w, (str_length - 1))]
    pairs.sort(key=lambda str_length : str_length[0] * str_length[1], reverse=True)
    # print pairs
    return pairs

""" need to iterate through the list of rectangle tuples"""
""" and plug each one into our function """

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
    print('done')

                                


def best_fit(w, h, across1, down1, across2, down2):
    """ Tries to fit a rectangle into a set of 4 molecule strings returns true if a fit is found"""
    for a1 in range(1, 12 - (w + 1)):
        for d1 in range(1, 12 - (h + 1)):
            if across1[a1] != down1[d1]:
                continue
            for a2 in range(1, 12 - (w + 1)):
                if across2[a2] != down1[d1 + (h +1)]:
                    continue
                for d2 in range(1, 12 - (h + 1)):
                    if down2[d2] != across1[a1 + (w + 1)]:
                        continue
                    if down2[d2 + (h + 1)] == across2[a2 + (w + 1)]:
                        return True
    return False




def main():

    # check_strings(strings_list)
    # rectangle_tuples(12)
    pairs = rectangle_tuples(strings_list3)
    # for w, h in pairs:
    print(pairs)
    find_4_unique_strings(8, 8, strings_list)
    # find_4_unique_strings(strings_list3)

    # print('Next set of data')
    # find_4_unique_strings(8, 8, string_samples)


if __name__ == '__main__':
    main()



# iterate through list of rectangle_tuples
#     w,h = rectangle_tuples[0]
#     call function(x,y,list):

strings_list = ['O I M D I H E I A F N L', 'C H J D B J M H P J K D',
                'L C B J O J G I E K B O', 'K A I N L H L O L B E J']

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

