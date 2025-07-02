import fitz  # PyMuPDF
import matplotlib.pyplot as plt
import numpy as np

class container():
    def __init__(self, content, coor_x, coor_y):
        self.content = content
        self.coor_x = coor_x
        self.coor_y = coor_y

    def content_read(self, split:int = 2):

        text = self.content.split("TRS:", 1)[-1]
        words = text.split()
        cut_text = []

        for i in range(0, len(words), split):
            
            two_words = ' '.join(words[i:i+split])
            cut_text.append(two_words)
        
        return '\r'.join(cut_text)
    
    def coor_read(self):
        return self.coor_x, self.coor_y
    
def show_annotations(page):

    """Display information about annotations on a PDF page."""
    width, height = page.rect.width, page.rect.height
    #print(f"Page size: {width:.1f} x {height:.1f} points")
    container_temp =[]

    for annot in page.annots():
        info = annot.info
        # print(f"Type: {annot.type[1]}")
        # print(f"Author: {info.get('title', 'Unknown')}")
        # print(f"{info.get('content', '')}")
        # print(f"Position x0: {annot.rect.x0}")
        #     #print(f"Position x1: {annot.rect.x1}")
        #     #print(f"Position y0: {annot.rect.y0}")
        # print(f"Position y0: {annot.rect.y1}\n" + "-"*30)
        container_temp.append(container(info.get('content', ''), annot.rect.x0, annot.rect.y1  ))

    # print(container_temp)

    return container_temp

def show_cropped(img_container):
    fig, axes = plt.subplots(1, len(img_container), figsize=(15, 5))
    
    if len(img_container) == 1:
        axes = [axes]  # Untuk kasus hanya satu gambar
    
    for idx, img in enumerate(img_container):
        axes[idx].imshow(img)
        axes[idx].axis('off')
        axes[idx].set_title(f'Gambar {idx+1}')
    
    plt.tight_layout()
    plt.show()

def open_pdf(path, page: int):
    doc = fitz.open(path)
    page = doc[page] 
    annot = show_annotations(page)

    for img in annot :
        # print(img.coor_read())
        x0, y0 = img.coor_read()
        
        x0, y0 = int(x0), int(y0)
        # Method 1: Jika tahu ukuran tetap
        width, height = 100, 50  # Sesuaikan!
        x1, y1 = x0 + width, y0 + height

        print(x0, y0, x1, y1)
        
if __name__ == "__main__":
    open_pdf("SakamotoDays Vol 2  cp 13.pdf", 18)