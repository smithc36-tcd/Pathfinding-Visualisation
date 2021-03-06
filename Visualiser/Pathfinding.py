from queue import PriorityQueue
from random import choice
import pygame


def heuristic(Pos1, Pos2):
    x1, y1 = Pos1 
    x2, y2 = Pos2 
    return abs(y1 - y2) + abs(x1 - x2)

def ReconstructPath(prev, current, drawFunc, AnimatePath):
    while current in prev:
        current = prev[current]
        current.setPATH(AnimatePath)
    drawFunc()

def AStar(DrawFunc,grid, start, end, VisualiseAlgorithm, AnimatePath):
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
            DrawFunc()
            ReconstructPath(cameFrom, current, DrawFunc, AnimatePath)
            end.setGOAL(VisualiseAlgorithm)
            start.setSTART(VisualiseAlgorithm)
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
                    neighbour.setEDGE(VisualiseAlgorithm)
        
        # if VisualiseAlgorithm:
        #     DrawFunc()

        if current != start:
            current.setCLOSED(VisualiseAlgorithm)
    # DrawFunc()
    
    return False



def Djikstra(DrawFunc,grid, start, goal, VisualiseAlgorithm, AnimatePath):

    count = 0
    openSet = PriorityQueue()
    openSet.put((0, count, start))
    cameFrom = {}

    dist = {cell: float("inf") for row in grid for cell in row}
    dist[start] = 0

    openSetHash = {start}
    while not openSet.empty():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = openSet.get()[2]
        openSetHash.remove(current)
        
        if current == goal:
            DrawFunc()
            ReconstructPath(cameFrom, current, DrawFunc, AnimatePath)
            goal.setGOAL(VisualiseAlgorithm)
            start.setSTART(VisualiseAlgorithm)
            return True
        
        for neighbour in current.neighbours:
            tentative_dist = dist[current] + 1

            if tentative_dist < dist[neighbour]:
                cameFrom[neighbour] = current
                dist[neighbour] = tentative_dist
                if neighbour not in openSetHash:
                    count += 1 
                    openSet.put((dist[neighbour], count, neighbour))
                    openSetHash.add(neighbour)
                    neighbour.setEDGE(VisualiseAlgorithm)
                
        if current != start:
            current.setCLOSED(VisualiseAlgorithm)
    # DrawFunc()
    
    return False

def WallFollower(DrawFunc, grid, start, goal, VisualiseAlgorithm, AnimatePath):
    pass




