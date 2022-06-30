from queue import PriorityQueue, Queue
import pygame


def heuristic(Pos1, Pos2):
    x1, y1 = Pos1 
    x2, y2 = Pos2 
    return abs(y1 - y2) + abs(x1 - x2)

def ReconstructPath(path, current, drawFunc):
    while current in path:
        current = path[current]
        current.setPATH()
        drawFunc()

def AStar(DrawFunc,grid, start, end):
    """A* Algorithm: it is a best first algorithm which uses the 
    current cost to node + a heuristic value to decide the best 
    node to check next"""
    count = 0
    openSet = PriorityQueue()
    openSet.put((0, count, start))
    cameFrom = {}

    gScore = {cell: float("inf") for row in grid for cell in row}
    gScore[start] = 0
    fScore = {cell: float("inf") for row in grid for cell in row}
    fScore[start] = heuristic(start.getPos(), end.getPos())


    openSetHash = {start}
    while not openSet.empty():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = openSet.get()[2]
        openSetHash.remove(current)
        
        if current == end:
            ReconstructPath(cameFrom, current, DrawFunc)
            end.setGOAL()
            start.setSTART()
            return True
        
        for neighbour in current.neighbours:
            tentative_gScore = gScore[current] + 1

            if tentative_gScore < gScore[neighbour]:
                cameFrom[neighbour] = current
                gScore[neighbour] = tentative_gScore
                fScore[neighbour] = tentative_gScore + heuristic(neighbour.getPos(), end.getPos())
                if neighbour not in openSetHash:
                    count += 1 
                    openSet.put((fScore[neighbour], count, neighbour))
                    openSetHash.add(neighbour)
                    neighbour.setEDGE()
                
        DrawFunc()

        if current != start:
            current.setCLOSED()
    
    return False

# def BreathFirstSearch(grid, start, goal, DrawFunc):
#     Q = Queue
#     cameFrom = {}

#     Q.put(start)
    
#     while not Q.empty():
#         currentCell = Q.get()
#         if currentCell == goal:
#             ReconstructPath(cameFrom, currentCell, DrawFunc())
#             goal.setGOAL()
#             start.setSTART()
#             return True

#         for neighbour in currentCell.neighbours:
#             if not neighbour.isCLOSED():
#                 neighbour.setCLOSED()
#                 Q.put(neighbour)
#         DrawFunc()

#     return False




# let Q be a queue
#  3      label root as explored
#  4      Q.enqueue(root)
#  5      while Q is not empty do
#  6          v := Q.dequeue()
#  7          if v is the goal then
#  8              return v
#  9          for all edges from v to w in G.adjacentEdges(v) do
# 10              if w is not labeled as explored then
# 11                  label w as explored
# 12                  Q.enqueue(w)

    pass