class PatrolGrid:
    def __init__(self, data : list[list[str]], starting_point : list):
        self.data = data
        self.point = starting_point

    def __getitem__(self, index):
        if index[0] < 0 or index[0] >= len(self.data) or \
           index[1] < 0 or index[1] >= len(self.data[index[0]]):
            raise IndexError("Index out of bounds.")
        return self.data[index[0]][index[1]]
    
    def print(self):
        for d in self.data:
            print(d)
        print('\n')
    
    def __go_up__(self):
        while self.data[self.point[0]][self.point[1]] != '#':
            self.data[self.point[0]][self.point[1]] = 'X'
            self.point[0] -= 1
        self.point[0] += 1
        
    def __go_down__(self):
        while self.data[self.point[0]][self.point[1]] != '#':
            self.data[self.point[0]][self.point[1]] = 'X'
            self.point[0] += 1
        self.point[0] -= 1

    def __go_right__(self):
        while self.data[self.point[0]][self.point[1]] != '#':
            self.data[self.point[0]][self.point[1]] = 'X'
            self.point[1] += 1
        self.point[1] -= 1
    
    def __go_left__(self):
        while self.data[self.point[0]][self.point[1]] != '#':
            self.data[self.point[0]][self.point[1]] = 'X'
            self.point[1]-= 1
        self.point[1] += 1

    def go_till_end(self):
        self.data[self.point[0]][self.point[1]] = 'X'
        while True:
            try:
                self.__go_up__()
                self.__go_right__()
                self.__go_down__()
                self.__go_left__()
            except IndexError:
                break

    def count_all_crosses(self) -> 0:
        res = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == 'X':
                    res += 1
        return res

def create_grid_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    data = []
    for i in range(len(lines)):
        data_line = []
        for j in range(len(lines[i]) - 1):
            data_line.append(lines[i][j])
            if lines[i][j] == '^':
                starting_point = [i, j]
        data.append(data_line)
    return PatrolGrid(data, starting_point)

grid = create_grid_from_file('input.txt')
grid.go_till_end()
print(grid.count_all_crosses())