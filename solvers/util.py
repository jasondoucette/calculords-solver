# via http://stackoverflow.com/a/7947461/19794
def interleave(a, b):
    c = a + b
    c[::2] = a
    c[1::2] = b
    return c
