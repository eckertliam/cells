from dataclasses import dataclass
import random
from pygame import PixelArray
import numpy as np

@dataclass
class World:
    cells: np.ndarray
    age: int = 0
    
    def __str__(self) -> str:
        world = ''
        for row in self.cells:
            for cell in row:
                if cell:
                    world += '█'
                else:
                    world += ' '
            world += '\n'
        return world
    
    
    def render(self, px_arr: PixelArray) -> None:
        for y in range(self.cells.shape[0]):
            for x in range(self.cells.shape[1]):
                cell = self.cells[y, x]
                if cell:
                    px_arr[x, y] = (255, 255, 255)
                else:
                    px_arr[x, y] = (0, 0, 0)
            
    
    def get_neighbors(self, x: int, y: int) -> int:
        x_min = max(x - 1, 0)
        x_max = min(x + 1, self.cells.shape[1] - 1)
        y_min = max(y - 1, 0)
        y_max = min(y + 1, self.cells.shape[0] - 1)
        
        neighbors = np.sum(self.cells[y_min:y_max+1, x_min:x_max+1]) - self.cells[y, x]
        return neighbors
    
    def update_cell(self, x: int, y: int, neighbors: int) -> int:
        cell = self.cells[y, x]
        
        if cell:
            if neighbors < 2 or neighbors > 3:
                # underpopulation and overpopulation
                return 0
            else:
                return 1
        else:
            if neighbors == 3:
                return 1
            else:
                return 0
            
    def update(self) -> None:
        neighbor_map = np.zeros_like(self.cells)
        
        for y in range(self.cells.shape[0]):
            for x in range(self.cells.shape[1]):
                neighbor_map[y, x] = self.get_neighbors(x, y)
        
        self.cells = np.vectorize(self.update_cell)(np.arange(self.cells.shape[0]), np.arange(self.cells.shape[1]), neighbor_map)
        self.age += 1
        
        
        

    

def random_world(width: int, height: int, density: float) -> World:
    cells = np.where(np.random.rand(height, width) < density, 1, 0)
    return World(cells)