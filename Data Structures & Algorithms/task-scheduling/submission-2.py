class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        max_heap = [x for x in cnt.values()]
        q = deque()
        time = 0
        heapq.heapify_max(max_heap)

        while max_heap or q:
            time += 1
            if max_heap:
                val = heapq.heappop_max(max_heap) - 1
                if val:
                    q.append([val, time+n])

            while q and q[0][1] == time:
                heapq.heappush_max(max_heap, q.popleft()[0])

        return time