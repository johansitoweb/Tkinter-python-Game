import tkinter as tk  
import random  

class Arkanoid:  
    def __init__(self, master):  
        self.master = master  
        self.master.title("Arkanoid")  
        
        self.canvas = tk.Canvas(master, width=400, height=300, bg="black")  
        self.canvas.pack()  

        self.paddle = self.canvas.create_rectangle(150, 280, 250, 290, fill="blue")  
        self.ball = self.canvas.create_oval(195, 250, 205, 260, fill="red")  
        
        self.ball_dx = 2  # velocidad en x  
        self.ball_dy = -2  # velocidad en y  
        
        # Crear bloques  
        self.blocks = []  
        self.create_blocks()  
        
        self.master.bind("<Left>", self.move_paddle_left)  
        self.master.bind("<Right>", self.move_paddle_right)  
        
        self.update_game()  

    def create_blocks(self):  
        for i in range(5):  
            for j in range(7):  
                x1 = j * 50 + 10  
                y1 = i * 20 + 30  
                x2 = x1 + 40  
                y2 = y1 + 15  
                block = self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")  
                self.blocks.append(block)  

    def move_paddle_left(self, event):  
        self.canvas.move(self.paddle, -20, 0)  

    def move_paddle_right(self, event):  
        self.canvas.move(self.paddle, 20, 0)  
    
    def update_game(self):  
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)  
        ball_pos = self.canvas.coords(self.ball)  

        # Comprobar colisiones con las paredes  
        if ball_pos[0] <= 0 or ball_pos[2] >= 400:  
            self.ball_dx = -self.ball_dx  # Rebote horizontal  
        if ball_pos[1] <= 0:  
            self.ball_dy = -self.ball_dy  # Rebote vertical  
        
        # Comprobar colisiones con la paleta  
        paddle_pos = self.canvas.coords(self.paddle)  
        if ball_pos[3] >= paddle_pos[1] and paddle_pos[0] <= ball_pos[0] <= paddle_pos[2]:  
            self.ball_dy = -self.ball_dy  

        # Comprobar colisiones con los bloques  
        for block in self.blocks:  
            block_pos = self.canvas.coords(block)  
            if (ball_pos[2] >= block_pos[0] and ball_pos[0] <= block_pos[2] and   
                    ball_pos[3] >= block_pos[1] and ball_pos[1] <= block_pos[3]):  
                self.canvas.delete(block)  
                self.blocks.remove(block)  
                self.ball_dy = -self.ball_dy  
                break  

        # Comprueba si la bola ha caído  
        if ball_pos[3] >= 300:  
            self.canvas.create_text(200, 150, text="¡Game Over!", fill="white", font=("Helvetica", 24))  
            return  

        # Actualiza el juego cada 20 ms  
        self.master.after(20, self.update_game)  


# Ejecutar el juego  
root = tk.Tk()  
game = Arkanoid(root)  
root.mainloop()  