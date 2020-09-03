d1 = {'a': 1, 'b': 2}
d2 = {'a': 2, 'c': 3}

assert d1 | d2 == {'a': 2, 'b': 2, 'c': 3}

# Union is not commutative
assert d1 | d2 != d2 | d1

# *Not always* of course
d3 = {'c': 3}
assert d1 | d3 == d3 | d1

d1 |= d3
assert d1 == {'a': 1, 'b': 2, 'c': 3}
