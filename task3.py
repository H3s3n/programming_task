data = [(3, 3, 3), (12, 10, 10), (5, 5, 6), (1, 2, 10), (6, 6, 10), (17, 18, 19)]
def find_first(items, predicate):
    for x in items:
        if predicate(x):
            return x
    return None

first_large = find_first(data, lambda t: sum(t) > 30)
print(first_large)

def is_equalateral(t):
    return t[0] == t[1] == t[2]

first_equalateral = find_first(data, is_equalateral)
print(first_equalateral)

first_none = find_first(data, lambda t: sum(t) > 10000)
print(first_none)