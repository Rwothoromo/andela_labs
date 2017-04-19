def find_max_min(A):
    a_sorted = sorted(A)
    a_min = a_sorted[0]
    a_max = a_sorted[-1]

    if a_min == a_max:
        return [len(A)]
    return [a_min, a_max]