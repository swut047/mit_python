def harmonic_sum(n):
    if n == 1:
        return 1 / n
    else:
        return 1 / n + harmonic_sum(n - 1)


print(harmonic_sum(3))


def is_palindrome(s):
    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c

        return letters

    def is_pal(s):
        if len(s) < 1:
            return True

        else:
            return s[0] == s[-1] and is_palindrome(s[1:-1])

    return is_pal(to_chars(s))


print(is_palindrome('foof'))
print(is_palindrome('fuck'))


def fib(x):
    global num_fib_calls
    num_fib_calls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def test_fib(n):
    for i in range(n + 1):
        global num_fib_calls
        num_fib_calls = 0
        print('fib of', i, '=', fib(i))
        print('fib called', num_fib_calls, 'times')


test_fib(6)
