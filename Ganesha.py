from tkinter import *            #Tk, Canvas, Frame, BOTH
import time
import random

class Ganesha(Frame):
    def __init__(self):
        super().__init__()    
        self.initUI()

    def initUI(self):
        root = Tk()
        root.geometry("700x450")
        
        self.master.title("!!..Shree Ganesha..!!")
        self.pack(fill=BOTH, expand=1)
        color = ['#f11','#1f1','#11f','#f11','#1f1','#11f','#f11','#1f1','#11f']
        i = random.choice([0, 1, 2,3,4,5,6,7,8])
        print(i)
        canvas = Canvas(self)
        canvas.create_polygon([ 320, 40, 280, 64, 370, 64 ], fill=color[i], width=2)
        canvas.create_polygon([ 270, 68, 270, 75, 380, 75, 380, 68 ], fill='#111', width=2)
        canvas.create_polygon([ 260, 78, 260, 85, 390, 85, 390, 78 ], fill='#111', width=2)
        canvas.create_polygon([ 250, 88, 250, 95, 400, 95, 400, 88 ], fill='#111', width=4)
        canvas.create_polygon([ 240, 98, 240, 105, 410, 105, 410, 98 ], fill='#111', width=4)
        canvas.create_polygon([ 320, 120, 310, 140, 320, 160, 330, 140 ], outline='#111', fill='#111', width=2)

        arc = canvas.create_arc(300, 140, 170, 200, start=0, extent=120, style="arc", width=6)            
        arc = canvas.create_arc(340, 140, 480, 200 , start=60, extent=120, style="arc", width=6)
        arc = canvas.create_arc(450, 280, 300,60, start=180, extent=60, style="arc", width=6)  
        arc = canvas.create_arc(500, 280, 340,60, start=180, extent=60, style="arc", width=6)  
        arc = canvas.create_arc(310, 260, 350, 370, start=80, extent=-110, style="arc", width=6)
        arc = canvas.create_arc(330, 250, 390, 360, start=50, extent=-140, style="arc", width=6)           
        
        canvas.create_oval(220, 170, 270, 190,  width=4)
        canvas.create_oval(370, 170, 420, 190,  width=4)
        canvas.create_oval(240, 170, 250, 190, outline="#111", fill="#111", width=6)
        canvas.create_oval(390, 170, 400, 190, outline="#111", fill="#111", width=6)
        b3 = Button(root, text = "Change Color",command = '__init__',pady = 10).pack(side = BOTTOM)
        canvas.pack(fill=BOTH, expand=1)
        root.mainloop()
            
if __name__ == '__main__':
    ex = Ganesha()

    