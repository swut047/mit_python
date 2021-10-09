import numpy as np


def find_root(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None

    low = min(-1, x)
    high = max(1, x)

    # use bisection search
    ans = (high + low) / 2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans

        ans = (low + high) / 2

    return ans


def bisection_solve(x, eval_ans, epsilon, low, high):
    # use bisection search
    ans = (high + low) / 2
    while abs(eval_ans(ans) - x) >= epsilon:
        if eval_ans(ans) < x:
            low = ans
        else:
            high = ans

        ans = (low + high) / 2

    return ans


# writing test code is very important
def test_find_root(x_vals, powers, epsilons):
    for x in x_vals:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                if result == None:
                    val = 'No root exists'
                else:
                    val = 'OK'
                    if abs(result**p - x) >= e:
                        val = 'Bad'

                print(f'x = {x}, power = {p}, epsilon = {e} : {val}')


def mult(int1, int2=1):
    return int1 * int2


print(mult(2, 3))
print(mult(2, 1))
print(mult(2))
