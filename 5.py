def is_divisible(n):
    """Checks if n can be evenly divided by nums 2 - 20"""
    for div in [7, 11, 13, 15, 16, 17, 18, 19, 20]:
        if n % div != 0:
            print(n, 'not divisible by', div)
            return False

    print(n, 'is divisible!')
    return True


if __name__ == '__main__':
    n = 20
    while not is_divisible(n):
        n += 20
