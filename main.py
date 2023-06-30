def simpleDiv(num):
    n = 0
    divisors = []
    div = 2
    while True:
        n += 1
        if num % div == 0:
            divisors.append(div)
            num = num // div
            if num!=1: divisors.append(num)
            div = 2
        else:
            div += 1
            if div > num:
                return sorted(set(divisors)), n


def od(num1, num2):
    divisors1 = simpleDiv(num1)[0]
    divisors2 = simpleDiv(num2)[0]
    print(divisors1, divisors2, sep='\n')

    if len(divisors1) == 1 and len(divisors2) == 1:
        if num1 != num2:
            return None
        else:
            return num1
    else:
        divisors = list(set(divisors1) & set(divisors2))

    if len(divisors) == 0: return None

    min = divisors[0]
    max = min
    for item in divisors:
        if item > max: max = item
        if item < min: min = item


    return min, max


if __name__ == '__main__':
    print(od(512, 1024))
