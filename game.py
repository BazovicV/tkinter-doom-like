import tkinter as tk

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

                if row == 0 and column == 0:
                    self.start_x0, self.start_y0, self.finish_x1, self.finish_y1 = 10, 10, 50, 50
                    starting_wall = self.wall.create_rectangle(self.start_x0, self.start_y0, self.finish_x1, self.finish_y1, fill=colour)
                    starting_wall
                        
                else:   
                    if column == 0:
                        self.start_y0 += 40
                        self.finish_y1 += 40
                        self.start_x0 = 10
                        self.finish_x1 = 50
                        x0 = 0

                    else:
                        x0 = 40
                    
                    self.wall.create_rectangle(self.start_x0+x0, self.start_y0, self.finish_x1+x0, self.finish_y1, fill=colour)
                    self.start_x0, self.start_y0, self.finish_x1, self.finish_y1 = self.start_x0+x0, self.start_y0, self.finish_x1+x0, self.finish_y1

        self.player_x0, self.player_y0, self.player_x1, self.player_y1 = 60, 60, 70, 70
        self.player = self.wall.create_rectangle(self.player_x0, self.player_y0, self.player_x1, self.player_y1, fill='red')
        self.player

        for key in 'wasd':
            self.bind(key, lambda event, k=key: self.player_movement(k))

    def player_movement(self, k): # USE MOVE INSTEAD
        if k == 'w':
            self.player_x0 += 0
            self.player_y0 -= 2
            self.player_x1 += 0
            self.player_y1 -= 2
           
        if k == 'a':
            self.player_x0 -= 2
            self.player_y0 += 0
            self.player_x1 -= 2
            self.player_y1 += 0

        if k == 's':
            self.player_x0 += 0
            self.player_y0 += 2
            self.player_x1 += 0
            self.player_y1 += 2

        if k == 'd':
            self.player_x0 += 2
            self.player_y0 += 0
            self.player_x1 += 2
            self.player_y1 += 0 

        self.wall.delete(self.player)
        self.player = self.wall.create_rectangle(self.player_x0, self.player_y0, self.player_x1, self.player_y1, fill='red')   




window = Game()
window.mainloop()