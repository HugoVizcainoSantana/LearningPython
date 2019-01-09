def primesTo100():
    primes = {2}
    for i in range(3, 100, 2):
        for n in primes.copy():
            if i % n != 0:
                primes.add(i)
    print("Primes Up to 100:" + str(primes))


def splitIntoDigits(num):
    digits = []
    while num > 0:
        digits.insert(0, num % 10)
        num = num // 10
    return digits


def union(set1, set2):
    s = set()
    for e1 in set1:
        s.add(e1)
    for e2 in set2:
        s.add(e2)
    return s


def intersection(set1, set2):
    s = set()
    for e in set1:
        if e in set2:
            s.add(s)
    return s


def difference(set1, set2):
    s = set()
    for e in set1:
        if e not in set2:
            s.add(s)
    return s


def copySet(s):
    result = set()
    for e in s:
        result.add(e)


def isCubifinite(num, cubifinites=set(), visited=set()):
    digits = splitIntoDigits(num)
    digit_sum = 0
    for d in digits:
        digit_sum += d ** 3

    if digit_sum == 1:
        cubifinites.add(num)
        return True
    else:
        # Check for Loop!
        if num == digit_sum or not isCubifinite(digit_sum, cubifinites, visited):
            visited.add(digit_sum)
            return False
        else:
            cubifinites.add(digit_sum)
            return True


def opposite_pairs(list):
    """"
    # Not optimal
# s = set()
# for e in list:
#    if e not in s:
#        s.add(-e)
#    else:
#        s.remove(e)
# return -s.pop()
"""
    s = 0
    for n in list:
        s += n
    return s


def get_non_repeated_element(list):
    s = 0
    for e in list:
        s ^= e
    return s


def split_even_odd(s):
    e = set()
    o = set()
    for elem in s:
        if elem & 1:
            o.add(elem)
        else:
            e.add(elem)
    return e, o


def cartessian_product(set1, set2):
    result = set()
    for s1 in set1:
        for s2 in set2:
            result.add((s1, s2))
    return result


# Examples
primesTo100()
print("Digits of " + str(1352458) + " are " + str(splitIntoDigits(1352458)))
print("Is Cubifinite 1? ", end="")
print(isCubifinite(1))
print("Is Cubifinite 513? ", end="")
print(isCubifinite(513))
l1 = [3, 5, -7, -9, -3, 7, 9]
print("Oposite Pairs: Args: " + str(l1))
print(opposite_pairs(l1))
l2 = [3, 7, 1, 9, 2, 9, 1, 2, 3]
print("Non Repeated Element: Args: " + str(l2))
print(get_non_repeated_element(l2))
print("Split array into (even,odd)")
print(split_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print("Cartessian Product of Sets:")
print(cartessian_product({1, 2, 3}, {4, 5, 6}))
