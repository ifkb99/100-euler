from sys import argv

def is_palindrome(n):
    return str(n) == str(n)[::-1]


def sort_tup(tup):
    return (tup[1], tup[0]) if tup[0] > tup[1] else tup


def largest_palindrome_from(a, b):
    queue = [(a, b)]
    d = {}

    while len(queue) > 0:
        (n1, n2) = queue.pop(0)
        sorted = sort_tup((n1, n2))
        if sorted in d:
            continue
        else:
            d[sorted] = n1 * n2
        if is_palindrome(n1 * n2):
            print ('Palindrome found!', n1 * n2, n1, n2)
            return n1 * n2
        print(n1, '*', n2, '=', n1 * n2)
        queue.append((n1-1, n2))
        queue.append((n1, n2-1))


if __name__ == '__main__':
    if len(argv) != 3:
        print(largest_palindrome_from(999, 999))
    else:
        print(largest_palindrome_from(int(argv[1]), int(argv[2])))
