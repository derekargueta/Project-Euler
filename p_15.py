# For an n x n grid, the number of lattice paths available is equivalent
# to the max value of row n*2 in Pascal's Triangle


class PascalTriangle(object):

    def __init__(self):
        self.rows = []

    def get_next_row(self):
        if self.rows == []:
            self.rows.append([1, 1])
            return

        new_row = [1]
        ############################
        last_row = self.rows[len(self.rows) - 1]
        for x in range(0, len(last_row) - 1):
            new_row.append(last_row[x] + last_row[x + 1])
        ############################
        new_row.append(1)
        self.rows.append(new_row)
        print(max(new_row))

if __name__ == '__main__':
    triangle = PascalTriangle()
    for x in range(0, 40):
        triangle.get_next_row()
