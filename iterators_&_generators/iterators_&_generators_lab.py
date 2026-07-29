class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current  >= self.end:
            raise StopIteration
        self.current  += 1
        return self.current

#
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)

class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start = len(iterable)
        self.end = 0
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            self.current -= 1

            return self.iterable[self.current]
        raise StopIteration


# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)

class VowelsIterator:
    def __init__(self, vowels):
        self.vowels = vowels
        self.current = -1
        self.end = len(vowels)


    def __iter__(self):

        return self

    def __next__(self):
        self.current += 1
        while self.current < self.end:
            if self.vowels[self.current].lower() in ['a', 'e', 'i', 'o','y', 'u']:
                return self.vowels[self.current]
            else:
                self.current += 1
        else:
            raise StopIteration


# my_string = VowelsIterator('Abcedifuty0o')
# for char in my_string:
#     print(char)

def squares(number: int):
    current = 1
    while current <= number:
        yield current ** 2
        current += 1



# print(list(squares(5)))

def gen_range(start: int, end: int):
    current = start
    while current <= end:
        yield current
        current += 1



# print(list(gen_range(1, 10)))

def reverse_text(text: str):
    current = len(text) - 1
    while current >= 0:
        yield text[current]
        current -= 1


#
# for char in reverse_text("step"):
#     print(char, end='')

