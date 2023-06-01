from dataclasses import dataclass
import random
from pygame import PixelArray

@dataclass
class World:
    cells: list[list[bool]]
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
        width = len(self.cells[0])
        height = len(self.cells)
        
        
        for y in range(height):
            for x in range(width):
                cell = self.cells[y][x]
                if cell:
                    px_arr[x, y] = (255, 255, 255)
                else:
                    px_arr[x, y] = (0, 0, 0)
            
    
    def get_neighbors(self, x: int, y: int) -> int:
        # calc neighbors idx
        x_min = max(x - 1, 0)
        x_max = min(x + 1, len(self.cells[0]) - 1)
        y_min = max(y - 1, 0)
        y_max = min(y + 1, len(self.cells) - 1)
        
        neighbors = 0
        for j in range(y_min, y_max + 1):
            for i in range(x_min, x_max + 1):
                if i == x and j == y:
                    continue
                elif self.cells[j][i]:
                    neighbors += 1
        
        return neighbors
    
    def update_cell(self, x: int, y: int) -> bool:
        neighbors = self.get_neighbors(x, y)
        cell = self.cells[y][x]
        
        if cell:
            if neighbors < 2 or neighbors > 3:
                # underpopulation and overpopulation
                return False
            else:
                return True
        else:
            if neighbors == 3:
                return True
            else:
                return False
            
    def update(self) -> None:
        new_cells = []
        width = len(self.cells[0])
        height = len(self.cells)
        
        for y in range(height):
            row = []
            for x in range(width):
                row.append(self.update_cell(x, y))
            new_cells.append(row)
        
        self.cells = new_cells
        self.age += 1
            
        
        
        
        
        
        
    

def random_world(width: int, height: int) -> World:
    cells = []
    
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(random.choice([True, False]))
        cells.append(row)
        
    return World(cells)

