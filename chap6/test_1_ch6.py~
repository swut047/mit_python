t1 = (1, 'two', 3)
t2 = (t1, 3.25)
t3 = 3 * ('a', 2)
print(t1)
print(t2)
print(t2[0])
print(t1 + t2)
print((t1 + t2)[2:5])

t4 = [1, 2, 3]
t4_tuple = tuple(t4)

print(sum(t4) / len(t4))
print(sum(t4_tuple) / len(t4_tuple))

t5 = []
print(type(t5))

l1 = [[]] * 2
l2 = [[], []]
print(l1)
print(l2)

L.append(L)
print(L is L[-1])


def append_val(val, list_1=[]):
    list_1.append(val)
    print(list_1)


append_val(3)
append_val(4)

L = [1, 2, 3]
L_clone = L[:]
print(L is L_clone)

L.append(4)
print(L)
print(L_clone)

prime_numbers = [
    x for x in range(2, 100) if all(x % y != 0 for y in range(2, x))
]

print(prime_numbers)

non_prime_numbers = [
    x for x in range(2, 100) if any(x % y == 0 for y in range(2, x))
]

print(non_prime_numbers)

L = list(map(min, [1, 3, 5], [2, 4, 6]))
print(L)

for i in map(min, [1, 3, 5], [2, 4, 6]):
    print(i)


def f(L1, L2):
    answer = 0
    for i in map(lambda x, y: x**y, L1, L2):
        answer += i

    return answer


L1 = [1, 3, 5]
L2 = [2, 4, 6]
print(f(L1, L2))  # very big

text = 'fuck you naoki'
print(text.split(' '))

baseball_teams = {'Dodgers', 'Giants', 'Padres', ' Rockies'}
football_teams = {'Giants', 'Eagles', 'Cardinals', 'Cowboys'}
print(type(baseball_teams))

baseball_teams.add('Tigers')
football_teams.update(['Patriots', 'Jets'])
print(baseball_teams)
print(football_teams)
print(baseball_teams.intersection(football_teams))
print(baseball_teams & football_teams)
print(baseball_teams.difference(football_teams))
print(baseball_teams - football_teams)
print({'Padres', 'Eagles'}.issubset(baseball_teams))
print({'Padres', 'Eagles'} <= baseball_teams)


def get_min(d):
    alphabet_list = sorted(list(d.keys()))
    return d[alphabet_list[0]]


d = {'x': 11, 'b': 12}
print(get_min(d))
# d.get(k, v) : if first argument is in d -> d[k], otherwise -> v
print(d.get('c', 'fuck'))

number_to_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 10: 'ten'}
word_to_number = {w: d for d, w in number_to_word.items()}

gen_code_keys = (lambda book, plain_text:
                 ({c: str(book.find(c))
                   for c in plain_text}))

plain_text = 'no is no'
book = 'Once upon a time, in a house in a far away'
don_quixote = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing."

print(gen_code_keys(book, plain_text))
print(gen_code_keys(don_quixote, plain_text))

join_test = ''.join('*' + 'fuck')
print(join_test)

gen_decode_keys = (lambda book, cipher_text:
                   {s: book[int(s)]
                    for s in cipher_text.split('*')})

print(gen_decode_keys(don_quixote, '1*13*2*6*57*2*1*13'))

target = '22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11'


def decoder(target, book):
    answer = []
    target_list = list(target.split('*'))
    for t in target_list:
        answer.append(book[int(t)])

    return ''.join(answer)


print(decoder(target, don_quixote))
