import tkinter as tk
import math

class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('400x400')
        self.title('Game')
        self.resizable(True, True)

        self.wall = tk.Canvas(self, width=4000, height=4000, bg='black')
        self.wall.pack()

        self.game_map = [
            [1,1,1,1,1,1,1],
            [1,0,0,0,1,0,1],
            [1,0,1,0,1,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,0,1]
        ]
    
        for row, row_of_nums in enumerate(self.game_map):
            for column, true_false in enumerate(row_of_nums):
                if true_false == 1:
                    colour = 'white'
                    self.wall_row = [row]
                    self.wall_column = [column]
                
                if true_false == 0:
                    colour = 'black'

                x0 = 40 * column
                y0 = 40 * row
                x1 = 40 + (40 * column)
                y1 = 40 + (40 * row)    
                cubes = self.wall.create_rectangle(x0, y0, x1, y1, fill=colour, outline=colour)
                

        self.player_x0, self.player_y0, self.player_x1, self.player_y1 = 60, 60, 70, 70
        self.player = self.wall.create_rectangle(self.player_x0, self.player_y0, self.player_x1, self.player_y1, fill='red', outline='red')
    
        self.player_line_x0, self.player_line_y0, self.player_line_x1, self.player_line_y1 = 65, 65, 65, 30      
        self.player_line = self.wall.create_line(self.player_line_x0, self.player_line_y0, self.player_line_x1, self.player_line_y1, fill='green', arrow=tk.LAST)

        for key in 'wasd':
            self.bind(key, lambda event, k=key: self.player_movement(k))

    def player_movement(self, k):
        angle = 0.1

        movement_speed_modifier = 0.1

        self.dx = self.player_line_x1 - self.player_line_x0
        self.dy = self.player_line_y1 - self.player_line_y0

        if k == 'w' or k == 's':
            if not self.player_collision():
                pass

                if k == 's':
                    self.dx = -self.dx
                    self.dy = -self.dy

                self.wall.move(self.player, self.dx * movement_speed_modifier, self.dy * movement_speed_modifier)
                self.wall.move(self.player_line, self.dx * movement_speed_modifier, self.dy * movement_speed_modifier)

                coords = self.wall.coords(self.player_line)
                self.player_line_x0, self.player_line_y0, self.player_line_x1, self.player_line_y1 = coords[0], coords[1], coords[2], coords[3]
           
        if k == 'a' or k == 'd':
            if k == 'a':
                angle = -angle

            self.new_x1 = self.dx * math.cos(angle) - self.dy * math.sin(angle) + self.player_line_x0
            self.new_y1 = self.dx * math.sin(angle) + self.dy * math.cos(angle) + self.player_line_y0
            self.player_line_x1 = self.new_x1
            self.player_line_y1 = self.new_y1
            
            self.wall.delete(self.player_line)
            self.player_line = self.wall.create_line(self.player_line_x0, self.player_line_y0, self.player_line_x1, self.player_line_y1, fill='green', arrow=tk.LAST)

    def player_collision(self):
        coords = self.wall.coords(self.player)
        self.player_x0, self.player_y0, self.player_x1, self.player_y1 = coords[0], coords[1], coords[2], coords[3]
        actual_x0 = int(self.player_x0 / 40)
        actual_y0 = int(self.player_y0 / 40)
        actual_x1 = int(self.player_x1 / 40)
        actual_y1 = int(self.player_y1 / 40)

        if self.game_map[actual_y0][actual_x0] == 1 or self.game_map[actual_y1][actual_x1] == 1:
            return True
        else:
            return False

window = Game()
window.mainloop()