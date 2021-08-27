def mutateTheArray(n, a):
    return [a[0] + a[1]] + [sum(a[x-1:x+2]) for x in range(1, len(a))] if n>1 else a

