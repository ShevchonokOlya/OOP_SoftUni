class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.current = 0 - step
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.current += self.step
            self.count -= 1
            return self.current
        raise StopIteration


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
#
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)


class DictionaryIter:
    def __init__(self, dictionary: dict):
        self.dictionary_list = list(dictionary.items())
        self.end = len(self.dictionary_list)
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.end:
            item = self.dictionary_list[self.current]
            self.current += 1
            return item
        raise StopIteration


#
# result = DictionaryIter({1: "1", 2: "2"})
# for x in result:
#     print(x)
#
# result = DictionaryIter({"name": "Peter", "age": 24})
# for x in result:
#     print(x)


class CountdownIterator:
    def __init__(self, count: int):
        self.count = count
        self.end = 0
        self.current = self.count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1

        if self.current >= self.end:
            return self.current
        raise StopIteration


#
# iterator = CountdownIterator(10)
# for item in iterator:
#     print(item, end=" ")
#
# iterator = CountdownIterator(0)
# for item in iterator:
#     print(item, end=" ")

from math import ceil


class SequenceRepeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.number:
            return self.sequence[self.current % len(self.sequence)]
        raise StopIteration


#
# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end='')
#
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end='')


def solution():

    def integers():
        count = 0
        while True:
            count += 1
            yield count

    def halves():
        for i in integers():
            yield i/2

    def take(n, seq):
        my_list = []
        for i in range(n):
            current_value = next(seq)
            my_list.append(current_value)
        return my_list

    return take, halves, integers

#
# take = solution()[0]
# halves = solution()[1]
# print(take(0, halves()))
#
# take = solution()[0]
# halves = solution()[1]
# print(take(5, halves()))


def fibonacci():

    previous_number = 0
    current_number = 1
    while True:
        yield previous_number
        previous_number, current_number = current_number, previous_number + current_number

#
# generator = fibonacci()
# for i in range(5):
#     print(next(generator))
# generator = fibonacci()
# for i in range(1):
    print(next(generator))


def read_next(*args):
    for arg in args:
        for element in arg:
            yield element

#
# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
#     print(item, end='')
# for i in read_next("Need", (2, 3), ["words", "."]):
#     print(i)

def is_prime(n):
    if n < 2:
        return False

    s = [True] * (n + 1)
    s[0] = s[1] = False

    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return s[n]

def get_primes(iterable):
    for element in iterable:
        if is_prime(element):
            yield element

#
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
# print(list(get_primes([-2, 0, 0, 1, 1, 0])))




def possible_permutations(ls) :
    if len(ls) <= 1:
        yield ls
    else:
        for i in range(len(ls)) :
            for perm in possible_permutations(ls[:i] + ls[i + 1:]):
                yield [ls[i]] + perm


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
