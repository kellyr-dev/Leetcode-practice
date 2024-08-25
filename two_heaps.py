import heapq

# 480. Sliding Window Median (just naive solution)
def medianSlidingWindow(nums, k):

    result = []
    right = k
    start = 0
    start_aux = 0
    heapM = []

    while right <= len(nums): #O(n)
        heap_aux = []
        start_aux = start
        while start_aux < right: #O(k)
            heapq.heappush(heap_aux, nums[start_aux]) #O(log(k))
            start_aux+= 1

        print(heap_aux)
        heapM.append(heap_aux)
        start+=1
        right+= 1

    if k % 2 == 0:
        limit2 = int(k/2)
        limit1 = limit2-1
        for heaps in heapM:
            for i in range(limit1):
                heapq.heappop(heaps)

            value1 = heapq.heappop(heaps)
            value2 = heapq.heappop(heaps)
            aux = (value1 + value2)/2
            result.append(aux)

    else:
        limit = k//2
        for heaps in heapM:
            for i in range(limit):
                heapq.heappop(heaps)
            result.append(heapq.heappop(heaps))

    return result


if __name__ == '__main__':

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(medianSlidingWindow(nums, k))