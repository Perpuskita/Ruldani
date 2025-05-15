import fitz  # PyMuPDF

# Buka file PDF
doc = fitz.open("Chapter4.pdf")


# Show PDF function
def show_pdf(annot):
    info = annot.info
    subtype = annot.type[0]  # Jenis anotasi (Text, Highlight, dll)
    content = info.get("content", "")
    author = info.get("title", "Unknown")
    rect = annot.rect  # Posisi anotasi

    width = page.rect.width
    height = page.rect.height
    print(f"  Lebar  = {width} poin")
    print(f"  Tinggi = {height} poin")
    print(f"  Jenis anotasi: {subtype}")
    print(f"  Penulis: {author}")
    print(content)
    print(f"  Posisi (x0, y0, x1, y1): {rect}")
    print("-" * 30)


# Loop halaman
for page_num, page in enumerate(doc, start=1):
    
    annot = page.first_annot
    while annot:
        show_pdf(annot)
        annot = annot.next
        

doc.close()
