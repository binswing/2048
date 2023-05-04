import func
from tkinter import *
from tkinter import font
from tkinter import messagebox
import threading
from pynput import keyboard
import time

class Window:
    def __init__(self):
        self.prop = func.func()
        self.frame = Tk()
        self.frame.title('wordle')
        self.frame.geometry("1000x1000")
        self.frame.resizable(False, False)
        self.frame.configure(bg="light grey")
        self.display = Canvas(self.frame, width=800, height = 800, bg = "light grey",highlightthickness=0)
        self.score = Label(self.frame,text="score : "+str(self.prop.score),font=font.Font(size=40))
        self.score.place(x=100, y=40)
        with open("best_score.txt","r") as f:
            best_score = f.readline() 
        self.bestscore = Label(self.frame,text="best score : "+str(best_score),font=font.Font(size=40))
        self.bestscore.place(x=500, y=40)
        self.display.grid(padx = 100, pady=150)
        self.nightmode = False
        self.kb = True
        self.t1 = threading.Thread(target= self.kb_inp_ctrl)
        self.t1.daemon = True
        self.t1.start()

        #box
        self.A1_box = self.display.create_rectangle(200,0,0,200,width=1,outline="black",fill = "white")
        self.A2_box = self.display.create_rectangle(400,0,200,200,width=1,outline="black",fill = "white")
        self.A3_box = self.display.create_rectangle(600,0,400,200,width=1,outline="black",fill = "white")
        self.A4_box = self.display.create_rectangle(799,0,600,200,width=1,outline="black",fill = "white")
        self.B1_box = self.display.create_rectangle(200,200,0,400,width=1,outline="black",fill = "white")
        self.B2_box = self.display.create_rectangle(400,200,200,400,width=1,outline="black",fill = "white")
        self.B3_box = self.display.create_rectangle(600,200,400,400,width=1,outline="black",fill = "white")
        self.B4_box = self.display.create_rectangle(799,200,600,400,width=1,outline="black",fill = "white")
        self.C1_box = self.display.create_rectangle(200,400,0,600,width=1,outline="black",fill = "white")
        self.C2_box = self.display.create_rectangle(400,400,200,600,width=1,outline="black",fill = "white")
        self.C3_box = self.display.create_rectangle(600,400,400,600,width=1,outline="black",fill = "white")
        self.C4_box = self.display.create_rectangle(799,400,600,600,width=1,outline="black",fill = "white")
        self.D1_box = self.display.create_rectangle(200,600,0,799,width=1,outline="black",fill = "white")
        self.D2_box = self.display.create_rectangle(400,600,200,799,width=1,outline="black",fill = "white")
        self.D3_box = self.display.create_rectangle(600,600,400,799,width=1,outline="black",fill = "white")
        self.D4_box = self.display.create_rectangle(799,600,600,799,width=1,outline="black",fill = "white")

        self.A_arr = [self.A1_box,self.A2_box,self.A3_box,self.A4_box]
        self.B_arr = [self.B1_box,self.B2_box,self.B3_box,self.B4_box]
        self.C_arr = [self.C1_box,self.C2_box,self.C3_box,self.C4_box]
        self.D_arr = [self.D1_box,self.D2_box,self.D3_box,self.D4_box]
        self.box_arr = [self.A_arr,self.B_arr,self.C_arr,self.D_arr]

        self.a1 =self.display.create_text(102,102,fill="black", font="Helvetica 50", text="")
        self.a2 =self.display.create_text(302,102,fill="black", font="Helvetica 50", text="")
        self.a3 =self.display.create_text(502,102,fill="black", font="Helvetica 50", text="")
        self.a4 =self.display.create_text(702,102,fill="black", font="Helvetica 50", text="")
        self.b1 =self.display.create_text(102,302,fill="black", font="Helvetica 50", text="")
        self.b2 =self.display.create_text(302,302,fill="black", font="Helvetica 50", text="")
        self.b3 =self.display.create_text(502,302,fill="black", font="Helvetica 50", text="")
        self.b4 =self.display.create_text(702,302,fill="black", font="Helvetica 50", text="")
        self.c1 =self.display.create_text(102,502,fill="black", font="Helvetica 50", text="")
        self.c2 =self.display.create_text(302,502,fill="black", font="Helvetica 50", text="")
        self.c3 =self.display.create_text(502,502,fill="black", font="Helvetica 50", text="")
        self.c4 =self.display.create_text(702,502,fill="black", font="Helvetica 50", text="")
        self.d1 =self.display.create_text(102,702,fill="black", font="Helvetica 50", text="")
        self.d2 =self.display.create_text(302,702,fill="black", font="Helvetica 50", text="")
        self.d3 =self.display.create_text(502,702,fill="black", font="Helvetica 50", text="")
        self.d4 =self.display.create_text(702,702,fill="black", font="Helvetica 50", text="")

        self.a_arr = [self.a1,self.a2,self.a3,self.a4]
        self.b_arr = [self.b1,self.b2,self.b3,self.b4]
        self.c_arr = [self.c1,self.c2,self.c3,self.c4]
        self.d_arr = [self.d1,self.d2,self.d3,self.d4]
        self.letter_arr = [self.a_arr,self.b_arr,self.c_arr,self.d_arr]

        self.update()

        self.frame.mainloop()
    
    def update(self):
        self.score.config(text = "score : "+str(self.prop.score))
        for i in range(4):
            for j in range(4):
                if i==self.prop.random_add[0] and j == self.prop.random_add[1]:
                    self.display.itemconfig(self.letter_arr[i][j],text = "")
                    self.display.itemconfig(self.box_arr[i][j],fill = "white")
                else:
                    num = self.prop.cont[i][j]
                    if num == 0:
                        self.display.itemconfig(self.letter_arr[i][j],text = "")
                        self.display.itemconfig(self.box_arr[i][j],fill = "white")
                    else:
                        self.display.itemconfig(self.letter_arr[i][j],text = str(num))
                        if num == 2: self.display.itemconfig(self.box_arr[i][j],fill = "yellow")
                        elif num == 4: self.display.itemconfig(self.box_arr[i][j],fill = "green")
                        elif num == 8: self.display.itemconfig(self.box_arr[i][j],fill = "lime")
                        elif num == 16: self.display.itemconfig(self.box_arr[i][j],fill = "light yellow")
                        elif num == 32: self.display.itemconfig(self.box_arr[i][j],fill = "light green")
                        elif num == 64: self.display.itemconfig(self.box_arr[i][j],fill = "dark green")
                        elif num == 128: self.display.itemconfig(self.box_arr[i][j],fill = "yellow")
                        elif num == 256: self.display.itemconfig(self.box_arr[i][j],fill = "green")
                        elif num == 512: self.display.itemconfig(self.box_arr[i][j],fill = "lime")
                        elif num == 1024: self.display.itemconfig(self.box_arr[i][j],fill = "light yellow")
                        elif num == 2048: self.display.itemconfig(self.box_arr[i][j],fill = "light green")
                        elif num == 4096: self.display.itemconfig(self.box_arr[i][j],fill = "dark green")                        
                      
                      
                      
                        elif num == 16384: self.display.itemconfig(self.box_arr[i][j],fill = "yellow")
                        elif num == 32768: self.display.itemconfig(self.box_arr[i][j],fill = "green")
                        elif num == 65536: self.display.itemconfig(self.box_arr[i][j],fill = "lime")
                        elif num == 131072: self.display.itemconfig(self.box_arr[i][j],fill = "light yellow")
                        elif num == 262144: self.display.itemconfig(self.box_arr[i][j],fill = "light green")
                        elif num == 524288: self.display.itemconfig(self.box_arr[i][j],fill = "dark green")
        time.sleep(0.1)
        self.display.itemconfig(self.letter_arr[self.prop.random_add[0]][self.prop.random_add[1]],text = str(self.prop.cont[self.prop.random_add[0]][self.prop.random_add[1]]))
        if self.prop.cont[self.prop.random_add[0]][self.prop.random_add[1]] == 2: 
            self.display.itemconfig(self.box_arr[self.prop.random_add[0]][self.prop.random_add[1]],fill = "yellow")
        elif self.prop.cont[self.prop.random_add[0]][self.prop.random_add[1]] == 4: 
            self.display.itemconfig(self.box_arr[self.prop.random_add[0]][self.prop.random_add[1]],fill = "green")

                    
    def lose(self):
        messagebox.showinfo("warning","You lose. Your score is " + str(self.prop.score))
        with open("best_score.txt","r") as f:
            best_score = f.readline()
        if self.prop.score > int(best_score):
            with open("best_score.txt","w") as f:
                f.write(str(self.prop.score))          
        self.frame.destroy()
        exit()        
    def up(self):
        check_lose,change = self.prop.up()
        if change: self.update()
        if check_lose == "lose": self.lose()
        self.kb = True
    def down(self):
        check_lose,change = self.prop.down()
        if change: self.update()
        if check_lose == "lose": self.lose()
        self.kb = True
    def left(self):
        check_lose,change = self.prop.left()
        if change: self.update()
        if check_lose == "lose": self.lose()
        self.kb = True
    def right(self):
        check_lose,change = self.prop.right()
        if change: self.update()
        if check_lose == "lose": self.lose()
        self.kb = True
    #phys keyboard input
    def on_release(self,key):
        self.kb = False
        if key == keyboard.Key.up or key == keyboard.KeyCode.from_char("w"): self.up()
        elif key == keyboard.Key.down or key == keyboard.KeyCode.from_char("s"): self.down()
        elif key == keyboard.Key.left or key == keyboard.KeyCode.from_char("a"): self.left()
        elif key == keyboard.Key.right or key == keyboard.KeyCode.from_char("d"): self.right()

    def kb_inp_ctrl(self):
        if self.kb:
            with keyboard.Listener(on_release= self.on_release) as listener:
                listener.join()


Window()