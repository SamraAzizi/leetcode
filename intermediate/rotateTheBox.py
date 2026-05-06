class Solution:
    def rotateTheBox(self, box):

        rows = len(box)
        cols = len(box[0])

        # Apply gravity
        for r in range(rows):

            empty = cols - 1

            for c in range(cols - 1, -1, -1):

                if box[r][c] == '*':
                    empty = c - 1

                elif box[r][c] == '#':

                    box[r][c], box[r][empty] = \
                    box[r][empty], box[r][c]

                    empty -= 1

        # Rotate matrix
        ans = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):

                ans[c][rows - 1 - r] = box[r][c]

        return ans