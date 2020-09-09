numbers = [3, 5, 7, 9, 4, 8, 15, 16, 23, 42]

is_there_any_odd_number = False
is_odd = lambda num: num % 2 == 1


def fun(num):
    print(f"fun({num})")
    return num % 2 == 1


for num in numbers:
    if is_odd(num):
        is_there_any_odd_number = True
        break
print(is_there_any_odd_number)

# print(any(map(is_odd, numbers)))
print(all(map(fun, numbers)))
