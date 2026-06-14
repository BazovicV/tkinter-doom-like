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

        self.wall_column = []
        self.wall_row = []
        self.empty_column = []
        self.empty_row = []

        game_map = [
            [1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1],
            [1,0,1,1,1,1,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1]
        ]
    
        for row, row_of_nums in enumerate(game_map):
            for column, true_false in enumerate(row_of_nums):
                if true_false == 1:
                    colour = 'white'
                    self.wall_row.append(row)
                    self.wall_column.append(column)
                
                if true_false == 0:
                    colour = 'black'
                    self.empty_column.append(row)
                    self.empty_row.append(column)

                x0 = 40 * column
                y0 = 40 * row
                x1 = 40 + (40 * column)
                y1 = 40 + (40 * row)    
                cubes = self.wall.create_rectangle(x0, y0, x1, y1, fill=colour, outline=colour)
                

        self.player_x0, self.player_y0, self.player_x1, self.player_y1 = 60, 60, 70, 70
        self.player = self.wall.create_rectangle(self.player_x0, self.player_y0, self.player_x1, self.player_y1, fill='red', outline='red')
    
        self.player_line_x0, self.player_line_y0, self.player_line_x1, self.player_line_y1 = 65, 65, 65, 30      
        self.player_line = self.wall.create_line(self.player_line_x0, self.player_line_y0, self.player_line_x1, self.player_line_y1, fill='green', arrow=tk.LAST)

        self.raycasting()

        for key in 'wasd':
            self.bind(key, lambda event, k=key: self.player_movement(k))

    def player_movement(self, k):
        angle = 0.1

        self.movement_speed_modifier = 0.1

        self.dx = self.player_line_x1 - self.player_line_x0
        self.dy = self.player_line_y1 - self.player_line_y0

        self.wall.delete('ray')
        self.raycasting()

        if k == 'w' or k == 's':
            if k == 's':
                    self.dx = -self.dx
                    self.dy = -self.dy

            if not self.player_collision():
                self.wall.move(self.player, self.dx * self.movement_speed_modifier, self.dy * self.movement_speed_modifier)
                self.wall.move(self.player_line, self.dx * self.movement_speed_modifier, self.dy * self.movement_speed_modifier)

                coords = self.wall.coords(self.player_line)
                self.player_line_x0, self.player_line_y0, self.player_line_x1, self.player_line_y1 = coords[0], coords[1], coords[2], coords[3]
            
            if self.player_collision():
                self.wall.move(self.player, -self.dx * self.movement_speed_modifier, -self.dy * self.movement_speed_modifier)
                self.wall.move(self.player_line, -self.dx * self.movement_speed_modifier, -self.dy * self.movement_speed_modifier)

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

        for wall_row, wall_column in zip(self.wall_row, self.wall_column): # zip() - Pairs by index nicely
            self.actual_x0 = int(self.player_x0 / 40)
            self.actual_y0 = int(self.player_y0 / 40)
            self.actual_x1 = int(self.player_x1 / 40)
            self.actual_y1 = int(self.player_y1 / 40)

            if (self.actual_x0, self.actual_y0) == (wall_column, wall_row) or (self.actual_x1, self.actual_y1) == (wall_column, wall_row) or (self.actual_x0, self.actual_y1) == (wall_column, wall_row) or (self.actual_x1, self.actual_y0) == (wall_column, wall_row):
                return True
            
    def raycasting(self):
        angle = -0.524 # -30 degrees

        for ray in range(60):
            dx = self.player_line_x1 - self.player_line_x0
            dy = self.player_line_y1 - self.player_line_y0

            new_ray_x1 = dx * math.cos(angle) - dy * math.sin(angle) + self.player_line_x0
            new_ray_y1 = dx * math.sin(angle) + dy * math.cos(angle) + self.player_line_y0
            ray_x1 = new_ray_x1
            ray_y1 = new_ray_y1

            current_ray_angle = math.atan2(new_ray_y1-self.player_line_y0, new_ray_x1-self.player_line_x0) + angle

            x_step = math.cos(current_ray_angle) * 2 # 2 pixels per step
            y_step = math.sin(current_ray_angle) * 2

            while True:
                ray_x1 += x_step
                ray_y1 += y_step

                actual_ray_x1 = int(ray_x1 / 40)
                actual_ray_y1 = int(ray_y1 / 40)

                for wall_row, wall_column in zip(self.wall_row, self.wall_column):
                    if (actual_ray_x1, actual_ray_y1) == (wall_column, wall_row):

                        self.wall.create_line(self.player_line_x0, self.player_line_y0, ray_x1, ray_y1, fill='blue', tags='ray')
                        
                break        
                
            angle += 0.0175 # +1 degree
            
            

window = Game()
window.mainloop()