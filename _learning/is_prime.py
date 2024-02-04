# def find_primes(n):
# if n <= 1:
# return []
# for i in range(2, n + 1):
# if isprime(i):
# yield i
# return [x for x in find_primes(n)]


def prime_numbers(n):
    prime_list = []
    for i in range(2, int(n ** 0.5) + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    return prime_list
prime_numbers(30)
def prime_numbers(n):
    prime_list = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    return prime_list

def prime_numbers(n):
    prime_list = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    return prime_list


prime_numbers(30)
