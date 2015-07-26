
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

count = 0
current = 0
while True:
    count = count + 1
    oldval = current
    current = oldval + count
    divisors = factors(current)
    print "%i: %i divisors" % (current, len(divisors))
    if len(divisors) > 500:
        break
