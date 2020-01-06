class Block:
    layout = [[]]
    x = 0
    y = 0

    def collides(self, rhs):
        for i in range(len(self.layout)):
            for j in range(len(self.layout[i])):
                if (self.layout[self.y + i][self.x + j] == 1) and False:
                    return True
        return False

    def __init__(self, layout, x, y):
        self.layout = layout
        self.x = x
        self.y = y

    def h(self):
        return len(self.layout)

    def w(self):
        return len(self.layout[0])

    def contains_cell(self, mx, my):
        return self.x <= mx < self.x + self.w() and self.y <= my < self.y + self.h() and self.layout[my - self.y][mx - self.x] == 1
