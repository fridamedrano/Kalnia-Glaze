from collections import defaultdict
import re
from fontTools.pens.boundsPen import BoundsPen

#Alphas
ALPHA_AXIS_WDTH = { (("wdth", 100),): 1.0, (("wdth", 105),): 1.0, (("wdth", 125),): 0.2 }
ALPHA_AXIS_WGHT = { (("wght", 100),): 1.0, (("wght", 110),): 1.0, (("wght", 600),): 0.2, (("wght", 700),): 0.4 } 
ALPHA_AXIS_NONE = { (("wdth", 100),): 1.0, (("wdth", 125),): 1.0 }

#color palettes 
EXT01_PALETTE = ["#66357AFF", "#FF7979FF"]
EXT02_PALETTE = ["#3B171FFF", "#FDE7D8FF"]
EXT03_PALETTE = ["#B740AFFF", "#FF7979FF"]
EXT04_PALETTE = ["#3B171FFF", "#FDE7D8FF"]
EXT05_PALETTE = ["#FF306FFF", "#7AA0FFFF"]

INT01_PALETTE = ["#A762FFFF", "#DCCDFFFF"]
INT02_PALETTE = ["#9A8BC7FF", "#EAD5D3FF"]
INT03_PALETTE = ["#FF29F2FF", "#F9C4BFFF"]
INT04_PALETTE = ["#FF4DB2FF", "#FFB6A6FF"]
INT05_PALETTE = ["#9A8BC7FF", "#DCCDFFFF"]

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

glyphset = font.getGlyphSet()

for glyphname in base_glyphs:
    bp = BoundsPen(glyphset)
    glyphset[glyphname].draw(bp)
    if not bp.bounds:
        continue
    xMin, yMin, xMax, yMax = bp.bounds

    #Exterior colors (Outline)
    GRADIENT1 = PaintLinearGradient(
    (xMin, yMin), (xMax, yMax), (-90, 100),
    ColorLine({
        0: EXT01_PALLETE,
        0.2: EXT02_PALETTE, 
        0.4: EXT03_PALETTE, 
        1.6: EXT04_PALETTE,
        0.8: EXT05_PALETTE,
        })
    )
    
    #Interior colors (Fill)
    GRADIENT2 = PaintLinearGradient(
    (xMin, yMin), (xMax, yMax), (-90, 100),
    ColorLine({
        0:   (INT01_PALETTE, ALPHA_AXIS_WDTH),
        0.2: (INT02_PALETTE, ALPHA_AXIS_WGHT),
        0.4: INT03_PALETTE, 
        1.6: (INT04_PALETTE, ALPHA_AXIS_WDTH),
        0.8: (INT05_PALETTE, ALPHA_AXIS_WGHT),
        })
    )

    layers = [ PaintGlyph(glyphname, GRADIENT1) ] # Base layer
    for more_glyph in additional_layers.get(glyphname, []):
        layers.append(PaintGlyph(more_glyph, GRADIENT2))
    glyphs[glyphname] = PaintColrLayers(layers)
    
SetLightMode(0)
SetDarkMode(1)