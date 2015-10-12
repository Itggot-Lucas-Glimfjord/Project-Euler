prime_cache = [2, 3, 5, 7, 11, 13, 17, 19]


def factor(num, factorial={}):
    for prime in prime_cache:
        if num%prime == 0:
            if prime in factorial.keys():
                factorial[prime] += 1
            else:
                factorial[prime] = 1
            factor(num=num/prime, factorial=factorial)

    return factorial

def smallest_multiple(max):
    smallest_mult = {}
    curr = 2
    while curr<=max:
        factors = factor(num=curr, factorial={})
        curr +=1

        for key in factors.keys():
            if smallest_mult.has_key(key):






smallest_multiple(20)










