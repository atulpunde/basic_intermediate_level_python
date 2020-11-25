from tkinter import *
import tkSnack

root = Tk()
tkSnack.initializeSnack(root)

snd = tkSnack.Sound()
snd.read('D://Home//Movie//Music//BOLE CHUDIYAN - KABHI KHUSHI KABHI GHAM.mp3')
snd.play(blocking=1)