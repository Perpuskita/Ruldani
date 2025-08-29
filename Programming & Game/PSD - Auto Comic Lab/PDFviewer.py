from container import container
import fitz

class PDFViewer:
    def __init__(self, path, page):
        self.path = path
        #self.page = page
        # self.open_pdf()
        self.container = []
        doc = fitz.open(self.path)
        self.page = doc[page]
    
    def content(self):
        # Empty container_temp
        self.container =[]
        # print(f"Page size: {width:.1f} x {height:.1f} points")
        
        for annot in self.page.annots():
            info = annot.info
            print(f"Type: {annot.type[1]}")
            print(f"Author: {info.get('title', 'Unknown')}")
            print(f"{info.get('content', '')}")
            print(f"Position x0: {annot.rect.x0}")
            print(f"Position x1: {annot.rect.x1}")
            print(f"Position y0: {annot.rect.y0}")
            print(f"Position y0: {annot.rect.y1}\n" + "-"*30)
            self.container.append(container(info.get('content', ''), annot.rect.x0, annot.rect.y1 ))

        return self.container

    def rect(self):
        # Display information about annotations on a PDF page
        width, height = self.page.rect.width, self.page.rect.height
        return height, width