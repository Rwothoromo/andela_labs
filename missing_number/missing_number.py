"""
You are presented with two arrays, all containing positive integers.
One of the arrays will have one extra number, see below:

[1,2,3] and [1,2,3,4] should return 4

[4,66,7] and [66,77,7,4] should return 77
"""

def find_missing(a_list, b_list):
    if (not a_list and not b_list) or a_list == b_list:
        return 0

    # convert the lists to sets for comparison
    set_a = set(a_list)
    set_b = set(b_list)

    set_difference = set_a^set_b
    # compare the sets for a difference
    # similar to set_b.difference(set_a)
    # but better because you'd otherwise repeat with
    # set_a.difference(set_b) if the previous returned an empty set

    difference = list(set_difference)[0]
    return difference
