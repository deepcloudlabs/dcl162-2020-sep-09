from multiprocessing import Pool


def times2(x):
    return x * 2


def parallel_map(xs, chunk=50000):
    with Pool(8) as P:        x = P.map(times2, xs, chunk)

    return x


if __name__ == '__main__':
    N = 1000000
    data = range(N)
    parallel_map(data)
