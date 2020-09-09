def sequence(n):  # generator
    while n > 1:
        print(f"sequence({n})")
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield n


def squared(nums): # generator
    for num in nums:
        print(f"squared:: {num}")
        yield num * num


for num in squared(sequence(7)):  # pipeline
    print(f"for loop: {num}")
