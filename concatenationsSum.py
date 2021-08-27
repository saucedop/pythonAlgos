def concatenationsSum(a):
    sum = 0
    for i in range (len(a)):
        for j in range(len(a)):
            prod = str(a[i]) + str(a[j])
            sum += int(prod)
    return sum