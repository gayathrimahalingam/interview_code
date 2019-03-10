'''
ContinuousMedian:Numbersarerandomlygeneratedandpassedtoamethod.Writeaprogram to find and maintain the median value as new values are generated.
'''

'''
Solution: Use two priority heaps: a max heap for the values below the median
and a min heap for values above the median.
'''

import os
import heapq

def addNewNumber(randnum):
    # maxHeap.size() >= minHeap.size() condition must be maintained
    if len(maxHeap) == len(minHeap):
        if minHeap[0] is not None and randnum > minHeap[0]:
            heapq.heappush(maxHeap, heapq.heappop(minHeap))
            heapq.heappush(minHeap, randnum)
        else:
            heapq.heappush(maxHeap, randnum)
    else:
        if randnum < maxHeap[0]:
            # take one from maxHeap and push it to minHeap
            # add randnum to maxHeap
            heapq.heappush(minHeap, heapq.heappop(maxHeap))
            heapq.heappush(maxHeap, randnum)
        else:
            # push to minHeap
            heapq.heappush(minHeap, randnum)

def getMedian():
    # maxHeap is always at least as big as minHeap. So if maxHeap is empty, then minHeap is also
    if len(maxHeap) == 0:
        return 0
    if len(maxHeap) == len(minHeap):
        # median is avg of min and max heaps root
        return (minHeap[0] + maxHeap[0]) / 2.0
    else:
        return maxHeap[0]
