class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        direction = 0
        x, y = 0, 0
        max_distance = 0
        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -2:  # turn left
                direction = (direction - 1) % 4
            elif command == -1:  # turn right
                direction = (direction + 1) % 4
            else:  # move forward
                for _ in range(command):
                    next_x, next_y = x, y
                    if direction == 0:  # north
                        next_y += 1
                    elif direction == 1:  # east
                        next_x += 1
                    elif direction == 2:  # south
                        next_y -= 1
                    elif direction == 3:  # west
                        next_x -= 1

                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        max_distance = max(max_distance, x**2 + y**2)
                    else:
                        break

        return max_distance