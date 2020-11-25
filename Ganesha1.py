from tkinter import Tk, Canvas, Frame, BOTH, Label
import random
class Ganesha(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("!!..Output..!!")
        self.pack(fill=BOTH, expand=1)
        colors = ['#f11','#f1f','#11f','#1f1','#f11','#f1f','#11f','#1f1','#f11','#f1f','#11f','#1f1']
        color = random.randrange(0, 11)

        canvas = Canvas(self) #atul
        canvas.create_polygon([ 320, 40, 280, 64, 370, 64 ], fill=colors[color], width=2)
        canvas.create_polygon([ 270, 68, 270, 75, 380, 75, 380, 68 ], fill=colors[color], width=2)
        canvas.create_polygon([ 260, 78, 260, 85, 390, 85, 390, 78 ], fill=colors[color], width=2)
        canvas.create_polygon([ 250, 88, 250, 95, 400, 95, 400, 88 ], fill=colors[color], width=4)
        canvas.create_polygon([ 240, 98, 240, 105, 410, 105, 410, 98 ], fill=colors[color], width=4)
        canvas.create_polygon([ 320, 120, 310, 140, 320, 160, 330, 140 ], outline=colors[color], fill=colors[color], width=2)

        canvas.create_arc(300, 140, 170, 200, start=0, extent=120, outline=colors[color], style="arc", width=6)            
        canvas.create_arc(340, 140, 480, 200 , start=60, extent=120, outline=colors[color], style="arc", width=6)

        canvas.create_arc(450, 280, 300,60, start=180, extent=60, outline=colors[color], style="arc", width=6)  
        canvas.create_arc(500, 280, 340,60, start=180, extent=60, outline=colors[color], style="arc", width=6)  
        canvas.create_arc(310, 260, 350, 370, start=80, extent=-110, outline=colors[color], style="arc", width=6)
        canvas.create_arc(330, 250, 390, 360, start=50, extent=-140, outline=colors[color], style="arc", width=6)           
        
        canvas.create_oval(220, 170, 270, 190, outline=colors[color],  width=4)
        canvas.create_oval(370, 170, 420, 190, outline=colors[color], width=4)
        canvas.create_oval(240, 170, 250, 190, outline=colors[color], fill=colors[color], width=6)
        canvas.create_oval(390, 170, 400, 190, outline=colors[color], fill=colors[color], width=6)
        Label(self,text="Run Program Once Again.",font="Arial").place(x=460,y=420)
        canvas.pack(fill=BOTH, expand=1)
            
if __name__ == '__main__':
    root = Tk()
    ex = Ganesha()
    root.geometry("700x450")
    root.mainloop()