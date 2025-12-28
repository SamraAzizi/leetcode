class Solution(object):
    def mostBooked(self, n, meetings):
        import heapq

        # Sort meetings by start time
        meetings.sort(key=lambda x: x[0])

        # Min-heap for available rooms
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        # Min-heap for ongoing meetings (end_time, room_index)
        ongoing_meetings = []

        # Count of bookings for each room
        booking_count = [0] * n

        for start, end in meetings:
            # Free up rooms that have finished their meetings
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                _, room_index = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, room_index)

            if available_rooms:
                # Assign the meeting to the lowest indexed available room
                room_index = heapq.heappop(available_rooms)
                booking_count[room_index] += 1
                heapq.heappush(ongoing_meetings, (end, room_index))
            else:
                # All rooms are occupied, delay the meeting
                end_time, room_index = heapq.heappop(ongoing_meetings)
                new_end_time = end_time + (end - start)
                booking_count[room_index] += 1
                heapq.heappush(ongoing_meetings, (new_end_time, room_index))

        # Find the room with the maximum bookings
        max_booked_room = max(range(n), key=lambda x: booking_count[x])
        return max_booked_room