class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])

        h = []
        nr_of_passengers = 0

        for pass_nr, start, end in trips:
            while h and h[0][0] <= start:
                nr_of_passengers -= h[0][1]
                heapq.heappop(h)
            heapq.heappush(h, (end, pass_nr))
            nr_of_passengers += pass_nr
            if nr_of_passengers > capacity:
                return False
        
        return True