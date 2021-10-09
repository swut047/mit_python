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


def find_root_2(x, power, epsilon):
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
