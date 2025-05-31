"""Create a new document."""

from photoshop import Session

with Session() as ps:
    ps.app.preferences.rulerUnits = ps.Units.Pixels
    doc = ps.active_document

    text_color = ps.SolidColor()
    text_color.rgb.red = 0
    text_color.rgb.green = 0
    text_color.rgb.blue = 0

    new_text_layer = doc.artLayers.add()
    new_text_layer.kind = ps.LayerKind.TextLayer
    new_text_layer.textItem.contents = "Hello, World!"
    new_text_layer.textItem.position = [260, 267]
    new_text_layer.textItem.size = 12
    new_text_layer.textItem.color = text_color
    new_text_layer.textItem.fauxBold

    print(new_text_layer.textItem.font)