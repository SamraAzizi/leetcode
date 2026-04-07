class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.width = width
        self.height = height
        self.dx_dy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.dir_names = ["East", "North", "West", "South"]
        self.dir_idx = 0 
        self.x = 0
        self.y = 0

        self.perimeter_moves = []
        for i in range(self.width - 1):
            self.perimeter_moves.append((1, 0))
        for i in range(self.height - 1):
            self.perimeter_moves.append((0, 1))
        for i in range(self.width - 1):
            self.perimeter_moves.append((-1, 0))
        for i in range(self.height - 1):
            self.perimeter_moves.append((0, -1))
        self.perimeter_len = len(self.perimeter_moves)
        self.perimeter_pos = 0 

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.width == 1 or self.height == 1:
            return

        steps = num % self.perimeter_len
        for _ in range(steps):
            dx, dy = self.perimeter_moves[self.perimeter_pos]
            self.x += dx
            self.y += dy
            self.perimeter_pos = (self.perimeter_pos + 1) % self.perimeter_len
        
        if self.perimeter_len > 0:
            if self.perimeter_pos == 0:
                self.dir_idx = 3 
            elif self.perimeter_pos <= self.width - 1:
                self.dir_idx = 0
            elif self.perimeter_pos <= self.width - 1 + self.height - 1:
                self.dir_idx = 1
            elif self.perimeter_pos <= 2 * (self.width - 1) + self.height - 1:
                self.dir_idx = 2
            else:
                self.dir_idx = 3

    def getPos(self):
        """
        :rtype: List[int]
        """
        return [self.x, self.y]

    def getDir(self):
        """
        :rtype: str
        """
        return self.dir_names[self.dir_idx]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()