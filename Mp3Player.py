from tkinter import filedialog
import playsound
file = filedialog.askopenfilename()
playsound.playsound(file)