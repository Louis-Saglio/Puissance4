class Grid:

    VOID = '.'

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.data = [[self.VOID for _ in range(self.width)] for _ in range(self.height)]

    def __str__(self):
        rep = []
        for row in self.data:
            for cell in row:
                rep.append(' ')
                rep.append(cell)
            rep.append('\n')
        return ''.join(rep)

    def __setitem__(self, key: int, value: str):
        for i in range(len(self.data) - 1, -1, -1):
            if self.data[i][key] == self.VOID:
                self.data[i][key] = value
                break

    def get_playable_cols(self):
        return [i for i, cell in enumerate(self.data[0]) if cell == self.VOID]


if __name__ == '__main__':
    d = Grid(7, 5)
    d[0] = '0'
    d[4] = '1'
    d[4] = '0'
    print(d)
