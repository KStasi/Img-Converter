from tkinter import *
from PIL import Image, ImageTk, ImageFilter
from tkinter import filedialog as fd
from tkmacosx import Button as MacButton


class Program:
    def __init__(self):
        self.root = Tk()
        self.root.title('PCX-BMP Converter')
        self.root.geometry('450x480')
        self.root.config(bg='#F2E0C9')

        self.pic = None
        self.width = IntVar()
        self.height = IntVar()

        self.frame = Frame(self.root, bg='#F2E0C9')

        self.go_main()
        self.root.mainloop()

    def read_pcx_file(self):
        file_path = fd.askopenfilename()
        self.pic = Image.open(file_path)

    def save_bmp_file(self):
        export_file_path = fd.asksaveasfilename(defaultextension='.bmp', filetypes=[('Image (.bmp file)', '.bmp')])

        width = self.width.get()
        height = self.height.get()
        newsize = (width, height)
        resized_pic = self.pic.resize(newsize)

        resized_pic.save(export_file_path)

    def save_modified_pcx(self):
        export_file_path = fd.asksaveasfilename(defaultextension='.pcx', filetypes=[('Image (.pcx file)', '.pcx')])
        self.pic = self.pic.convert('RGB')
        edge_enhance = self.pic.filter(ImageFilter.EDGE_ENHANCE)
        edge_enhance.save(export_file_path)

    def save_modified_bmp(self):
        export_file_path = fd.asksaveasfilename(defaultextension='.bmp', filetypes=[('Image (.bpm file)', '.bmp')])
        self.pic = self.pic.convert('RGB')
        edge_enhance = self.pic.filter(ImageFilter.EDGE_ENHANCE)
        edge_enhance.save(export_file_path)

    def read_bmp_file(self):
        file_location = fd.askopenfilename()
        self.pic = Image.open(file_location)

    def save_pcx_file(self):
        export_file_location = fd.asksaveasfilename(defaultextension='.pcx', filetypes=[('Image (.pcx file)', '.pcx')])
        width = self.width.get()
        height = self.height.get()
        newsize = (width, height)
        resized_pic = self.pic.resize(newsize)
        resized_pic.save(export_file_location)

    def save_bmp_file(self):
        export_file_path = fd.asksaveasfilename(defaultextension='.bmp', filetypes=[('Image (.bmp file)', '.bmp')])
        self.pic = self.pic.convert('RGB')
        edge_enhance = self.pic.filter(ImageFilter.EDGE_ENHANCE)
        edge_enhance.save(export_file_path)

    def clean(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def put_int_entry(self,entry_obj):
        entry_style = { 'highlightbackground':'#2B678C', 'bg':'#F2E0C9', 'fg':'#2B678C', 'font': ('helvetica', 11, 'bold') }
        entry = Entry(self.frame, textvariable=entry_obj, **entry_style)
        entry.pack(pady=10)

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

        self.put_label('PCX-BMP Converter')

        self.put_button("PCX to BMP", self.go_to_bmp, style='secondary')
        self.put_button("BMP to PCX", self.go_to_pcx, style='secondary')

        self.frame.pack(pady=20)


    def go_to_bmp(self):
        self.clean()

        self.put_button("Import PCX File", self.read_pcx_file)

        self.put_int_entry(self.width)
        self.put_int_entry(self.height)

        self.put_button("Convert PCX to BMP", self.save_bmp_file)
        self.put_button("PCX with filter edge enhence", self.save_modified_pcx)

        self.put_button("Back", self.go_main, style='secondary')
        self.put_button("Close", self.root.destroy, style='secondary')


    def go_to_pcx(self):
        self.clean()

        self.put_button("Import BMP File", self.read_bmp_file)

        self.put_int_entry(self.width)
        self.put_int_entry(self.height)

        self.put_button("Convert BMP to PCX", self.save_pcx_file)
        self.put_button("BMP with filter edge enhence", self.save_modified_bmp)

        self.put_button("Back", self.go_main, style='secondary')
        self.put_button("Close", self.root.destroy, style='secondary')

Program()