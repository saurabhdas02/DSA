from multiprocessing import Pool, cpu_count


def square(n):
    return n * n


if __name__ == "__main__":
    with Pool(cpu_count()) as pool:
        results = pool.map(square, range(10))
    print(results)
