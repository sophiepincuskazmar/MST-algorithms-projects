import math
import heapq

def printMST(parent, graph, v): 
        print("Edge \tWeight")
        for i in range(1, v): 
            print(parent[i], "-", i, "\t", graph[i][ parent[i] ])

def prims(adjMatrix, v): #adjMatrix is a 2d list
	inMST = [False] * v
	priority = [math.inf] * v
	predecessor = [None] * v

	priority[0] = 0
	predecessor[0] = -1

	for i in range(v):
		min = math.inf
		minIndex = 0
		for j in range(v):
			if priority[j] < min and inMST[j] == False:
				min = priority[j]
				minIndex = j

		inMST[minIndex] = True

		for j in range(v):
			if adjMatrix[minIndex][j] > 0 and inMST[j] == False and priority[j] > adjMatrix[minIndex][j]:
				priority[j] = adjMatrix[minIndex][j]
				predecessor[j] = minIndex

	printMST(predecessor, adjMatrix, v)


# def heapPrims(adjList, v):
# 	inMST = [False] * v
# 	predecessor = [None] * v

# 	priority = [math.inf] * v
# 	priority[0] = 0
# 	heapq.heapify(priority)

# 	while len(priority) > 0:
# 		min = heapq.heappop(priority)




matrix = [[0, 5, 1, 3],[5, 0, 3, 1],[1, 3, 0, 2],[3, 1, 2, 0]]
prims(matrix, 4)





