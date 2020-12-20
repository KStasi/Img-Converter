from tkinter import *
from PIL import Image, ImageTk, ImageFilter
from tkinter import filedialog as fd, ttk
from tkmacosx import Button as MacButton
import cv2
import numpy as np

class Program:
    def __init__(self):
        self.root = Tk()
        self.root.title('PNG-BMP Converter')
        self.root.geometry('450x480')
        self.root.config(bg='#F2E0C9')

        self.pic = None
        self.combosize = None
        self.width = IntVar()
        self.height = IntVar()

        self.frame = Frame(self.root, bg='#F2E0C9')

        self.go_main()
        self.root.mainloop()

    def read_file(self):
        file_path = fd.askopenfilename()
        self.pic = cv2.imread(file_path)

    def save_file(self, ext):
        export_file_path = fd.asksaveasfilename(defaultextension=ext, filetypes=[(f'Image ({ext} file)', ext)])
        scale_percent = float(self.combosize.get())
        width = int(self.pic.shape[1] * scale_percent)
        height = int(self.pic.shape[0] * scale_percent)
        newsize = (width, height)
        resized_pic = cv2.resize(self.pic, newsize)
        cv2.imwrite(export_file_path, resized_pic)

    def save_png_file(self):
        self.save_file('.png')

    def save_bmp_file(self):
        self.save_file('.bmp')

    def save_modified(self, ext):
        export_file_path = fd.asksaveasfilename(defaultextension=ext, filetypes=[(f'Image ({ext} file)', ext)])
        width = int(self.pic.shape[1])
        height = int(self.pic.shape[0])
        size = (width, height)
        matrix = cv2.getRotationMatrix2D(((height-1)/2.0,(width-1)/2.0),90,1)
        rotation = cv2.warpAffine(self.pic, matrix, size)
        matrix = np.float32([[1,0,100],[0,1,50]])
        slide = cv2.warpAffine(rotation, matrix, size)
        cv2.imwrite(export_file_path, slide)

    def save_modified_png(self):
        self.save_modified('.png')

    def save_modified_bmp(self):
        self.save_modified('.bmp')

    def clean(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def put_int_entry(self,entry_obj):
        entry_style = { 'highlightbackground':'#2B678C', 'bg':'#F2E0C9', 'fg':'#2B678C', 'font': ('helvetica', 11, 'bold') }
        entry = Entry(self.frame, textvariable=entry_obj, **entry_style)
        entry.pack(pady=10)

    def put_combox(self):
        self.combosize = ttk.Combobox(self.frame,
                         values=[
                             "0.5",
                             "1",
                             "1.5",
                             "2",
                             "2.5",
                             "3",
                             "3.5",
                             "4"])
        self.combosize.pack(pady=30)
        self.combosize.current(1)

    def put_button(self, text, command, style='main'):
        button_styles = {
            'main':{ 'highlightbackground':'#2B678C', 'bg':'#F2E0C9', 'fg':'#2B678C', 'font': ('helvetica', 15, 'bold') },
            'secondary': { 'bg':'#2B678C', 'fg': '#F2E0C9', 'font': '11' }
        }
        pack_styles = {
            'main':{ 'pady': 20 },
            'secondary': { 'padx':40, 'pady': 10  }
        }
        button = MacButton(self.frame, text=text, command=command, **button_styles[style])
        button.pack(**pack_styles[style])

    def put_label(self, text, style='main'): 
        label_styles = { 
            'main':{ 'text':text, 'padx':5, 'pady':5, 'bg':'#F2E0C9', 'fg':'#2B678C', 'font': 'Lucida 20 bold' }, 
            'secondary': { 'textvariable': text, 'textvariable' : StringVar(), 'bg':'#2B678C', 'fg': '#F2E0C9', 'font': '11' } 
        } 
        pack_styles = { 
            'main':{ 'pady': 20 }, 
            'secondary': { 'padx':40, 'pady': 10  } 
        } 
        label = Label(self.frame, **label_styles[style]) 
        label.pack(**pack_styles[style]) 

    def go_main(self):
        self.clean()

        self.put_label('PNG-BMP Converter')

        self.put_button("PNG to BMP", self.go_to_bmp, style='secondary')
        self.put_button("BMP to PNG", self.go_to_png, style='secondary')

        self.frame.pack(pady=20)


    def go_to_bmp(self):
        self.clean()

        self.put_button("Import PNG File", self.read_file)

        self.put_label('new size (percent of size)', style="secondary")

        self.put_combox()

        self.put_button("Convert PNG to BMP", self.save_bmp_file)
        self.put_button("PNG with rotation and slipage", self.save_modified_png)

        self.put_button("Back", self.go_main, style='secondary')
        self.put_button("Close", self.root.destroy, style='secondary')


    def go_to_png(self):
        self.clean()

        self.put_button("Import BMP File", self.read_file)

        self.put_label('new size (percent of size)', style="secondary")

        self.put_combox()

        self.put_button("Convert BMP to PNG", self.save_png_file)
        self.put_button("BMP with rotation and slipage", self.save_modified_bmp)

        self.put_button("Back", self.go_main, style='secondary')
        self.put_button("Close", self.root.destroy, style='secondary')

Program()