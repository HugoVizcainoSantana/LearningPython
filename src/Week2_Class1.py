from math import sqrt


def is_prime(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(sqrt(num) + 1), 2):
        if num % i == 0:
            return False
    else:
        return True


def primes_to_100():
    primes = [1, 2]
    for i in range(2, 100):
        if is_prime(i):
            primes.append(i)
    return primes


def print_elements_in_even_pos(list):
    for i in range(0, len(list), 2):
        print(list[i])


def is_perfect_number(num):
    count = 0
    for i in range(1, num):
        if num % i == 0:
            count += i
    print("Is " + str(num) + " a perfect number?")
    return count == num


def square_and_cube(list):
    result = []
    for e in list:
        result.append((e, e ** 2, e ** 3))
    return result


def max_and_min(list):
    """
    Returns max and min value from a list
    :param list: List[int]
    :return: (int,int) max and min
    """
    min_elem, max_elem = list[0], list[0]
    for e in list:
        if e > max_elem:
            max_elem = e
        if e < min_elem:
            min_elem = e
    return max_elem, min_elem


def invert_string(string):
    return string[::-1]


def capitalize_string(string):
    return string[0].upper() + string[1:].lower()


def print_matrix(matrix):
    output = ""
    for row in matrix:
        for elem in row:
            output += "[" + str(elem) + "] "
        output += "\n"
    return output


# Exercises
print("E1: Primes up to 100")
print(primes_to_100())
print("E2: Print Elements in Even Pos")
print_elements_in_even_pos([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("E3: Perfect Number?")
print(is_perfect_number(28))
print(is_perfect_number(45))
print("E4: Calculate Square and Cube")
print(square_and_cube([1, 2, 3]))
ej5 = [1, 4, 432, 5, 634, 7, 85, 2, 634, 66, 2]
print("E5: Get max and min from list. Values are " + str(ej5))
print(max_and_min(ej5))
print("E6: Invert String")
print(invert_string("Hola Mundo!"))
print("E7: Capitalize String")
print(capitalize_string("buenos dias mundo"))
print("E8: Print Matrix")
print(print_matrix(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
))
