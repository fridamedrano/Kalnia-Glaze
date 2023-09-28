from collections import defaultdict
import re
from fontTools.pens.boundsPen import BoundsPen

ALPHA_AXIS_WDTH = { (("wdth", 100),): 0.0, (("wdth", 115),): 1.0, (("wdth", 125),): 0.0 }
ALPHA_AXIS_WGHT = { (("wght", 100),): 1.0, (("wght", 100),): 0.0, (("wght", 700),): 1.0 }
ALPHA_AXIS_NONE = { (("wdth", 100),): 1.0, (("wdth", 125),): 1.0 }

MG01 = { (("wght", 100),): 0.0, (("wght", 700),): 0.2 }
MG02 = { (("wght", 100),): 0.2, (("wght", 700),): 0.4 }
MG03 = { (("wght", 100),): 0.4, (("wght", 700),): 0.6 }
MG04 = { (("wght", 100),): 0.6, (("wght", 700),): 0.8 }
MG05 = { (("wght", 100),): 0.8, (("wght", 700),): 1.0 }

SG01 = { (("wght", 100),): 0.0, (("wght", 700),): 0.1 }
SG02 = { (("wght", 100),): 0.1, (("wght", 700),): 0.2 }
SG03 = { (("wght", 100),): 0.2, (("wght", 700),): 0.8 }
SG04 = { (("wght", 100),): 0.8, (("wght", 700),): 1.0 }


base_glyphs = []
additional_layers = defaultdict(list)


# Split all glyphs in the font into either base or additional
for glyphname in font.getGlyphOrder():
    if ".layer" in glyphname:
        baseglyph = re.sub(r".layer.*", "", glyphname)
        # We ignore A.color0 and use the base A outline instead
        if glyphname.endswith(".layer0"):
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

    GRADIENT1 = PaintLinearGradient(
    (xMin, yMin), (xMax, yMax), (-90, 100),
    ColorLine([
        (MG01, "#F67F68FF"),
        (MG02, ("#FDE7D8FF", ALPHA_AXIS_NONE )),
        (MG03, "#FF8B8BFF"),
        (MG04, "#FDE7D8FF"),
        (MG05, "#7AA0FFFF")
        ])
    )
    
    GRADIENT2 = PaintLinearGradient(
    (xMin, yMin), (xMax, yMax), (-90, 100),
    ColorLine([
        (SG01, ("#FFB5C2FF", ALPHA_AXIS_WGHT )),
        (SG02, ("#EAD5D3FF", ALPHA_AXIS_WDTH )),
        (SG03, ("#FFB6A6FF", ALPHA_AXIS_WGHT )),
        (SG04, ("#D6E4EEFF", ALPHA_AXIS_WDTH )),
        ])
    )

    layers = [ PaintGlyph(glyphname, GRADIENT1) ] # Base layer
    for more_glyph in additional_layers.get(glyphname, []):
        layers.append(PaintGlyph(more_glyph, GRADIENT2))
    glyphs[glyphname] = PaintColrLayers(layers)
    