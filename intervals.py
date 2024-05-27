# Summary Pseudocode pattern
# prev = A
# current = B

    # if current_start < prev_star:
    #   if current_end > prev_end:
        # case 5)
    #   else:
    #       # if current_end < prev_start:
                # case 6)
            # else:
                # case 4)
    # else:
        # if current_start > prev_end:
            # case 1)
        # else:
            # if current_end < prev_end:
                # case 3)
            # else
                # case 2)

# 56. Merge Intervals
import heapq


def basicMerge(intervals):

    # step 1 initialize prev
    # step 2 order by startings points
    # step 3 apply summary about 6 possibles cases

    if len(intervals) <= 1:
        return intervals

    intervals.sort() # O(nlogn)
    print(intervals)

    res = []
    prev_start = intervals[0][0]
    prev_end = intervals[0][1]


    for i in range(1, len(intervals)): # O(n)
        print(f"prev: [{prev_start}:{prev_end}]")
        current_start = intervals[i][0]
        current_end = intervals[i][1]
        print(f"current: [{current_start}:{current_end}]")

        if current_start <= prev_end:
            prev_end = max(current_end, prev_end)
        else:
            res.append([prev_start, prev_end])
            prev_start = current_start
            prev_end = current_end

    res.append([prev_start, prev_end])
    return res

# 57. Insert Interval
def insertIntervals(intervals, newInterval):


    # two options
    # a.- a first loop to insert newInterval and new loop to apply same algorithm that merge intervals
    # b.- insert and sort in-place it means at the same time (loop)

    if len(intervals) == 0:
        intervals.append(newInterval)
        return intervals

    print(intervals)
    inserted = False
    for i in range(len(intervals)):
        current_start = intervals[i][0]
        current_end = intervals[i][1]

        if current_start >= newInterval[0]:
            intervals.insert(i, newInterval)
            inserted = True

        if inserted:
            break

    if not inserted:
        intervals.append(newInterval)

    print(intervals)

    prev_start = intervals[0][0]
    prev_end = intervals[0][1]

    res = []
    for j in range(1, len(intervals)):
        current_start = intervals[j][0]
        current_end = intervals[j][1]
        if current_start <= prev_end:
            prev_end = max(current_end, prev_end)
        else:
            res.append([prev_start, prev_end])
            prev_start = current_start
            prev_end = current_end

    res.append([prev_start, prev_end])
    return res

# Conflicting appointments
def conflictingAppointments(intervals):

    if len(intervals) <= 1:
        return True

    intervals.sort()
    prev_start = intervals[0][0]
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):

        current_start = intervals[i][0]
        current_end = intervals[i][1]

        if current_start < prev_end:
            return False
        else:
            prev_start = current_start
            prev_end = max(current_end, prev_end)

    return True

# 253. Minimun Meeting Rooms II (my solution)
def minimunMeetingRoomIIOwn(intervals):

    if len(intervals) == 1:
        return 1

    if len(intervals) == 0:
        return 0

    print(f"intervals before: ", intervals)
    intervals.sort() # O(nlogn)
    print(f"intervals after: ", intervals)
    mergedIntervals = []
    for i in range(len(intervals)): # O(n^2) // need to improve this function
        current_start = intervals[i][0]
        current_end = intervals[i][1]
        print(f"current: [{current_start}:{current_end}]")
        if current_start == -1 or current_end == -1:
            continue

        else:
            for j in range(i+1, len(intervals)):
                aux_start = intervals[j][0]
                aux_end = intervals[j][1]
                print(f"aux: [{aux_start}: {aux_end}]")

                if current_end == aux_start:
                    current_end = aux_end
                    intervals[j][1] = -1
                    intervals[j][0] = -1


        mergedIntervals.append([current_start, current_end])

    print(f"mergedIntervals: ",mergedIntervals)

    if len(mergedIntervals) <= 1:
        return len(mergedIntervals)

    result = 1
    prev_start = mergedIntervals[0][0]
    prev_end = mergedIntervals[0][1]

    for i in range(1, len(mergedIntervals)): # O(n)
        current_start = mergedIntervals[i][0]
        current_end = mergedIntervals[i][1]

        if current_start < prev_end:
            result += 1
            prev_start = current_start
            prev_end = current_end

    return result

    # time complexity: O(nlogn) + O(n^2) + O(n)
    # space complexity: O(n)

# 253. Minimun Meeting Rooms II (two list)
def minimunMeetingRoomIITwoList(intervals):

    if len(intervals) == 0:
        return 0
    if len(intervals) == 1:
        return 1

    startTimes = []
    endTimes = []

    for i in range(len(intervals)):
        startTimes.append(intervals[i][0])
        endTimes.append(intervals[i][1])

    startTimes.sort()
    endTimes.sort()

    print(startTimes)
    print(endTimes)

    i = 0
    j = 0
    minRoom = 0
    for i in range(len(startTimes)):

        if startTimes[i] < endTimes[j]:
            minRoom += 1
        else:
            j += 1

    return minRoom

# 253. Minimun Meeting Rooms II (heap)
def minimunMeetingRoomIITwoHeap(intervals):

    if len(intervals) == 0:
        return 0
    if len(intervals) == 1:
        return 1

    intervals.sort()

    # will be used in the heap
    rooms = []
    heapq.heappush(rooms, intervals[0][1])

    for i in range(1, len(intervals)):
        print(rooms)
        if intervals[i][0] >= rooms[0]:
            heapq.heappop(rooms)

        heapq.heappush(rooms, intervals[i][1])

    return len(rooms)

if __name__ == '__main__':
    intervals = [[4,5], [2,3], [2,4], [3,5]]
    newInterval = [2,7]
    event1 = ["10:00","11:00"]
    event2 = ["14:00","15:00"]
    print(minimunMeetingRoomIITwoHeap(intervals))