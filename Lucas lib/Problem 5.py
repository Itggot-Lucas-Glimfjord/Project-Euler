prime_cache = [2, 3, 5, 7, 11, 13, 17, 19]


def smallest_multiple(max):
    curr = 2
    while curr<=max:
        factorial = {}

        if curr > 1:
            for prime in prime_cache:
                value = curr
                while value % prime == 0 and curr != prime:
                    value / prime
                    if prime in factorial.keys():
                        factorial[prime] += 1
                    else:
                        factorial[prime] = 1
        curr += 1

        print factorial

smallest_multiple(20)










