from photoshop import Session
import os
import fitz 

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

def write_text(doc, pos, text:str, font:str = "SofiaSansCondensed-Regular" ):
    
    text_color = ps.SolidColor()
    text_color.rgb.red = 0
    text_color.rgb.green = 0
    text_color.rgb.blue = 0
    
    new_text_layer = doc.artLayers.add()
    new_text_layer.kind = ps.LayerKind.TextLayer
    new_text_layer.textItem.contents = text
    new_text_layer.textItem.position = pos
    new_text_layer.textItem.size = 12
    new_text_layer.textItem.color = text_color
    new_text_layer.textItem.font = font
    new_text_layer.textItem.justification = 2
    new_text_layer.textItem.autoLeadingAmount = 110


def open_pdf( path, page):
    doc = fitz.open(path)
    page = doc[page]
    
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

    return height, width, container_temp

# Font Declaration

speech = "SofiaSansCondensed-Regular"
thoughts = "SofiaSansCondensed-Italic"
shout = "SofiaSansCondensed-Bold"
narasi_dalam_box = "SofiaSansCondensed-Medium"
narasi_luar_box = "SofiaSansCondensed-MediumItalic"
credit = "RobotoCondensed-Regular"
perkenalan_char = "NotoSerif-Medium"
small_text = "Mynerve-Regular"
sfx1= "ComicRelief-Bold"
sfx2= "DelaGothicOne-Regular"
sfx3= "Play-Bold"
sfx4= "Mansalva-Regular"

# Open File
path = '08882685_107_1.psd'
path_pdf = 'SakamotoDays Vol 2  cp 13.pdf'
page = 0

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'PSD')
file_path = os.path.join(file_path, path)
file_path = os.path.normpath(file_path).replace(os.sep, "/")

with Session(file_path,action="open") as ps:
    #ps.echo(ps.active_document.name)
    ps.app.preferences.rulerUnits = ps.Units.Pixels
    doc = ps.active_document

    print(doc.height/doc.width)
    data = open_pdf(path_pdf, page)
    print(data[0]/data[1])


    for pdf_open in data[2]:
        text = pdf_open.content_read()
        x,y = pdf_open.coor_read()
        new_x = doc.height/data[0]*x
        new_y = doc.width/data[1]*y
        write_text(doc, [new_x, new_y], text, speech)

    #write_text(doc, [240, 467], "hello world", sfx2)

    #main_group = doc.layerSets.add()
    #main_group.name = "Main Group"