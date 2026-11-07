import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        
        busy = []
        ans = []
        current_time = 0
        
        for j in range(len(tasks)):
            if not free:
                current_time = max(current_time, busy[0][0])
            else:
                current_time = max(current_time, j)
            
            while busy and busy[0][0] <= current_time:
                end, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            
            w, i = heapq.heappop(free)
            ans.append(i)
            
            heapq.heappush(busy, (current_time + tasks[j], w, i))
            
        return ans