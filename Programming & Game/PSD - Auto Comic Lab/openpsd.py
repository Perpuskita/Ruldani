from psd_tools import PSDImage
from PIL import Image, ImageTk
import tkinter as tk

class PSDViewer:
    def __init__(self, root, path):
        self.path = path
        self.root = root
        self.root.title("PSD Viewer dengan Tkinter")
        
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

        self.btn_zoom = tk.Button(self.button_frame, width= 20, text="Zoom In")
        self.btn_zoom.pack(fill=tk.X, pady=2, padx= 4)

        self.btn_zoom2 = tk.Button(self.button_frame, width= 20, text="Zoom In")
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

if __name__ == "__main__":
    root = tk.Tk()
    path = 'Panel129.psd'
    app = PSDViewer(root, path)
    root.geometry("600x620")
    app.open_psd()
    root.mainloop()