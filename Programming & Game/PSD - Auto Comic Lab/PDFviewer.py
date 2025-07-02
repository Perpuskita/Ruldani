from container import container
import fitz

class PDFViewer:
    def __init__(self, path, page):
        self.path = path
        self.page = page

        # self.open_pdf()
    
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
        
        container_temp =[]

        print(f"Page size: {width:.1f} x {height:.1f} points")
        for annot in page.annots():
            info = annot.info
            # print(f"Type: {annot.type[1]}")
            # print(f"Author: {info.get('title', 'Unknown')}")
            # print(f"{info.get('content', '')}")
            # print(f"Position x0: {annot.rect.x0}")
            # print(f"Position x1: {annot.rect.x1}")
            # print(f"Position y0: {annot.rect.y0}")
            # print(f"Position y0: {annot.rect.y1}\n" + "-"*30)
            container_temp.append(container(info.get('content', ''), annot.rect.x0, annot.rect.y1  ))

        # print(container_temp)

        return height, width, container_temp

