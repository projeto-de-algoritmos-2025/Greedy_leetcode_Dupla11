class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key = lambda x : x[1])
        arrows = 1

        point = points[0][1]

        for i in range(len(points) - 1):
            if point < points[i + 1][0]:
                arrows += 1
                point = points[i + 1][1]

        return arrows