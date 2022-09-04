import math
import pygame

maze = "maze1.png"

class buildEnvironment:
    def __init__(self, width, height, maze, color):
        self.mapw = width
        self.maph = height
        self.color = color
        pygame.init()
        self.pointCloud = []
        self.externalMap = pygame.image.load(maze)
        self.MapWindowName = "Map"
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph))
        self.map.blit(self.externalMap, (0, 0))
        
        self.black = (0, 0, 0)
        self.grey = (128, 128, 128)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
    
    def AD2pos(self, distance, angle, currentPos):
        x = int(currentPos[0] + distance * math.cos(angle))
        y = int(currentPos[1] + distance * math.sin(angle))
        return x, y
    
    def dataStore(self, data):
        # print(len(self.pointCloud))
        for element in data:
            point = self.AD2pos(element[0], element[1], element[2])
            if point not in self.pointCloud:
                self.pointCloud.append(point)
    
    def show_sensorData(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]), int(point[1])), self.red)
            