# # factorials


def factorial(n):
    if n == 0:
        return 1
    ans = int(1)
    i = int(1)
    while i <= n:
        ans *= i

        i += 1
    return ans


def rec_factorial(n):
    if n == 0:
        return 1
    return n * rec_factorial(n - 1)


print(factorial(4))
print(rec_factorial(4))

# prime


def prime(n):
    if n == 2:
        return True
    i = int(2)
    while i < n:
        if n % i == 0:
            return False
        i += 1

    return True


def rec_prime(n, i=2):
    if n == i:
        return True
    elif n % i == 0:
        return False
    else:
        return rec_prime(n, i + 1)


print(prime(7), rec_prime(7))

x = 10


def change():
    global x
    x = x + 5
    print(x)


change()
print(x)


def fun(var):
    let = ["a", "e", "i", "o", "u"]
    if var in let:
        return True
    return False


# using filter()
sequence = ["s", "u", "d", "e", "s", "h"]
filtered = filter(fun, sequence)

for s in filtered:
    print(s)

x = lambda a, b, c: a * b * c
print(x(10, 202, 40))


def addition(n):
    return n + n


num = [10, 1, 1, 1, 13, 5, 6]

result = map(addition, num)

print(list(result))

print(num)
