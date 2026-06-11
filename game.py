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
                    if row == 0 and column == 0:
                        self.zero_x0, self.zero_y0, self.zero_x1, self.zero_y1 = 10, 10, 50, 50
                        starting_wall = self.wall.create_rectangle(self.zero_x0, self.zero_y0, self.zero_x1, self.zero_y1, fill='white')
                        starting_wall
                        
                    else:
                        try:
                            x0 = 40
                            zero_check = 10 / column

                        except ZeroDivisionError:
                            self.zero_y0 += 40
                            self.zero_y1 += 40
                            self.zero_x0 = 10
                            self.zero_x1 = 50
                            x0 = 0

                        finally:
                            self.wall.create_rectangle(self.zero_x0+x0, self.zero_y0, self.zero_x1+x0, self.zero_y1, fill='white')
                            self.zero_x0, self.zero_y0, self.zero_x1, self.zero_y1 = self.zero_x0+x0, self.zero_y0, self.zero_x1+x0, self.zero_y1

                if true_false == 0:
                    if row == 0 and column == 0:
                        self.zero_x0, self.zero_y0, self.zero_x1, self.zero_y1 = 10, 10, 50, 50
                        starting_wall = self.wall.create_rectangle(self.zero_x0, self.zero_y0, self.zero_x1, self.zero_y1, fill='blue')
                        starting_wall
                        
                    else:
                        try:
                            x0 = 40
                            zero_check = 10 / column

                        except ZeroDivisionError:
                            self.zero_y0 += 40
                            self.zero_y1 += 40
                            self.zero_x0 = 10
                            self.zero_x1 = 50
                            x0 = 0

                        finally:
                            self.wall.create_rectangle(self.zero_x0+x0, self.zero_y0, self.zero_x1+x0, self.zero_y1, fill='blue')
                            self.zero_x0, self.zero_y0, self.zero_x1, self.zero_y1 = self.zero_x0+x0, self.zero_y0, self.zero_x1+x0, self.zero_y1




window = Game()
window.mainloop()