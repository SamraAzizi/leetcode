class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        earliest = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                # Land -> Water
                land_finish = landStartTime[i] + landDuration[i]
                finish1 = max(land_finish, waterStartTime[j]) + waterDuration[j]

                # Water -> Land
                water_finish = waterStartTime[j] + waterDuration[j]
                finish2 = max(water_finish, landStartTime[i]) + landDuration[i]

                earliest = min(earliest, finish1, finish2)

        return earliest