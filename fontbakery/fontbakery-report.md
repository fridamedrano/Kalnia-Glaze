## Fontbakery report

Fontbakery version: 0.8.9

<details><summary><b>[14] Kalnia-Color-RegularExtended.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-RegularExtended.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0308 (COMBINING DIAERESIS)


	- 0x0300 (COMBINING GRAVE ACCENT)


	- 0x0301 (COMBINING ACUTE ACCENT)


	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x0304 (COMBINING MACRON)


	- 0x0102 (LATIN CAPITAL LETTER A WITH BREVE)


	- 0x01CD (LATIN CAPITAL LETTER A WITH CARON)


	- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


	- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)


	- 0x0106 (LATIN CAPITAL LETTER C WITH ACUTE)
 

	- And 115 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender+abs(hhea.descender)+hhea.lineGap is 1141 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces">com.google.fonts/check/name/trailing_spaces</a>)</summary><div>


* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 10) has trailing spaces that must be removed: 'Kalnia is [...]dth axes. ' [code: trailing-space]
</div></details><details><summary>🔥 <b>FAIL:</b> Does full font name begin with the font family name? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/match_familyname_fullfont">com.google.fonts/check/name/match_familyname_fullfont</a>)</summary><div>


* 🔥 **FAIL** On the 'name' table, the full font name 'Kalnia-Color Regular Extended' does not begin with the font family name 'Kalnia-Color Extended' in platformID 3, encodingID 1, languageID 1033(0409), and nameID 1. [code: mismatch-font-names]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + b

	- b + f

	- f + h

	- h + i

	- i + j

	- j + k 

	- And k + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Kalnia-Color Extended' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 4	Expected: 2

	- Glyph name: quotedbl	Contours detected: 4	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: percent	Contours detected: 9	Expected: 5

	- Glyph name: ampersand	Contours detected: 8	Expected: 1, 2 or 3

	- Glyph name: quotesingle	Contours detected: 2	Expected: 1

	- Glyph name: parenleft	Contours detected: 2	Expected: 1

	- Glyph name: parenright	Contours detected: 2	Expected: 1

	- Glyph name: asterisk	Contours detected: 7	Expected: 1 or 4 

	- And 391 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fi (U+FB01): L<<439.0,500.0>--<621.0,492.0>> -> L<<621.0,492.0>--<1082.0,515.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<236.0,154.0>-<236.0,192.0>-<253.0,238.0>>/L<<253.0,238.0>--<108.0,13.0>> = 12.516972183702592

	* A (U+0041): L<<661.0,302.0>--<413.0,296.0>>/L<<413.0,296.0>--<661.0,295.0>> = 1.6169479677075704

	* AE (U+00C6): B<<1465.5,45.5>-<1435.0,23.0>-<1388.0,14.0>>/L<<1388.0,14.0>--<1628.0,14.0>> = 10.840305454330565

	* AE (U+00C6): L<<1628.0,694.0>--<1372.0,694.0>>/B<<1372.0,694.0>-<1416.0,687.0>-<1446.5,666.5>> = 9.039482803355098

	* AE (U+00C6): L<<484.0,287.0>--<365.0,294.0>>/L<<365.0,294.0>--<535.0,308.0>> = 8.074312907802039

	* Aacute (U+00C1): B<<236.0,154.0>-<236.0,192.0>-<253.0,238.0>>/L<<253.0,238.0>--<108.0,13.0>> = 12.516972183702592

	* Aacute (U+00C1): L<<661.0,302.0>--<413.0,296.0>>/L<<413.0,296.0>--<661.0,295.0>> = 1.6169479677075704

	* Acircumflex (U+00C2): B<<236.0,154.0>-<236.0,192.0>-<253.0,238.0>>/L<<253.0,238.0>--<108.0,13.0>> = 12.516972183702592

	* Acircumflex (U+00C2): L<<661.0,302.0>--<413.0,296.0>>/L<<413.0,296.0>--<661.0,295.0>> = 1.6169479677075704

	* Adieresis (U+00C4): B<<236.0,154.0>-<236.0,192.0>-<253.0,238.0>>/L<<253.0,238.0>--<108.0,13.0>> = 12.516972183702592 

	* And 176 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* A (U+0041): L<<413.0,296.0>--<661.0,295.0>>

	* AE (U+00C6): L<<1301.0,692.0>--<942.0,693.0>>

	* AE (U+00C6): L<<942.0,15.0>--<1309.0,16.0>>

	* Aacute (U+00C1): L<<413.0,296.0>--<661.0,295.0>>

	* Acircumflex (U+00C2): L<<413.0,296.0>--<661.0,295.0>>

	* Adieresis (U+00C4): L<<413.0,296.0>--<661.0,295.0>>

	* Agrave (U+00C0): L<<413.0,296.0>--<661.0,295.0>>

	* Aring (U+00C5): L<<413.0,296.0>--<661.0,295.0>>

	* Atilde (U+00C3): L<<413.0,296.0>--<661.0,295.0>>

	* E (U+0045): L<<430.0,15.0>--<797.0,16.0>> 

	* And 25 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[12] Kalnia-Color-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-Regular.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0308 (COMBINING DIAERESIS)


	- 0x0300 (COMBINING GRAVE ACCENT)


	- 0x0301 (COMBINING ACUTE ACCENT)


	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x0304 (COMBINING MACRON)


	- 0x0102 (LATIN CAPITAL LETTER A WITH BREVE)


	- 0x01CD (LATIN CAPITAL LETTER A WITH CARON)


	- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


	- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)


	- 0x0106 (LATIN CAPITAL LETTER C WITH ACUTE)
 

	- And 115 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender+abs(hhea.descender)+hhea.lineGap is 1141 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces">com.google.fonts/check/name/trailing_spaces</a>)</summary><div>


* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 10) has trailing spaces that must be removed: 'Kalnia is [...]dth axes. ' [code: trailing-space]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + b

	- b + f

	- f + h

	- h + i

	- i + j

	- j + k 

	- And k + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 4	Expected: 2

	- Glyph name: quotedbl	Contours detected: 4	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: percent	Contours detected: 9	Expected: 5

	- Glyph name: ampersand	Contours detected: 8	Expected: 1, 2 or 3

	- Glyph name: quotesingle	Contours detected: 2	Expected: 1

	- Glyph name: parenleft	Contours detected: 2	Expected: 1

	- Glyph name: parenright	Contours detected: 2	Expected: 1

	- Glyph name: asterisk	Contours detected: 7	Expected: 1 or 4 

	- And 391 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* at (U+0040): L<<578.0,429.0>--<568.0,377.0>> -> L<<568.0,377.0>--<566.0,370.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<157.0,147.0>-<157.0,181.0>-<168.0,225.0>>/L<<168.0,225.0>--<82.0,13.0>> = 8.044201699606887

	* A (U+0041): L<<434.0,302.0>--<253.0,296.0>>/L<<253.0,296.0>--<434.0,296.0>> = 1.8986123706587712

	* Aacute (U+00C1): B<<157.0,147.0>-<157.0,181.0>-<168.0,225.0>>/L<<168.0,225.0>--<82.0,13.0>> = 8.044201699606887

	* Aacute (U+00C1): L<<434.0,302.0>--<253.0,296.0>>/L<<253.0,296.0>--<434.0,296.0>> = 1.8986123706587712

	* Acircumflex (U+00C2): B<<157.0,147.0>-<157.0,181.0>-<168.0,225.0>>/L<<168.0,225.0>--<82.0,13.0>> = 8.044201699606887

	* Acircumflex (U+00C2): L<<434.0,302.0>--<253.0,296.0>>/L<<253.0,296.0>--<434.0,296.0>> = 1.8986123706587712

	* Adieresis (U+00C4): B<<157.0,147.0>-<157.0,181.0>-<168.0,225.0>>/L<<168.0,225.0>--<82.0,13.0>> = 8.044201699606887

	* Adieresis (U+00C4): L<<434.0,302.0>--<253.0,296.0>>/L<<253.0,296.0>--<434.0,296.0>> = 1.8986123706587712

	* Agrave (U+00C0): B<<157.0,147.0>-<157.0,181.0>-<168.0,225.0>>/L<<168.0,225.0>--<82.0,13.0>> = 8.044201699606887

	* Agrave (U+00C0): L<<434.0,302.0>--<253.0,296.0>>/L<<253.0,296.0>--<434.0,296.0>> = 1.8986123706587712 

	* And 151 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<576.0,15.0>--<776.0,16.0>>

	* AE (U+00C6): L<<768.0,692.0>--<576.0,693.0>>

	* E (U+0045): L<<249.0,15.0>--<449.0,16.0>>

	* E (U+0045): L<<441.0,692.0>--<249.0,693.0>>

	* Eacute (U+00C9): L<<249.0,15.0>--<449.0,16.0>>

	* Eacute (U+00C9): L<<441.0,692.0>--<249.0,693.0>>

	* Ecircumflex (U+00CA): L<<249.0,15.0>--<449.0,16.0>>

	* Ecircumflex (U+00CA): L<<441.0,692.0>--<249.0,693.0>>

	* Edieresis (U+00CB): L<<249.0,15.0>--<449.0,16.0>>

	* Edieresis (U+00CB): L<<441.0,692.0>--<249.0,693.0>> 

	* And 23 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[12] Kalnia-Color-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-Thin.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0308 (COMBINING DIAERESIS)


	- 0x0300 (COMBINING GRAVE ACCENT)


	- 0x0301 (COMBINING ACUTE ACCENT)


	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x0304 (COMBINING MACRON)


	- 0x0102 (LATIN CAPITAL LETTER A WITH BREVE)


	- 0x01CD (LATIN CAPITAL LETTER A WITH CARON)


	- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


	- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)


	- 0x0106 (LATIN CAPITAL LETTER C WITH ACUTE)
 

	- And 115 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender+abs(hhea.descender)+hhea.lineGap is 1141 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces">com.google.fonts/check/name/trailing_spaces</a>)</summary><div>


* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 10) has trailing spaces that must be removed: 'Kalnia is [...]dth axes. ' [code: trailing-space]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + b

	- b + f

	- f + h

	- h + i

	- i + j

	- j + k 

	- And k + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 4	Expected: 2

	- Glyph name: quotedbl	Contours detected: 4	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: percent	Contours detected: 9	Expected: 5

	- Glyph name: ampersand	Contours detected: 8	Expected: 1, 2 or 3

	- Glyph name: quotesingle	Contours detected: 2	Expected: 1

	- Glyph name: parenleft	Contours detected: 2	Expected: 1

	- Glyph name: parenright	Contours detected: 2	Expected: 1

	- Glyph name: asterisk	Contours detected: 7	Expected: 1 or 4 

	- And 393 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* A (U+0041): L<<206.0,295.0>--<206.0,295.0>> -> L<<206.0,295.0>--<494.0,295.0>>

	* Aacute (U+00C1): L<<206.0,295.0>--<206.0,295.0>> -> L<<206.0,295.0>--<494.0,295.0>>

	* Acircumflex (U+00C2): L<<206.0,295.0>--<206.0,295.0>> -> L<<206.0,295.0>--<494.0,295.0>>

	* Acircumflex (U+00C2): L<<351.0,887.0>--<353.0,885.0>> -> L<<353.0,885.0>--<476.0,771.0>>

	* Adieresis (U+00C4): L<<206.0,295.0>--<206.0,295.0>> -> L<<206.0,295.0>--<494.0,295.0>>

	* Agrave (U+00C0): L<<206.0,295.0>--<206.0,295.0>> -> L<<206.0,295.0>--<494.0,295.0>>

	* Aring (U+00C5): L<<206.0,295.0>--<206.0,295.0>> -> L<<206.0,295.0>--<494.0,295.0>>

	* Atilde (U+00C3): L<<206.0,295.0>--<206.0,295.0>> -> L<<206.0,295.0>--<494.0,295.0>>

	* Ecircumflex (U+00CA): L<<381.0,886.0>--<383.0,884.0>> -> L<<383.0,884.0>--<506.0,770.0>>

	* Icircumflex (U+00CE): L<<170.0,887.0>--<172.0,885.0>> -> L<<172.0,885.0>--<295.0,771.0>> 

	* And 24 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* A (U+0041): L<<494.0,300.0>--<206.0,295.0>>/L<<206.0,295.0>--<206.0,295.0>> = 0.9946184736404607

	* A (U+0041): L<<89.0,5.0>--<160.0,5.0>>/B<<160.0,5.0>-<113.0,14.0>-<113.0,50.0>> = 10.840305454330565

	* AE (U+00C6): B<<839.5,25.5>-<827.0,8.0>-<789.0,7.0>>/L<<789.0,7.0>--<858.0,7.0>> = 1.5074357587748821

	* AE (U+00C6): L<<664.0,360.0>--<668.0,288.0>>/L<<668.0,288.0>--<668.0,388.0>> = 3.1798301198641643

	* AE (U+00C6): L<<668.0,288.0>--<668.0,388.0>>/B<<668.0,388.0>-<667.0,381.0>-<666.0,374.0>> = 8.13010235415596

	* AE (U+00C6): L<<840.0,634.0>--<826.0,491.0>>/L<<826.0,491.0>--<858.0,701.0>> = 3.072577677350764

	* AE (U+00C6): L<<858.0,7.0>--<825.0,236.0>>/L<<825.0,236.0>--<846.0,84.0>> = 0.33407768660106585

	* AE (U+00C6): L<<858.0,701.0>--<772.0,701.0>>/B<<772.0,701.0>-<813.0,700.0>-<828.5,685.5>> = 1.397181027296108

	* AE (U+00C6): L<<90.0,5.0>--<168.0,5.0>>/B<<168.0,5.0>-<121.0,14.0>-<121.0,50.0>> = 10.840305454330565 

	* And 557 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* seven (U+0037): L<<85.0,709.0>--<84.0,592.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[12] Kalnia-Color-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-Light.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0308 (COMBINING DIAERESIS)


	- 0x0300 (COMBINING GRAVE ACCENT)


	- 0x0301 (COMBINING ACUTE ACCENT)


	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x0304 (COMBINING MACRON)


	- 0x0102 (LATIN CAPITAL LETTER A WITH BREVE)


	- 0x01CD (LATIN CAPITAL LETTER A WITH CARON)


	- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


	- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)


	- 0x0106 (LATIN CAPITAL LETTER C WITH ACUTE)
 

	- And 115 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender+abs(hhea.descender)+hhea.lineGap is 1141 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces">com.google.fonts/check/name/trailing_spaces</a>)</summary><div>


* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 10) has trailing spaces that must be removed: 'Kalnia is [...]dth axes. ' [code: trailing-space]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + b

	- b + f

	- f + h

	- h + i

	- i + j

	- j + k 

	- And k + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 4	Expected: 2

	- Glyph name: quotedbl	Contours detected: 4	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: percent	Contours detected: 9	Expected: 5

	- Glyph name: ampersand	Contours detected: 8	Expected: 1, 2 or 3

	- Glyph name: quotesingle	Contours detected: 2	Expected: 1

	- Glyph name: parenleft	Contours detected: 2	Expected: 1

	- Glyph name: parenright	Contours detected: 2	Expected: 1

	- Glyph name: asterisk	Contours detected: 7	Expected: 1 or 4 

	- And 391 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Scaron (U+0160): L<<420.0,836.0>--<434.0,842.0>> -> L<<434.0,842.0>--<449.0,848.0>>

	* Zcaron (U+017D): L<<425.0,843.0>--<439.0,849.0>> -> L<<439.0,849.0>--<454.0,855.0>>

	* ampersand (U+0026): L<<479.0,185.0>--<480.0,187.0>> -> L<<480.0,187.0>--<504.0,237.0>>

	* caron (U+02C7): L<<244.0,655.0>--<258.0,661.0>> -> L<<258.0,661.0>--<273.0,667.0>>

	* cent (U+00A2): L<<315.0,53.0>--<324.0,53.0>> -> L<<324.0,53.0>--<324.0,53.0>>

	* scaron (U+0161): L<<337.0,655.0>--<351.0,661.0>> -> L<<351.0,661.0>--<366.0,667.0>> 

	* And zcaron (U+017E): L<<348.0,655.0>--<362.0,661.0>> -> L<<362.0,661.0>--<377.0,667.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<133.0,93.0>-<133.0,119.0>-<145.0,157.0>>/L<<145.0,157.0>--<86.0,9.0>> = 4.209062845065125

	* A (U+0041): L<<467.0,301.0>--<224.0,295.0>>/L<<224.0,295.0>--<467.0,295.0>> = 1.4144232114020547

	* AE (U+00C6): B<<851.0,34.5>-<836.0,15.0>-<802.0,10.0>>/L<<802.0,10.0>--<892.0,10.0>> = 8.365886124032546

	* AE (U+00C6): L<<855.0,628.0>--<862.0,488.0>>/L<<862.0,488.0>--<892.0,698.0>> = 10.992507580267716

	* AE (U+00C6): L<<892.0,10.0>--<862.0,233.0>>/L<<862.0,233.0>--<866.0,95.0>> = 6.001668785989419

	* AE (U+00C6): L<<892.0,698.0>--<788.0,698.0>>/B<<788.0,698.0>-<823.0,694.0>-<838.5,678.5>> = 6.5198017516569164

	* Aacute (U+00C1): B<<133.0,93.0>-<133.0,119.0>-<145.0,157.0>>/L<<145.0,157.0>--<86.0,9.0>> = 4.209062845065125

	* Aacute (U+00C1): L<<467.0,301.0>--<224.0,295.0>>/L<<224.0,295.0>--<467.0,295.0>> = 1.4144232114020547

	* Acircumflex (U+00C2): B<<133.0,93.0>-<133.0,119.0>-<145.0,157.0>>/L<<145.0,157.0>--<86.0,9.0>> = 4.209062845065125

	* Acircumflex (U+00C2): L<<467.0,301.0>--<224.0,295.0>>/L<<224.0,295.0>--<467.0,295.0>> = 1.4144232114020547 

	* And 385 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<856.0,97.0>--<857.0,253.0>>

	* C (U+0043): L<<592.0,379.0>--<593.0,522.0>>

	* Ccedilla (U+00C7): L<<592.0,379.0>--<593.0,522.0>>

	* E (U+0045): L<<558.0,97.0>--<559.0,253.0>>

	* Eacute (U+00C9): L<<558.0,97.0>--<559.0,253.0>>

	* Ecircumflex (U+00CA): L<<558.0,97.0>--<559.0,253.0>>

	* Edieresis (U+00CB): L<<558.0,97.0>--<559.0,253.0>>

	* Egrave (U+00C8): L<<558.0,97.0>--<559.0,253.0>>

	* M (U+004D): L<<143.0,179.0>--<144.0,10.0>>

	* M (U+004D): L<<751.0,24.0>--<752.0,606.0>> 

	* And 4 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[13] Kalnia-Color-ThinExtended.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-ThinExtended.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0308 (COMBINING DIAERESIS)


	- 0x0300 (COMBINING GRAVE ACCENT)


	- 0x0301 (COMBINING ACUTE ACCENT)


	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x0304 (COMBINING MACRON)


	- 0x0102 (LATIN CAPITAL LETTER A WITH BREVE)


	- 0x01CD (LATIN CAPITAL LETTER A WITH CARON)


	- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


	- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)


	- 0x0106 (LATIN CAPITAL LETTER C WITH ACUTE)
 

	- And 115 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender+abs(hhea.descender)+hhea.lineGap is 1141 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces">com.google.fonts/check/name/trailing_spaces</a>)</summary><div>


* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 10) has trailing spaces that must be removed: 'Kalnia is [...]dth axes. ' [code: trailing-space]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + b

	- b + f

	- f + h

	- h + i

	- i + j

	- j + k 

	- And k + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Kalnia-Color Thin Extended' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 4	Expected: 2

	- Glyph name: quotedbl	Contours detected: 4	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: percent	Contours detected: 9	Expected: 5

	- Glyph name: ampersand	Contours detected: 8	Expected: 1, 2 or 3

	- Glyph name: quotesingle	Contours detected: 2	Expected: 1

	- Glyph name: parenleft	Contours detected: 2	Expected: 1

	- Glyph name: parenright	Contours detected: 2	Expected: 1

	- Glyph name: asterisk	Contours detected: 7	Expected: 1 or 4 

	- And 393 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Acircumflex (U+00C2): L<<528.0,887.0>--<531.0,885.0>> -> L<<531.0,885.0>--<681.0,772.0>>

	* Ecircumflex (U+00CA): L<<565.0,886.0>--<568.0,884.0>> -> L<<568.0,884.0>--<718.0,771.0>>

	* Icircumflex (U+00CE): L<<233.0,887.0>--<236.0,885.0>> -> L<<236.0,885.0>--<386.0,772.0>>

	* M (U+004D): L<<1065.0,682.0>--<1059.0,673.0>> -> L<<1059.0,673.0>--<1032.0,629.0>>

	* Ocircumflex (U+00D4): L<<587.0,887.0>--<590.0,885.0>> -> L<<590.0,885.0>--<740.0,772.0>>

	* Scaron (U+0160): L<<700.0,874.0>--<550.0,761.0>> -> L<<550.0,761.0>--<547.0,759.0>>

	* Ucircumflex (U+00DB): L<<560.0,886.0>--<563.0,884.0>> -> L<<563.0,884.0>--<713.0,771.0>>

	* Zcaron (U+017D): L<<684.0,884.0>--<534.0,771.0>> -> L<<534.0,771.0>--<531.0,769.0>>

	* acircumflex (U+00E2): L<<451.0,692.0>--<454.0,690.0>> -> L<<454.0,690.0>--<604.0,577.0>>

	* caron (U+02C7): L<<351.0,701.0>--<201.0,588.0>> -> L<<201.0,588.0>--<198.0,586.0>> 

	* And 17 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<179.0,50.0>-<179.0,68.0>-<191.0,90.0>>/L<<191.0,90.0>--<142.0,5.0>> = 1.3517244304524603

	* A (U+0041): L<<142.0,5.0>--<248.0,5.0>>/B<<248.0,5.0>-<179.0,14.0>-<179.0,50.0>> = 7.431407971172489

	* A (U+0041): L<<763.0,300.0>--<316.0,295.0>>/L<<316.0,295.0>--<763.0,294.0>> = 0.7690439247434497

	* AE (U+00C6): B<<1315.0,27.0>-<1303.0,8.0>-<1265.0,7.0>>/L<<1265.0,7.0>--<1334.0,7.0>> = 1.5074357587748821

	* AE (U+00C6): L<<1000.0,360.0>--<1004.0,288.0>>/L<<1004.0,288.0>--<1004.0,388.0>> = 3.1798301198641643

	* AE (U+00C6): L<<1004.0,288.0>--<1004.0,388.0>>/B<<1004.0,388.0>-<1003.0,381.0>-<1002.0,374.0>> = 8.13010235415596

	* AE (U+00C6): L<<1317.0,624.0>--<1302.0,491.0>>/L<<1302.0,491.0>--<1334.0,701.0>> = 2.2293962820711486

	* AE (U+00C6): L<<1334.0,7.0>--<1302.0,236.0>>/L<<1302.0,236.0>--<1321.0,92.0>> = 0.4384447329817478

	* AE (U+00C6): L<<1334.0,701.0>--<1248.0,701.0>>/B<<1248.0,701.0>-<1290.0,700.0>-<1306.0,682.5>> = 1.3639275316029233

	* AE (U+00C6): L<<136.0,5.0>--<250.0,5.0>>/B<<250.0,5.0>-<181.0,14.0>-<181.0,50.0>> = 7.431407971172489 

	* And 578 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* A (U+0041): L<<316.0,295.0>--<763.0,294.0>>

	* Aacute (U+00C1): L<<316.0,295.0>--<763.0,294.0>>

	* Acircumflex (U+00C2): L<<316.0,295.0>--<763.0,294.0>>

	* Adieresis (U+00C4): L<<316.0,295.0>--<763.0,294.0>>

	* Agrave (U+00C0): L<<316.0,295.0>--<763.0,294.0>>

	* Aring (U+00C5): L<<316.0,295.0>--<763.0,294.0>>

	* Atilde (U+00C3): L<<316.0,295.0>--<763.0,294.0>>

	* H (U+0048): L<<225.0,342.0>--<945.0,348.0>>

	* ae (U+00E6): L<<785.0,286.0>--<1545.0,290.0>>

	* e (U+0065): L<<83.0,286.0>--<843.0,290.0>> 

	* And 8 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[12] Kalnia-Color-LightExtended.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-LightExtended.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0308 (COMBINING DIAERESIS)


	- 0x0300 (COMBINING GRAVE ACCENT)


	- 0x0301 (COMBINING ACUTE ACCENT)


	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x0304 (COMBINING MACRON)


	- 0x0102 (LATIN CAPITAL LETTER A WITH BREVE)


	- 0x01CD (LATIN CAPITAL LETTER A WITH CARON)


	- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


	- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)


	- 0x0106 (LATIN CAPITAL LETTER C WITH ACUTE)
 

	- And 115 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender+abs(hhea.descender)+hhea.lineGap is 1141 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces">com.google.fonts/check/name/trailing_spaces</a>)</summary><div>


* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 10) has trailing spaces that must be removed: 'Kalnia is [...]dth axes. ' [code: trailing-space]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + b

	- b + f

	- f + h

	- h + i

	- i + j

	- j + k 

	- And k + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Kalnia-Color Light Extended' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 4	Expected: 2

	- Glyph name: quotedbl	Contours detected: 4	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: percent	Contours detected: 9	Expected: 5

	- Glyph name: ampersand	Contours detected: 8	Expected: 1, 2 or 3

	- Glyph name: quotesingle	Contours detected: 2	Expected: 1

	- Glyph name: parenleft	Contours detected: 2	Expected: 1

	- Glyph name: parenright	Contours detected: 2	Expected: 1

	- Glyph name: asterisk	Contours detected: 7	Expected: 1 or 4 

	- And 393 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<205.0,96.0>-<205.0,126.0>-<223.0,163.0>>/L<<223.0,163.0>--<127.0,9.0>> = 5.996153426800191

	* A (U+0041): L<<127.0,9.0>--<293.0,9.0>>/B<<293.0,9.0>-<246.0,20.0>-<225.5,40.0>> = 13.172553423326871

	* A (U+0041): L<<718.0,301.0>--<359.0,295.0>>/L<<359.0,295.0>--<718.0,295.0>> = 0.9575004843313389

	* AE (U+00C6): B<<1381.5,35.0>-<1361.0,14.0>-<1320.0,10.0>>/L<<1320.0,10.0>--<1465.0,10.0>> = 5.572197803963754

	* AE (U+00C6): L<<124.0,9.0>--<299.0,9.0>>/B<<299.0,9.0>-<261.0,17.0>-<241.5,33.5>> = 11.888658039627968

	* AE (U+00C6): L<<1465.0,698.0>--<1303.0,698.0>>/B<<1303.0,698.0>-<1346.0,694.0>-<1368.5,675.5>> = 5.3145456699447315

	* Aacute (U+00C1): B<<205.0,96.0>-<205.0,126.0>-<223.0,163.0>>/L<<223.0,163.0>--<127.0,9.0>> = 5.996153426800191

	* Aacute (U+00C1): L<<127.0,9.0>--<293.0,9.0>>/B<<293.0,9.0>-<246.0,20.0>-<225.5,40.0>> = 13.172553423326871

	* Aacute (U+00C1): L<<718.0,301.0>--<359.0,295.0>>/L<<359.0,295.0>--<718.0,295.0>> = 0.9575004843313389

	* Acircumflex (U+00C2): B<<205.0,96.0>-<205.0,126.0>-<223.0,163.0>>/L<<223.0,163.0>--<127.0,9.0>> = 5.996153426800191 

	* And 439 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* B (U+0042): L<<316.0,376.0>--<572.0,378.0>>

	* B (U+0042): L<<572.0,363.0>--<316.0,365.0>>

	* four (U+0034): L<<839.0,203.0>--<997.0,204.0>> 

	* And trademark (U+2122): L<<938.0,699.0>--<937.0,425.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[13] Kalnia-Color-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-Bold.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0308 (COMBINING DIAERESIS)


	- 0x0300 (COMBINING GRAVE ACCENT)


	- 0x0301 (COMBINING ACUTE ACCENT)


	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x0304 (COMBINING MACRON)


	- 0x0102 (LATIN CAPITAL LETTER A WITH BREVE)


	- 0x01CD (LATIN CAPITAL LETTER A WITH CARON)


	- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


	- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)


	- 0x0106 (LATIN CAPITAL LETTER C WITH ACUTE)
 

	- And 115 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender+abs(hhea.descender)+hhea.lineGap is 1141 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces">com.google.fonts/check/name/trailing_spaces</a>)</summary><div>


* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 10) has trailing spaces that must be removed: 'Kalnia is [...]dth axes. ' [code: trailing-space]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + b

	- b + f

	- f + h

	- h + i

	- i + j

	- j + k 

	- And k + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 4	Expected: 2

	- Glyph name: quotedbl	Contours detected: 4	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: percent	Contours detected: 9	Expected: 5

	- Glyph name: ampersand	Contours detected: 8	Expected: 1, 2 or 3

	- Glyph name: quotesingle	Contours detected: 2	Expected: 1

	- Glyph name: parenleft	Contours detected: 2	Expected: 1

	- Glyph name: parenright	Contours detected: 2	Expected: 1

	- Glyph name: asterisk	Contours detected: 7	Expected: 1 or 4 

	- And 393 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* dollar (U+0024): X=168.5,Y=2.0 (should be at baseline 0?)

	* dollar (U+0024): X=469.5,Y=2.0 (should be at baseline 0?)

	* three (U+0033): X=238.0,Y=706.0 (should be at cap-height 708?)

	* G (U+0047): X=516.5,Y=-1.0 (should be at baseline 0?)

	* G (U+0047): X=405.0,Y=1.0 (should be at baseline 0?)

	* G (U+0047): X=405.0,Y=1.0 (should be at baseline 0?)

	* J (U+004A): X=191.0,Y=1.0 (should be at baseline 0?)

	* a (U+0061): X=218.5,Y=502.0 (should be at x-height 500?)

	* a (U+0061): X=311.0,Y=501.0 (should be at x-height 500?)

	* a (U+0061): X=387.0,Y=498.5 (should be at x-height 500?) 

	* And 53 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Acircumflex (U+00C2): L<<359.0,857.0>--<504.0,785.0>> -> L<<504.0,785.0>--<508.0,783.0>>

	* C (U+0043): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Ccedilla (U+00C7): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Ecircumflex (U+00CA): L<<327.0,856.0>--<472.0,784.0>> -> L<<472.0,784.0>--<476.0,782.0>>

	* Euro (U+20AC): L<<655.0,522.0>--<701.0,414.0>> -> L<<701.0,414.0>--<704.0,407.0>>

	* Icircumflex (U+00CE): L<<142.0,857.0>--<287.0,785.0>> -> L<<287.0,785.0>--<291.0,783.0>>

	* Ocircumflex (U+00D4): L<<363.0,857.0>--<508.0,785.0>> -> L<<508.0,785.0>--<512.0,783.0>>

	* Scaron (U+0160): L<<394.0,802.0>--<249.0,874.0>> -> L<<249.0,874.0>--<245.0,876.0>>

	* Ucircumflex (U+00DB): L<<360.0,857.0>--<505.0,785.0>> -> L<<505.0,785.0>--<509.0,783.0>>

	* Y (U+0059): L<<496.0,20.0>--<495.0,277.0>> -> L<<495.0,277.0>--<495.0,337.0>> 

	* And 15 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* A (U+0041): L<<387.0,303.0>--<295.0,296.0>>/L<<295.0,296.0>--<387.0,296.0>> = 4.3510779515738935

	* Aacute (U+00C1): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Aacute (U+00C1): L<<387.0,303.0>--<295.0,296.0>>/L<<295.0,296.0>--<387.0,296.0>> = 4.3510779515738935

	* Acircumflex (U+00C2): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Acircumflex (U+00C2): L<<387.0,303.0>--<295.0,296.0>>/L<<295.0,296.0>--<387.0,296.0>> = 4.3510779515738935

	* Adieresis (U+00C4): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Adieresis (U+00C4): L<<387.0,303.0>--<295.0,296.0>>/L<<295.0,296.0>--<387.0,296.0>> = 4.3510779515738935

	* Agrave (U+00C0): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Agrave (U+00C0): L<<387.0,303.0>--<295.0,296.0>>/L<<295.0,296.0>--<387.0,296.0>> = 4.3510779515738935 

	* And 24 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* G (U+0047): L<<710.0,286.0>--<505.0,287.0>>

	* M (U+004D): L<<105.0,328.0>--<107.0,20.0>>

	* M (U+004D): L<<677.0,20.0>--<678.0,592.0>>

	* M (U+004D): L<<698.0,612.0>--<697.0,20.0>>

	* Y (U+0059): L<<496.0,20.0>--<495.0,277.0>>

	* Y (U+0059): L<<515.0,319.0>--<516.0,25.0>>

	* Yacute (U+00DD): L<<496.0,20.0>--<495.0,277.0>>

	* Yacute (U+00DD): L<<515.0,319.0>--<516.0,25.0>>

	* Ydieresis (U+0178): L<<496.0,20.0>--<495.0,277.0>>

	* Ydieresis (U+0178): L<<515.0,319.0>--<516.0,25.0>> 

	* And 15 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[14] Kalnia-Color-BoldExtended.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-BoldExtended.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0308 (COMBINING DIAERESIS)


	- 0x0300 (COMBINING GRAVE ACCENT)


	- 0x0301 (COMBINING ACUTE ACCENT)


	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x0304 (COMBINING MACRON)


	- 0x0102 (LATIN CAPITAL LETTER A WITH BREVE)


	- 0x01CD (LATIN CAPITAL LETTER A WITH CARON)


	- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


	- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)


	- 0x0106 (LATIN CAPITAL LETTER C WITH ACUTE)
 

	- And 115 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** The sum of hhea.ascender+abs(hhea.descender)+hhea.lineGap is 1141 when it should be at least 1200 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table records must not have trailing spaces. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces">com.google.fonts/check/name/trailing_spaces</a>)</summary><div>


* 🔥 **FAIL** Name table record with key = (3, 1, 1033, 10) has trailing spaces that must be removed: 'Kalnia is [...]dth axes. ' [code: trailing-space]
</div></details><details><summary>🔥 <b>FAIL:</b> Does full font name begin with the font family name? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/match_familyname_fullfont">com.google.fonts/check/name/match_familyname_fullfont</a>)</summary><div>


* 🔥 **FAIL** On the 'name' table, the full font name 'Kalnia-Color Bold Extended' does not begin with the font family name 'Kalnia-Color Extended' in platformID 3, encodingID 1, languageID 1033(0409), and nameID 1. [code: mismatch-font-names]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + b

	- b + f

	- f + h

	- h + i

	- i + j

	- j + k 

	- And k + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 4	Expected: 2

	- Glyph name: quotedbl	Contours detected: 4	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: percent	Contours detected: 9	Expected: 5

	- Glyph name: ampersand	Contours detected: 8	Expected: 1, 2 or 3

	- Glyph name: quotesingle	Contours detected: 2	Expected: 1

	- Glyph name: parenleft	Contours detected: 2	Expected: 1

	- Glyph name: parenright	Contours detected: 2	Expected: 1

	- Glyph name: asterisk	Contours detected: 7	Expected: 1 or 4 

	- And 393 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* exclam (U+0021): X=214.5,Y=-0.5 (should be at baseline 0?)

	* exclam (U+0021): X=482.0,Y=-0.5 (should be at baseline 0?)

	* dollar (U+0024): X=638.0,Y=1.0 (should be at baseline 0?)

	* dollar (U+0024): X=566.0,Y=709.0 (should be at cap-height 708?)

	* ampersand (U+0026): X=855.5,Y=709.5 (should be at cap-height 708?)

	* parenleft (U+0028): X=361.0,Y=708.5 (should be at cap-height 708?)

	* parenleft (U+0028): X=474.5,Y=-1.5 (should be at baseline 0?)

	* parenright (U+0029): X=559.0,Y=708.5 (should be at cap-height 708?)

	* parenright (U+0029): X=445.5,Y=-1.5 (should be at baseline 0?)

	* comma (U+002C): X=157.5,Y=-0.5 (should be at baseline 0?) 

	* And 84 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Aacute (U+00C1): L<<566.0,773.0>--<569.0,774.0>> -> L<<569.0,774.0>--<882.0,856.0>>

	* Acircumflex (U+00C2): L<<512.0,859.0>--<888.0,774.0>> -> L<<888.0,774.0>--<892.0,773.0>>

	* Agrave (U+00C0): L<<335.0,857.0>--<648.0,775.0>> -> L<<648.0,775.0>--<651.0,774.0>>

	* Eacute (U+00C9): L<<652.0,773.0>--<655.0,774.0>> -> L<<655.0,774.0>--<968.0,856.0>>

	* Ecircumflex (U+00CA): L<<576.0,858.0>--<952.0,773.0>> -> L<<952.0,773.0>--<956.0,772.0>>

	* Egrave (U+00C8): L<<360.0,856.0>--<673.0,774.0>> -> L<<673.0,774.0>--<676.0,773.0>>

	* Iacute (U+00CD): L<<276.0,773.0>--<279.0,774.0>> -> L<<279.0,774.0>--<592.0,856.0>>

	* Icircumflex (U+00CE): L<<205.0,859.0>--<581.0,774.0>> -> L<<581.0,774.0>--<585.0,773.0>>

	* Igrave (U+00CC): L<<70.0,856.0>--<383.0,774.0>> -> L<<383.0,774.0>--<386.0,773.0>>

	* Oacute (U+00D3): L<<636.0,773.0>--<639.0,774.0>> -> L<<639.0,774.0>--<952.0,856.0>> 

	* And 33 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): L<<581.0,303.0>--<489.0,296.0>>/L<<489.0,296.0>--<581.0,296.0>> = 4.3510779515738935

	* Aacute (U+00C1): L<<581.0,303.0>--<489.0,296.0>>/L<<489.0,296.0>--<581.0,296.0>> = 4.3510779515738935

	* Acircumflex (U+00C2): L<<581.0,303.0>--<489.0,296.0>>/L<<489.0,296.0>--<581.0,296.0>> = 4.3510779515738935

	* Adieresis (U+00C4): L<<581.0,303.0>--<489.0,296.0>>/L<<489.0,296.0>--<581.0,296.0>> = 4.3510779515738935

	* Agrave (U+00C0): L<<581.0,303.0>--<489.0,296.0>>/L<<489.0,296.0>--<581.0,296.0>> = 4.3510779515738935

	* Aring (U+00C5): L<<581.0,303.0>--<489.0,296.0>>/L<<489.0,296.0>--<581.0,296.0>> = 4.3510779515738935

	* Atilde (U+00C3): L<<581.0,303.0>--<489.0,296.0>>/L<<489.0,296.0>--<581.0,296.0>> = 4.3510779515738935

	* C (U+0043): B<<910.0,25.0>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Ccedilla (U+00C7): B<<667.5,-168.0>-<627.0,-186.0>-<568.0,-191.0>>/B<<568.0,-191.0>-<594.0,-192.0>-<622.5,-192.5>> = 7.046598536846509

	* Ccedilla (U+00C7): B<<910.0,25.0>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508 

	* And 34 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<1188.0,15.0>--<1343.0,16.0>>

	* AE (U+00C6): L<<1343.0,692.0>--<1188.0,693.0>>

	* E (U+0045): L<<590.0,15.0>--<745.0,16.0>>

	* E (U+0045): L<<745.0,692.0>--<590.0,693.0>>

	* Eacute (U+00C9): L<<590.0,15.0>--<745.0,16.0>>

	* Eacute (U+00C9): L<<745.0,692.0>--<590.0,693.0>>

	* Ecircumflex (U+00CA): L<<590.0,15.0>--<745.0,16.0>>

	* Ecircumflex (U+00CA): L<<745.0,692.0>--<590.0,693.0>>

	* Edieresis (U+00CB): L<<590.0,15.0>--<745.0,16.0>>

	* Edieresis (U+00CB): L<<745.0,692.0>--<590.0,693.0>> 

	* And 17 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 34 | 68 | 996 | 57 | 620 | 0 |
| 0% | 2% | 4% | 56% | 3% | 35% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
