import numpy as np

# min_num = 2
# max_num = 1000
# answer = []

# for i in range(min_num, max_num):
#     prime_num = i
#     for j in range(2, i):
#         if i % j == 0:
#             prime_num = 0
#             break

#     if prime_num == i:
#         prime_num ==
#         answer.append(i)

# print(sum(answer))

# x = -125
# epsilon = 0.01
# step = epsilon**2
# num_guesses = 0

# if x < 0:
#     low = min(-1, x)
#     high = 0
# else:
#     low = 0
#     high = max(1, x)

# ans = (low + high) / 2

# while abs(ans**3 - x) >= epsilon:
#     num_guesses += 1
#     if ans**3 < x:
#         low = ans
#     else:
#         high = ans

#     ans = (low + high) / 2

# print(f'number of guesses : {num_guesses}')

# if (abs(ans**3 - x) >= epsilon):
#     print(f'failed on square root of {x}')

# else:
#     print(f'{ans} is close to cube of {x}')

# Newton-Raphson for square root
k = 108
epsilon = 0.00001
guess = k / 2
num_guesses = 0
while abs(guess**2 - k) > epsilon:
    num_guesses += 1
    guess = guess - (((guess**2) - k) / (2 * guess))

print(f'Square root of {k} is about {guess}')
print(f'it took {num_guesses} times')
