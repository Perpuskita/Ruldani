"""Create a new document."""

from photoshop import Session
import photoshop.api as psd

app =psd.Application()


text = "hallo masyarakat dunia yang indah"

def join_str(text: str, split: int = 2) -> str:
    words = text.split()  # Memisahkan teks menjadi daftar kata
    cut_text = []

    for i in range(0, len(words), split):
        # Mengambil dua kata sekaligus dan menggabungkannya
        two_words = ' '.join(words[i:i+split])
        cut_text.append(two_words)
    
    return '\r'.join(cut_text)  # Mengembalikan hasil per baris

with Session() as ps:
    ps.app.preferences.rulerUnits = ps.Units.Pixels
    doc = ps.active_document

    text_color = ps.SolidColor()
    text_color.rgb.red = 0
    text_color.rgb.green = 0
    text_color.rgb.blue = 0

    new_text_layer = doc.artLayers.add()
    new_text_layer.kind = ps.LayerKind.TextLayer
    new_text_layer.textItem.contents = join_str(text)
    new_text_layer.textItem.position = [260, 267]
    new_text_layer.textItem.size = 12
    new_text_layer.textItem.color = text_color
    new_text_layer.textItem.fauxBold

    new_text_layer.textItem.justification = 2
    new_text_layer.textItem.autoLeadingAmount = 110

    
    