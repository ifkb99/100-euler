# longest collatz sequence under 1 million

def collatz(n, d, q):
    # n is seed, d is memoized dict
    # q is tuple of nums that need to be added to dict when result is found
    for idx in range(len(q)):
        # add 1 to number of steps in collatz
        q[idx][1] += 1
    if n in d:
        for entry in q:
            d[entry[0]] = d[n] + entry[1]
    elif n % 2 == 0:
        q.append([n, 0])
        collatz(n//2, d, q)
    else:
        q.append([n, 0])
        collatz(3*n+1, d, q)


if __name__ == '__main__':
    d = {1 : 0}
    most_steps = 0
    num_steps = 0
    for i in range(2, 1000001):
        #print('Starting collatz for', i)
        collatz(i, d, [])
        #print('Collatz for', i, 'is', d[i])
        if d[i] > num_steps:
            num_steps = d[i]
            most_steps = i
            print('New max found at', i, 'with', d[i], 'steps!')

    print('Max steps was', num_steps, 'for', most_steps)
