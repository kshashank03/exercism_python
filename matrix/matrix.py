class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = matrix_string.splitlines()

    def row(self, index):
        x = [int(i) for i in self.rows[index - 1].split(" ")]
        return x
    
    def column(self, index):
        column_list = []
        for i in self.rows:
            x = i.split(" ")
            column_list.append(int(x[index - 1]))
        return column_list