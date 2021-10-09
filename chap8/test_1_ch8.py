import copy


def is_small(x, y):
    assert type(x) == int or type(x) == float, 'invalid x : {}'.format(x)
    assert type(y) == int or type(y) == float, 'invalid y : {}'.format(y)

    return min(x, y)


x, y = 3, 5
x, y = 'fuck', 5
x, y = 3.5, 5
print(is_small(x, y))

x = ['a', 'b']
y = x[:]
y.reverse()
print(x)
print(y)
print(x == y)

a = [[1, 2], [3, 4]]
b = copy.copy(a)
a.append([5, 6])
a[0].append(7)
print(a)
print(b)


def sum_digits(s):
    answer = 0
    for i in range(len(s)):
        try:
            answer += int(s[i])
        except ValueError:
            print(f'Invalid value : {s[i]}')
            continue

    return answer


input_words = 'a2b3c'
print(f'The answer for {input_words} is {sum_digits(input_words)}')


def find_an_even(L):
    for i in L:
        try:
            if i % 2 == 0:
                return i

        except:
            continue

    raise ValueError('no even number in the list')


L = [1, 3, 'a', 5]
find_an_even(L)
