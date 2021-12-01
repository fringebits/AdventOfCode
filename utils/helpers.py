# module of helper functions

def bisect(array, value):
    n = len(array)

    if (value < array[0]):
        return -1
    elif (value > array[n-1]):
        return n

    kLO = 0
    kUP = n - 1

    while (kUP - kLO > 1):
        kMID = (kUP + kLO) >> 1
        if (value == array[kMID]):
            return kMID  # we're done!
        elif (value > array[kMID]):
            kLO = kMID
        else:
            kUP = kMID

    if (value == array[0]):
        return 0
    elif (value == array[n-1]):
        return n-1
    else:
        return kLO

def xor(a, b):
    return (a and not b) or (not a and b)