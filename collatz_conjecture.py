def collatz_conjecture(x):
    count = 1
    while x != 4:
        if x % 2 == 0:
            x = x/2
            count += 1
        elif x%2 != 0:
            x = 3*x + 1
            count += 1
    return count
