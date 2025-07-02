# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-шоп

class Map:
    
    #def generate_rivers(): # Генератор рек
    #def generate_forest(): # Генератор леса

    def print_map(self):
        print("⬛" * (self.w + 2))
        for row in self.cells:
            print("⬛", end="")
            for cell in row:
                if cell == 0: # 0 - поле
                    print("🟨", end = "")
                elif cell == 1: # 1 - дерево
                    print("🌲", end = "")
                elif cell == 2: # 2 - река
                    print("🌊", end = "")
                elif cell == 3: # 3 - госпиталь
                    print("🏥", end = "")
                elif cell == 4: # 4 - апгрейд-шоп
                    print("🏦", end = "")
            print("⬛")
        print("⬛" * (self.w + 2))
            
    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]