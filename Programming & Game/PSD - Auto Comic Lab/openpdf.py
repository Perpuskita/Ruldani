import fitz  # PyMuPDF

def show_annotations(page):
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

def open_pdf(path, page: int):
    doc = fitz.open(path)
    page = doc[page] 
    show_annotations(page)

if __name__ == "__main__":
    open_pdf("Chapter4.pdf", 18)