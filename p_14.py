
num = 2
x = 0
biggest_chain = 0

while num < 1000000:

    chain_length = 1
    x = num
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        chain_length = chain_length + 1

    if chain_length > biggest_chain:
        print "%i yielded chain of %i" % (num, chain_length)
        biggest_chain = chain_length
    num = num + 1
