from collections import defaultdict
import re

ALPHA_AXIS = { (("wdth", 100),): 0.0, (("wdth", 125),): 1.0 }

GRADIENT1 = PaintLinearGradient(
    (0, 0), (1000, 1000), (-90, 100),
    ColorLine(
        {
            0.0: "#641EFFFF",
            0.3: "#E6E6C8FF",
            0.6: "#FF1463FF"
        }
    )
)

GRADIENT2 = PaintLinearGradient(
    (0, 0), (1000, 1000), (-90, 100),
    ColorLine(
        {
            0.0: "#C8FFFFFF",
            0.25: ("#968CFAFF", ALPHA_AXIS ),
            0.5: ("#FF00DCFF", ALPHA_AXIS ),
            0.75: "#FF82AAFF",
            1: "#FFDCDCFF"
        }
    )
)


base_glyphs = []
additional_layers = defaultdict(list)

# Split all glyphs in the font into either base or additional
for glyphname in font.getGlyphOrder():
    if ".color" in glyphname:
        baseglyph = re.sub(r".color.*", "", glyphname)
        # We ignore A.color0 and use the base A outline instead
        if glyphname.endswith(".color0"):
            continue
        additional_layers[baseglyph].append(glyphname)
    else:
        base_glyphs.append(glyphname)

for glyphname in base_glyphs:
    layers = [ PaintGlyph(glyphname, GRADIENT1) ] # Base layer
    for more_glyph in additional_layers.get(glyphname, []):
        layers.append(PaintGlyph(more_glyph, GRADIENT2))
    glyphs[glyphname] = PaintColrLayers(layers)
    