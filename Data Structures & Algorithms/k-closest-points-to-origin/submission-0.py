class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap =[]
        n = len(points)
        
        def dist(x, y):
            return x*x + y*y

        for x, y in points:
            d = dist(x, y)
            if len(max_heap) < k:
                heapq.heappush_max(max_heap, (d, x, y))
            else:
                heapq.heappushpop_max(max_heap, (d, x, y))

        return [[x, y] for d, x, y in max_heap]