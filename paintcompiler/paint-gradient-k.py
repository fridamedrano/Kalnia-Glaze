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

for glyphname in font.getGlyphOrder():
    advancewidth = font["hmtx"][glyphname][0]
    glyphs[glyphname] = PaintColrLayers([
        # Paint the glyph in red
        PaintGlyph(glyphname, GRADIENT1)
    ])