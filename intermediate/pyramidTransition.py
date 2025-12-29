class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        from collections import defaultdict

        allowed_map = defaultdict(list)
        for triplet in allowed:
            allowed_map[triplet[:2]].append(triplet[2])

        def can_build(current_level):
            if len(current_level) == 1:
                return True

            next_level_options = []

            for i in range(len(current_level) - 1):
                pair = current_level[i:i + 2]
                if pair in allowed_map:
                    next_level_options.append(allowed_map[pair])
                else:
                    return False

            def backtrack(index, next_level):
                if index == len(next_level_options):
                    return can_build(''.join(next_level))

                for char in next_level_options[index]:
                    next_level.append(char)
                    if backtrack(index + 1, next_level):
                        return True
                    next_level.pop()

                return False

            return backtrack(0, [])

        return can_build(bottom)