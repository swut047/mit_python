import numpy as np
from module_test import test
from test_1 import bisection_solve


def fuck():
    '''just print fuck'''
    print(fuck)


x, p, e = 0.25, 2, 0.001
result = test.find_root(x, p, e)
print(result)

low, high = 0, 10000

#  lambda expression
print(bisection_solve(99, lambda ans: ans**2, 0.01, low, high))


def answer(num, denm):
    return num / denm if denm != 0 else None


print(answer(10, 0))

s = 'fuck you you'
s.find('you')


def find_last(s, sub):
    ans = None
    s_tmp = s

    while s_tmp.find(sub) > 0:
        print(s_tmp.find(sub))
        ans += s_tmp.find(sub) + len(sub)
        print(f"ans:{ans}")
        s_tmp = s_tmp[ans:]
        print(s_tmp)
    return ans


s = 'fuck you you you'
sub = 'you'
print(find_last(s, sub))
print(len(s))
