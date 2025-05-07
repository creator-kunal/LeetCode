class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        
        min_time = [[float('inf')] * m for _ in range(n)]
        min_time[0][0] = 0 
        
        pq = [(0, 0, 0)]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while pq:
            current_time, row, col = heappop(pq)
            
            if current_time > min_time[row][col]:
                continue
                
            if row == n-1 and col == m-1:
                return current_time
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if 0 <= new_row < n and 0 <= new_col < m:
                    start_move_time = max(current_time, moveTime[new_row][new_col])
                    
                    arrival_time = start_move_time + 1
                    
                    if arrival_time < min_time[new_row][new_col]:
                        min_time[new_row][new_col] = arrival_time
                        heappush(pq, (arrival_time, new_row, new_col))
        
        return min_time[n-1][m-1]  