import re


def find_substring(input, string):
    res = re.findall(string + "\\b", input)
    return len(res), res


def pad_numbers(numbers):
    max_pad = len(str(max(numbers))) + 1
    result = []
    for e in numbers:
        result.append(str(e).zfill(max_pad))
    return result


def find_cites(text: str):
    """

    :param text:
    :return:
    """
    r = re.findall(r'".*?"', text)
    return r


def piramide(niveles: int):
    assert niveles > 0

    for i in range(1, niveles + 1):
        print("·" * (niveles - i), end="")
        print("*" * (i * 2 - 1), end="")
        print("·" * (niveles - i))


if __name__ == "__main__":
    print(find_substring("esta es mi casa que esta en madrid y tiene estanterias atestadas", "esta"))
    print(pad_numbers([50, 278, 23, 4, 3125]))
    print(find_cites(r'Debemos encontrar "Texto citado" en esta frase "varias" veces'))
    print(find_cites(r'capitan: "me dijo el grumete "no fui yo", jajaja."'))
    piramide(3)
