from psd_tools import PSDImage
import fitz  # PyMuPDF
from PIL import Image, ImageTk
import tkinter as tk

class PDFViewer:
    def __init__(self, path, page):
        self.path = path
        self.page = page

        self.open_pdf()
    
    def content(self):
        return "content"
    
    def rect(self):
        return "rect"
    
    def size(self):
        height = 540
        width = 360
        return height, width

    def open_pdf(self):
        doc = fitz.open(self.path)
        page = doc[self.page]
        """Display information about annotations on a PDF page."""
        width, height = page.rect.width, page.rect.height
        print(f"Page size: {width:.1f} x {height:.1f} points")
        for annot in page.annots():
            info = annot.info
            print(f"Type: {annot.type[1]}")
            print(f"Author: {info.get('title', 'Unknown')}")
            print(f"{info.get('content', '')}")
            print(f"Position x0: {annot.rect.x0}")
            #print(f"Position x1: {annot.rect.x1}")
            #print(f"Position y0: {annot.rect.y0}")
            print(f"Position y0: {annot.rect.y1}\n" + "-"*30)
        
class PSDViewer:
    def __init__(self, root, path, pdf, page:int):
        self.path = path
        self.root = root
        self.root.title("PSD Viewer dengan Tkinter")
        
        self.pdf = PDFViewer(pdf, page)

        # Frame utama
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame untuk canvas dan tombol
        self.content_frame = tk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas untuk menampilkan gambar
        self.canvas = tk.Canvas(self.content_frame, bg='gray')
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Frame untuk tombol-tombol
        self.button_frame = tk.Frame(self.content_frame, width=180, bg='lightgray')
        self.button_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)

        self.btn_zoom = tk.Button(self.button_frame, width= 20, text="Next")
        self.btn_zoom.pack(fill=tk.X, pady=2, padx= 4)

        self.btn_zoom2 = tk.Button(self.button_frame, width= 20, text="Prev")
        self.btn_zoom2.pack(fill=tk.X, pady=2, padx= 4)

        self.photo = None


    def open_psd(self):
    
        # Open PSD format with psd_tools
        psd = PSDImage.open(self.path)

        # Get info height and width 
        print (f" height = {psd.height}, width = {psd.width}, ratio = {psd.height / psd.width}")
        
        # PSD composite to img
        composite = psd.composite()
        height = 600
        width = (int(height * psd.width / psd.height))

        # Resize image composite
        composite = composite.resize((width , height), Image.LANCZOS)
        
        # Convert to PhotoImage
        self.photo = ImageTk.PhotoImage(composite)
        
        # Display on canvas
        self.canvas.create_image(
            composite.width/2 + 10, 
            composite.height/2 + 10, 
            image=self.photo
        )

        self.canvas.create_image(
            composite.width*3/2 + 20, 
            composite.height/2 + 10, 
            image=self.photo
        )

if __name__ == "__main__":
    root = tk.Tk()
    path = '08882685_047_1.psd'
    path_pdf = 'SakamotoDays Vol 2  cp 10.pdf'
    page = 3
    app = PSDViewer(root, path, path_pdf, page)
    root.geometry("970x620")
    app.open_psd()
    root.mainloop()