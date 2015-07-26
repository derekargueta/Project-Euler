import math

matrix = []

with open('13.txt', 'rb') as data:
    for line in data:
        line = line.replace('\n', '')
        matrix.append(list(line))

# print(matrix)
main_sum = 0
for i in range(49, -1, -1):
    tmp_sum = 0
    for line in matrix:
        tmp_sum += int(line[i]) * math.pow(10, (49-i))
    main_sum += tmp_sum

print(main_sum)
