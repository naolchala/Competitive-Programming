import math

class Solution:
    def distance(self, x, y):
        return math.sqrt(x**2 + y**2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_with_distance = []
        for point in points:
            points_with_distance.append((self.distance(point[0], point[1]), point))
            
        points_with_distance.sort()
        return [x[1] for x in points_with_distance[:k]]
