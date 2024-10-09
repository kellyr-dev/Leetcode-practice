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

# 373. Find K Pairs with Smallest Sums (TLE)
def kSmallestPairs(list1, list2, k):

    # Working but getting TLE
    minHeap = []

    for i in range(len(list1)):
        for j in range(len(list2)):
            n1 = -list1[i]
            n2 = -list2[j]
            key = (n1+n2, [list1[i], list2[j]])
            if len(minHeap) < k:
                heapq.heappush(minHeap, key)
            else:
                if n1 + n2 > minHeap[0][0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, key)

    print(minHeap)
    result = []
    for i in range(len(minHeap)):
        aux = minHeap[i][1]
        result.append(aux)

    return result


if __name__ == '__main__':
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    print(kSmallestPairs(nums1, nums2, k))