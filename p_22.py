
with open('p_22.txt', 'rb') as f:
    names = sorted(f.readline().replace('"', '').split(','))
    index = 1
    tot = 0
    for name in names:
        tot += sum(ord(char) - 64 for char in name) * index
        index += 1
    print(tot)
