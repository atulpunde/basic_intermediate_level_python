from tkinter import Tk, Canvas, Frame, BOTH, Label
import random
import winsound

class Ganesha(Frame):
    def __init__(self,root, color):
        super().__init__()
        self.initUI(root, color)

    def initUI(self,root, color):
        root.title("!!..Ganpati Bappa..!!")
        self.pack(fill=BOTH, expand=1)
        
        canvas = Canvas(root) #atul
        canvas.create_polygon([ 320, 40, 280, 64, 370, 64 ], fill=color, width=2)
        canvas.create_polygon([ 270, 68, 270, 75, 380, 75, 380, 68 ], fill=color, width=2)
        canvas.create_polygon([ 260, 78, 260, 85, 390, 85, 390, 78 ], fill=color, width=2)
        canvas.create_polygon([ 250, 88, 250, 95, 400, 95, 400, 88 ], fill=color, width=4)
        canvas.create_polygon([ 240, 98, 240, 105, 410, 105, 410, 98 ], fill=color, width=4)
        canvas.create_polygon([ 320, 120, 310, 140, 320, 160, 330, 140 ], outline=color, fill=color, width=2)

        canvas.create_arc(300, 140, 170, 200, start=0, extent=120, outline=color, style="arc", width=6)            
        canvas.create_arc(340, 140, 480, 200 , start=60, extent=120, outline=color, style="arc", width=6)
        canvas.create_arc(450, 280, 300,60, start=180, extent=60, outline=color, style="arc", width=6)  
        canvas.create_arc(500, 280, 340,60, start=180, extent=60, outline=color, style="arc", width=6)  
        canvas.create_arc(310, 260, 350, 370, start=80, extent=-110, outline=color, style="arc", width=6)
        canvas.create_arc(330, 250, 390, 360, start=50, extent=-140, outline=color, style="arc", width=6)           
        
        canvas.create_oval(220, 170, 270, 190, outline=color,  width=4)
        canvas.create_oval(370, 170, 420, 190, outline=color, width=4)
        canvas.create_oval(240, 170, 250, 190, outline=color, fill=color, width=6)
        canvas.create_oval(390, 170, 400, 190, outline=color, fill=color, width=6)
        Label(root,text="atulpunde970@gmail.com",font=("verdana",8)).place(x=540,y=10)
        Label(root,text="Run Program Once Again to change color.",font="Arial").place(x=160,y=560)
        Label(root,text="M.Sc. IMCA,(Batch:2018-21) Fergusson College, Pune",font=("Arial",12)).place(x=150,y=600)
        canvas.pack(fill=BOTH, expand=1)
        winsound.Beep(3000, 500)

#atulpunde970@gmail.com            
if __name__ == '__main__':
    colors = ['blue4','red3','dark green']
    for color in colors:
        root = Tk()
        ex = Ganesha(root,color)
        root.geometry("700x640")
        root.mainloop()   
