import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk


def openfile():
    '''
    root = tk.Tk()
    root.geometry("400x350")
    btn = tk.Button(text='파일열기', command = openfile)
    imageLabel = tk.Label()
    btn.pack()
    imageLabel.pack()
    tk.mainloop()
    '''
    fpath = fd.askopenfilename()
    return fpath





