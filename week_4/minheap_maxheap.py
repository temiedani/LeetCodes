import heapq

if __name__ == "__main__":
    x = [1, 5, 4, 3, 2, 5, 16, 27, 11]
    maxHeap = [-i for i in x]
    heapq.heapify(x)
    heapq.heapify(maxHeap)
    print("minheap", end="\n")

    print("\nnsmallest", end="\n")
    print(heapq.nsmallest(2, x))

    print("\nnlargest", end="\n")
    print(heapq.nlargest(2, x))

    for i in range(len(x)):
        print(heapq.heappop(x), end="-")
    print("\nmaxheap", end="\n")

    for i in range(len(maxHeap)):
        print(-1*(heapq.heappop(maxHeap)), end="-")
    print()
