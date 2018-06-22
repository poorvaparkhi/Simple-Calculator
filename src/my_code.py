import re

def add(text):
    res = 0
    if text:
        numbers = split_text(text)
        int_numbers = map(lambda x: int(x), numbers)

        neg_check = check_for_negative(int_numbers)
        if neg_check:
            raise Exception("negatives not allowed", int_numbers)

        removed_thousand = greater_than_thousand(int_numbers)

        res = sum(removed_thousand)
        return res
    else:
        return res


def sum(numbers):
    sum = reduce(lambda x, y: x + y, numbers)
    return sum


def greater_than_thousand(numbers):
    for n in numbers:
        if n > 1000:
            numbers.remove(n)
    return numbers


def check_for_negative(numbers):
    neg_check = [i for i in numbers if i < 0]

    if neg_check:
        return True
    else:
        return False


def split_text(text):
    numbers = re.split("\n|,|\*|%|//[\*][%]", text)
    print numbers
    number_regex = re.compile(r'[-]?[0-9]+')
    num = []
    for n in numbers:
        print n
        if number_regex.match(n):
            num.append(n)

    return num