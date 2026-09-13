class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set()

        st = [0]
        while st:
            room = st.pop()
            visited_rooms.add(room)
            for key in rooms[room]:
                if key not in visited_rooms:
                    st.append(key)
        
        return len(rooms) == len(visited_rooms)