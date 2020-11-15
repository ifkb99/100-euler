"""

Special Pythagorean Triplet

Find a set of three natural numbers such that:

    a < b < c AND a**2 + b**2 = c**2 AND a + b + c = 1000
    
    Solve the last equation for c = x (or 1000) - a - b
    Substitute c^2 in second equation to get a^2 + b^2 = a^2 + b^2 - 2ax - 2bx + 2ab + x^2
    Simplify and solve for b to get b = (ax - x^2 / 2) / (a - x)
    Increase a until b is a whole number, then c can be calculated

"""

def pythag_trip(target):
    t_mod = target * target / 2
    for a in range(1, target // 3 + 1):
        if ((a * target - t_mod) / (a - target)).is_integer():
            b = int((a * target - t_mod) / (a - target))
            return a, b, target - a - b
    print('No triplet found for', target)
        


if __name__ == '__main__':
    print(pythag_trip(1000))
