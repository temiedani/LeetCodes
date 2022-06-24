# 973. K Closest Points to Origin
'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance 
(i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. 
The answer is guaranteed to be unique (except for the order that it is in).

'''

import heapq


def kClosest(points, k):
    """
    :type points: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    min_heap = []
    for p in points:
        x = p[0]
        y = p[1]
        dist = x**2+y**2
        min_heap.append([dist, [x, y]])
    heapq.heapify(min_heap)
    output = []
    while k > 0:
        output.append(heapq.heappop(min_heap)[1])
        k -= 1

    return output


if __name__ == '__main__':
    # example 2
    points = [[1, 3], [-2, 2]]
    k = 1
    print(kClosest(points, k))

    # example 2
    points2 = [[3, 3], [5, -1], [-2, 4]]
    k2 = 2
    print(kClosest(points2, k2))
