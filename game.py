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

        game_map = [
            [1,1,1,1,1,1,1],
            [1,0,0,0,1,0,1],
            [1,0,1,0,1,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,0,1]
        ]
    
        for row, row_of_nums in enumerate(game_map):
            for column, true_false in enumerate(row_of_nums):
                if true_false == 1:
                    colour = 'white'
                
                if true_false == 0:
                    colour = 'black'

                x0 = 40 * column
                y0 = 40 * row
                x1 = 40 + (40 * column)
                y1 = 40 + (40 * row)    
                cubes = self.wall.create_rectangle(x0, y0, x1, y1, fill=colour, outline=colour)
                

        self.player_x0, self.player_y0, self.player_x1, self.player_y1 = 60, 60, 70, 70
        self.player = self.wall.create_rectangle(self.player_x0, self.player_y0, self.player_x1, self.player_y1, fill='red')
    
        self.player_line_x0, self.player_line_y0, self.player_line_x1, self.player_line_y1 = 65, 65, 65, 30      
        self.player_line = self.wall.create_line(self.player_line_x0, self.player_line_y0, self.player_line_x1, self.player_line_y1, fill='green', arrow=tk.LAST)

        for key in 'wasd':
            self.bind(key, lambda event, k=key: self.player_movement(k))

    def player_movement(self, k):
        angle = 0.08

        movement_speed_modifier = 0.04

        if k == 'w':
            self.wall.move(self.player, self.new_x1 * movement_speed_modifier, self.new_y1 * movement_speed_modifier)
            self.wall.move(self.player_line, self.new_x1 * movement_speed_modifier, self.new_y1 * movement_speed_modifier)

            coords = self.wall.coords(self.player_line)
            self.player_line_x0, self.player_line_y0, self.player_line_x1, self.player_line_y1 = coords[0], coords[1], coords[2], coords[3]
           
        if k == 'a' or k == 'd':
            if k == 'a':
                angle = -angle

            dx = self.player_line_x1 - self.player_line_x0
            dy = self.player_line_y1 - self.player_line_y0
            self.new_x1 = dx * math.cos(angle) - dy * math.sin(angle) + self.player_line_x0
            self.new_y1 = dx * math.sin(angle) + dy * math.cos(angle) + self.player_line_y0
            self.player_line_x1 = self.new_x1
            self.player_line_y1 = self.new_y1
            
            self.wall.delete(self.player_line)
            self.player_line = self.wall.create_line(self.player_line_x0, self.player_line_y0, self.player_line_x1, self.player_line_y1, fill='green', arrow=tk.LAST)


window = Game()
window.mainloop()