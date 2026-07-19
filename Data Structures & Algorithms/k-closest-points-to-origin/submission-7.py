class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_point = []

        for point in points:
            distance = point[0]**2 + point[1]**2
            dist_point.append([distance,point])

        dist_point.sort()

        res = []

        for i in range(k):
            res.append(dist_point[i][1])

        return res