## Fontbakery report

Fontbakery version: 0.8.9

<details><summary><b>[7] KalniaExtended-Bold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fi (U+FB01): L<<580.0,500.0>--<697.0,495.0>> -> L<<697.0,495.0>--<1318.0,515.0>>

	* g (U+0067): L<<511.0,110.0>--<473.0,84.0>> -> L<<473.0,84.0>--<457.0,73.0>>

	* gbreve (U+011F): L<<511.0,110.0>--<473.0,84.0>> -> L<<473.0,84.0>--<457.0,73.0>>

	* gdotaccent (U+0121): L<<511.0,110.0>--<473.0,84.0>> -> L<<473.0,84.0>--<457.0,73.0>> 

	* And uni0123 (U+0123): L<<511.0,110.0>--<473.0,84.0>> -> L<<473.0,84.0>--<457.0,73.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* C (U+0043): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Cacute (U+0106): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Ccaron (U+010C): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Ccedilla (U+00C7): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Cdotaccent (U+010A): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Euro (U+20AC): B<<987.0,24.5>-<1092.0,42.0>-<1184.0,83.0>>/B<<1184.0,83.0>-<1115.0,71.0>-<1041.0,71.0>> = 14.154439854180508

	* U (U+0055): B<<941.5,43.0>-<1027.0,64.0>-<1081.0,104.0>>/B<<1081.0,104.0>-<1038.0,82.0>-<980.5,70.5>> = 9.433302873233353

	* Uacute (U+00DA): B<<941.5,43.0>-<1027.0,64.0>-<1081.0,104.0>>/B<<1081.0,104.0>-<1038.0,82.0>-<980.5,70.5>> = 9.433302873233353

	* Ubreve (U+016C): B<<941.5,43.0>-<1027.0,64.0>-<1081.0,104.0>>/B<<1081.0,104.0>-<1038.0,82.0>-<980.5,70.5>> = 9.433302873233353

	* Ucircumflex (U+00DB): B<<941.5,43.0>-<1027.0,64.0>-<1081.0,104.0>>/B<<1081.0,104.0>-<1038.0,82.0>-<980.5,70.5>> = 9.433302873233353 

	* And 37 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[9] KalniaExtended-Medium.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
 FONT_FAMILY_NAME = 'Kalnia Extended Medium' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fi (U+FB01): L<<442.0,500.0>--<623.0,492.0>> -> L<<623.0,492.0>--<1086.0,515.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* AE (U+00C6): B<<1518.0,110.0>-<1480.0,30.0>-<1390.0,14.0>>/L<<1390.0,14.0>--<1632.0,14.0>> = 10.08059798754231

	* AE (U+00C6): L<<1632.0,694.0>--<1374.0,694.0>>/B<<1374.0,694.0>-<1460.0,680.0>-<1499.0,608.0>> = 9.24611274556323

	* Aacute (U+00C1): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Abreve (U+0102): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Acircumflex (U+00C2): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Adieresis (U+00C4): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Agrave (U+00C0): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Amacron (U+0100): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Aogonek (U+0104): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491 

	* And 190 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* four (U+0034): L<<973.0,201.0>--<1107.0,202.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[8] KalniaExtended-ExtraLight.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
 FONT_FAMILY_NAME = 'Kalnia Extended ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<190.0,72.0>-<190.0,97.0>-<209.0,131.0>>/L<<209.0,131.0>--<134.0,7.0>> = 1.9696866000377569

	* A (U+0041): L<<134.0,7.0>--<268.0,7.0>>/B<<268.0,7.0>-<228.0,14.0>-<209.0,29.0>> = 9.926245506651705

	* AE (U+00C6): B<<1346.5,30.5>-<1331.0,10.0>-<1291.0,9.0>>/L<<1291.0,9.0>--<1395.0,9.0>> = 1.4320961841645452

	* AE (U+00C6): L<<130.0,7.0>--<273.0,7.0>>/B<<273.0,7.0>-<237.0,9.0>-<218.5,24.5>> = 3.1798301198641643

	* AE (U+00C6): L<<1355.0,621.0>--<1360.0,487.0>>/L<<1360.0,487.0>--<1395.0,699.0>> = 11.51155787464854

	* AE (U+00C6): L<<1395.0,699.0>--<1274.0,699.0>>/B<<1274.0,699.0>-<1316.0,698.0>-<1335.0,679.5>> = 1.3639275316029233

	* AE (U+00C6): L<<1395.0,9.0>--<1360.0,238.0>>/L<<1360.0,238.0>--<1362.0,96.0>> = 7.882820834037182

	* Aacute (U+00C1): B<<190.0,72.0>-<190.0,97.0>-<209.0,131.0>>/L<<209.0,131.0>--<134.0,7.0>> = 1.9696866000377569

	* Aacute (U+00C1): L<<134.0,7.0>--<268.0,7.0>>/B<<268.0,7.0>-<228.0,14.0>-<209.0,29.0>> = 9.926245506651705

	* Abreve (U+0102): B<<190.0,72.0>-<190.0,97.0>-<209.0,131.0>>/L<<209.0,131.0>--<134.0,7.0>> = 1.9696866000377569 

	* And 611 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<1354.0,97.0>--<1353.0,248.0>>

	* B (U+0042): L<<557.0,362.0>--<267.0,364.0>>

	* OE (U+0152): L<<1537.0,97.0>--<1536.0,248.0>>

	* OE (U+0152): L<<1544.0,238.0>--<1545.0,96.0>>

	* four (U+0034): L<<784.0,203.0>--<951.0,204.0>>

	* four (U+0034): L<<83.0,198.0>--<711.0,202.0>> 

	* And seven (U+0037): L<<101.0,708.0>--<100.0,588.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] KalniaExtended-SemiBold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
 FONT_FAMILY_NAME = 'Kalnia Extended SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Y (U+0059): L<<889.0,17.0>--<889.0,286.0>> -> L<<889.0,286.0>--<893.0,327.0>>

	* Yacute (U+00DD): L<<889.0,17.0>--<889.0,286.0>> -> L<<889.0,286.0>--<893.0,327.0>>

	* Ycircumflex (U+0176): L<<889.0,17.0>--<889.0,286.0>> -> L<<889.0,286.0>--<893.0,327.0>>

	* Ydieresis (U+0178): L<<889.0,17.0>--<889.0,286.0>> -> L<<889.0,286.0>--<893.0,327.0>>

	* Ygrave (U+1EF2): L<<889.0,17.0>--<889.0,286.0>> -> L<<889.0,286.0>--<893.0,327.0>>

	* fi (U+FB01): L<<514.0,500.0>--<662.0,494.0>> -> L<<662.0,494.0>--<1208.0,515.0>> 

	* And yen (U+00A5): L<<889.0,277.0>--<889.0,286.0>> -> L<<889.0,286.0>--<893.0,327.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* AE (U+00C6): B<<1597.0,117.0>-<1538.0,40.0>-<1439.0,17.0>>/L<<1439.0,17.0>--<1750.0,17.0>> = 13.079123780066805

	* AE (U+00C6): L<<1750.0,691.0>--<1424.0,691.0>>/B<<1424.0,691.0>-<1513.0,671.0>-<1572.0,602.0>> = 12.665063765042364

	* C (U+0043): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* Cacute (U+0106): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* Ccaron (U+010C): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* Ccedilla (U+00C7): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* Cdotaccent (U+010A): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* E (U+0045): B<<1039.0,117.0>-<980.0,40.0>-<882.0,17.0>>/L<<882.0,17.0>--<1192.0,17.0>> = 13.207928462779101

	* E (U+0045): L<<1192.0,691.0>--<866.0,691.0>>/B<<866.0,691.0>-<955.0,671.0>-<1014.0,602.0>> = 12.665063765042364

	* Eacute (U+00C9): B<<1039.0,117.0>-<980.0,40.0>-<882.0,17.0>>/L<<882.0,17.0>--<1192.0,17.0>> = 13.207928462779101 

	* And 100 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* B (U+0042): L<<632.0,366.0>--<515.0,367.0>> 

	* And M (U+004D): L<<1415.0,687.0>--<1014.0,685.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] Kalnia-Color-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-ExtraLight.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
 FONT_FAMILY_NAME = 'Kalnia-Color ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* AE (U+00C6): B<<845.5,29.5>-<832.0,11.0>-<795.0,9.0>>/L<<795.0,9.0>--<874.0,9.0>> = 3.094058058917113

	* AE (U+00C6): L<<672.0,359.0>--<687.0,287.0>>/L<<687.0,287.0>--<687.0,393.0>> = 11.768288932020628

	* AE (U+00C6): L<<847.0,631.0>--<843.0,490.0>>/L<<843.0,490.0>--<874.0,699.0>> = 6.811927773881065

	* AE (U+00C6): L<<874.0,699.0>--<779.0,699.0>>/B<<779.0,699.0>-<817.0,698.0>-<832.5,682.5>> = 1.5074357587748821

	* AE (U+00C6): L<<874.0,9.0>--<842.0,234.0>>/L<<842.0,234.0>--<855.0,89.0>> = 2.9712829451437766

	* Aacute (U+00C1): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* Abreve (U+0102): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* Acircumflex (U+00C2): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* Adieresis (U+00C4): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424 

	* And 566 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* T (U+0054): L<<86.0,469.0>--<85.0,586.0>>

	* Tcaron (U+0164): L<<86.0,469.0>--<85.0,586.0>>

	* seven (U+0037): L<<81.0,708.0>--<80.0,588.0>> 

	* And uni021A (U+021A): L<<86.0,469.0>--<85.0,586.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[7] Kalnia-Color-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-Light.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* AE (U+00C6): B<<849.5,32.5>-<835.0,13.0>-<800.0,10.0>>/L<<800.0,10.0>--<887.0,10.0>> = 4.899092453787774

	* AE (U+00C6): L<<852.0,629.0>--<856.0,489.0>>/L<<856.0,489.0>--<887.0,698.0>> = 10.073481173022614

	* AE (U+00C6): L<<887.0,10.0>--<855.0,233.0>>/L<<855.0,233.0>--<863.0,93.0>> = 4.895581645025753

	* AE (U+00C6): L<<887.0,698.0>--<785.0,698.0>>/B<<785.0,698.0>-<821.0,695.0>-<836.5,679.5>> = 4.763641690726143

	* Aacute (U+00C1): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Abreve (U+0102): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Acircumflex (U+00C2): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Adieresis (U+00C4): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Agrave (U+00C0): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688 

	* And 492 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[8] Kalnia-Color-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-Regular.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* cent (U+00A2): L<<324.0,541.0>--<324.0,541.0>> -> L<<324.0,541.0>--<324.0,541.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* AE (U+00C6): B<<860.0,41.5>-<844.0,20.0>-<812.0,13.0>>/L<<812.0,13.0>--<918.0,13.0>> = 12.33908727832618

	* AE (U+00C6): L<<918.0,13.0>--<888.0,230.0>>/L<<888.0,230.0>--<881.0,104.0>> = 11.051012056695225

	* AE (U+00C6): L<<918.0,695.0>--<799.0,695.0>>/B<<799.0,695.0>-<830.0,689.0>-<845.5,673.0>> = 10.954062643398332

	* Aacute (U+00C1): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Abreve (U+0102): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Abreve (U+0102): B<<379.0,862.0>-<388.0,862.0>-<400.0,916.0>>/L<<400.0,916.0>--<398.0,906.0>> = 1.2188752351313326

	* Abreve (U+0102): L<<360.0,906.0>--<358.0,916.0>>/B<<358.0,916.0>-<370.0,862.0>-<379.0,862.0>> = 1.2188752351313326

	* Acircumflex (U+00C2): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Adieresis (U+00C4): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386 

	* And 289 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[8] Kalnia-Color-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-Medium.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Euro (U+20AC): L<<142.0,394.0>--<255.0,394.0>> -> L<<255.0,394.0>--<255.0,394.0>> 

	* And Euro (U+20AC): L<<270.0,394.0>--<270.0,394.0>> -> L<<270.0,394.0>--<535.0,394.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<158.0,148.0>-<158.0,182.0>-<169.0,227.0>>/L<<169.0,227.0>--<82.0,14.0>> = 8.48132596389569

	* Aacute (U+00C1): B<<158.0,148.0>-<158.0,182.0>-<169.0,227.0>>/L<<169.0,227.0>--<82.0,14.0>> = 8.48132596389569

	* Abreve (U+0102): B<<158.0,148.0>-<158.0,182.0>-<169.0,227.0>>/L<<169.0,227.0>--<82.0,14.0>> = 8.48132596389569

	* Acircumflex (U+00C2): B<<158.0,148.0>-<158.0,182.0>-<169.0,227.0>>/L<<169.0,227.0>--<82.0,14.0>> = 8.48132596389569

	* Adieresis (U+00C4): B<<158.0,148.0>-<158.0,182.0>-<169.0,227.0>>/L<<169.0,227.0>--<82.0,14.0>> = 8.48132596389569

	* Agrave (U+00C0): B<<158.0,148.0>-<158.0,182.0>-<169.0,227.0>>/L<<169.0,227.0>--<82.0,14.0>> = 8.48132596389569

	* Amacron (U+0100): B<<158.0,148.0>-<158.0,182.0>-<169.0,227.0>>/L<<169.0,227.0>--<82.0,14.0>> = 8.48132596389569

	* Aogonek (U+0104): B<<158.0,148.0>-<158.0,182.0>-<169.0,227.0>>/L<<169.0,227.0>--<82.0,14.0>> = 8.48132596389569

	* Aring (U+00C5): B<<158.0,148.0>-<158.0,182.0>-<169.0,227.0>>/L<<169.0,227.0>--<82.0,14.0>> = 8.48132596389569

	* Atilde (U+00C3): B<<158.0,148.0>-<158.0,182.0>-<169.0,227.0>>/L<<169.0,227.0>--<82.0,14.0>> = 8.48132596389569 

	* And 147 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[8] KalniaExtended-Light.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
 FONT_FAMILY_NAME = 'Kalnia Extended Light' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<199.0,88.0>-<199.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 4.360204305907731

	* A (U+0041): L<<129.0,8.0>--<284.0,8.0>>/B<<284.0,8.0>-<240.0,18.0>-<219.5,36.5>> = 12.80426606528674

	* AE (U+00C6): B<<1371.0,33.5>-<1352.0,13.0>-<1311.0,10.0>>/L<<1311.0,10.0>--<1443.0,10.0>> = 4.184916125118406

	* AE (U+00C6): L<<126.0,8.0>--<291.0,8.0>>/B<<291.0,8.0>-<253.0,12.0>-<234.0,29.5>> = 6.009005957494474

	* AE (U+00C6): L<<1443.0,10.0>--<1405.0,239.0>>/L<<1405.0,239.0>--<1393.0,99.0>> = 14.320836921067032

	* AE (U+00C6): L<<1443.0,698.0>--<1294.0,698.0>>/B<<1294.0,698.0>-<1337.0,696.0>-<1358.0,677.0>> = 2.663000766067037

	* Aacute (U+00C1): B<<199.0,88.0>-<199.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 4.360204305907731

	* Aacute (U+00C1): L<<129.0,8.0>--<284.0,8.0>>/B<<284.0,8.0>-<240.0,18.0>-<219.5,36.5>> = 12.80426606528674

	* Abreve (U+0102): B<<199.0,88.0>-<199.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 4.360204305907731

	* Abreve (U+0102): L<<129.0,8.0>--<284.0,8.0>>/B<<284.0,8.0>-<240.0,18.0>-<219.5,36.5>> = 12.80426606528674 

	* And 526 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* four (U+0034): L<<822.0,203.0>--<982.0,204.0>>

	* four (U+0034): L<<83.0,196.0>--<704.0,201.0>> 

	* And seven (U+0037): L<<97.0,708.0>--<96.0,586.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[8] KalniaExtended-Thin.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* M (U+004D): L<<1065.0,682.0>--<1059.0,673.0>> -> L<<1059.0,673.0>--<1032.0,629.0>>

	* four (U+0034): L<<720.0,204.0>--<720.0,546.0>> -> L<<720.0,546.0>--<725.0,724.0>>

	* four (U+0034): L<<730.0,716.0>--<725.0,546.0>> -> L<<725.0,546.0>--<725.0,8.0>>

	* onequarter (U+00BC): L<<566.0,93.0>--<566.0,230.0>> -> L<<566.0,230.0>--<567.0,302.0>>

	* t (U+0074): L<<182.0,640.0>--<178.0,490.0>> -> L<<178.0,490.0>--<178.0,61.0>>

	* tcaron (U+0165): L<<182.0,640.0>--<178.0,490.0>> -> L<<178.0,490.0>--<178.0,61.0>>

	* threequarters (U+00BE): L<<697.0,93.0>--<697.0,230.0>> -> L<<697.0,230.0>--<698.0,302.0>>

	* uni021B (U+021B): L<<182.0,640.0>--<178.0,490.0>> -> L<<178.0,490.0>--<178.0,61.0>> 

	* And uni2074 (U+2074): L<<293.0,509.0>--<293.0,646.0>> -> L<<293.0,646.0>--<294.0,718.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<178.0,50.0>-<178.0,68.0>-<190.0,91.0>>/L<<190.0,91.0>--<141.0,5.0>> = 2.12027053535989

	* A (U+0041): L<<141.0,5.0>--<247.0,5.0>>/B<<247.0,5.0>-<178.0,14.0>-<178.0,50.0>> = 7.431407971172489

	* AE (U+00C6): L<<1000.0,360.0>--<1004.0,288.0>>/L<<1004.0,288.0>--<1004.0,388.0>> = 3.1798301198641643

	* AE (U+00C6): L<<1004.0,288.0>--<1004.0,388.0>>/B<<1004.0,388.0>-<1003.0,381.0>-<1002.0,374.0>> = 8.13010235415596

	* AE (U+00C6): L<<1317.0,624.0>--<1302.0,491.0>>/L<<1302.0,491.0>--<1334.0,701.0>> = 2.2293962820711486

	* AE (U+00C6): L<<1334.0,7.0>--<1302.0,236.0>>/L<<1302.0,236.0>--<1321.0,92.0>> = 0.4384447329817478

	* Aacute (U+00C1): B<<178.0,50.0>-<178.0,68.0>-<190.0,91.0>>/L<<190.0,91.0>--<141.0,5.0>> = 2.12027053535989

	* Aacute (U+00C1): L<<141.0,5.0>--<247.0,5.0>>/B<<247.0,5.0>-<178.0,14.0>-<178.0,50.0>> = 7.431407971172489

	* Abreve (U+0102): B<<178.0,50.0>-<178.0,68.0>-<190.0,91.0>>/L<<190.0,91.0>--<141.0,5.0>> = 2.12027053535989

	* Abreve (U+0102): L<<141.0,5.0>--<247.0,5.0>>/B<<247.0,5.0>-<178.0,14.0>-<178.0,50.0>> = 7.431407971172489 

	* And 594 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* H (U+0048): L<<225.0,342.0>--<945.0,348.0>>

	* Hbar (U+0126): L<<225.0,342.0>--<945.0,348.0>>

	* ae (U+00E6): L<<785.0,286.0>--<1545.0,290.0>>

	* e (U+0065): L<<83.0,286.0>--<843.0,290.0>>

	* eacute (U+00E9): L<<83.0,286.0>--<843.0,290.0>>

	* ecaron (U+011B): L<<83.0,286.0>--<843.0,290.0>>

	* ecircumflex (U+00EA): L<<83.0,286.0>--<843.0,290.0>>

	* edieresis (U+00EB): L<<83.0,286.0>--<843.0,290.0>>

	* edotaccent (U+0117): L<<83.0,286.0>--<843.0,290.0>>

	* egrave (U+00E8): L<<83.0,286.0>--<843.0,290.0>> 

	* And 6 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[7] KalniaExtended-Regular.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fi (U+FB01): L<<398.0,500.0>--<599.0,492.0>> -> L<<599.0,492.0>--<1013.0,515.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* AE (U+00C6): B<<1431.5,41.0>-<1405.0,19.0>-<1360.0,13.0>>/L<<1360.0,13.0>--<1561.0,13.0>> = 7.594643368591447

	* AE (U+00C6): L<<115.0,12.0>--<335.0,12.0>>/B<<335.0,12.0>-<296.0,20.0>-<274.0,42.5>> = 11.592175410291041

	* AE (U+00C6): L<<1561.0,695.0>--<1344.0,695.0>>/B<<1344.0,695.0>-<1428.0,685.0>-<1456.0,612.0>> = 6.788974574438767

	* Aacute (U+00C1): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Abreve (U+0102): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Acircumflex (U+00C2): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Adieresis (U+00C4): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Agrave (U+00C0): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Amacron (U+0100): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657 

	* And 320 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[10] Kalnia-Color-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-Thin.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* ampersand (U+0026): X=640.5,Y=1.5 (should be at baseline 0?)

	* comma (U+002C): X=68.0,Y=-2.0 (should be at baseline 0?)

	* two (U+0032): X=87.5,Y=-2.0 (should be at baseline 0?)

	* two (U+0032): X=202.0,Y=706.0 (should be at cap-height 708?)

	* two (U+0032): X=232.0,Y=706.0 (should be at cap-height 708?)

	* two (U+0032): X=232.0,Y=706.0 (should be at cap-height 708?)

	* three (U+0033): X=192.0,Y=2.0 (should be at baseline 0?)

	* three (U+0033): X=195.0,Y=706.0 (should be at cap-height 708?)

	* five (U+0035): X=207.0,Y=2.0 (should be at baseline 0?)

	* seven (U+0037): X=544.5,Y=706.0 (should be at cap-height 708?) 

	* And 90 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* M (U+004D): L<<785.0,682.0>--<780.0,672.0>> -> L<<780.0,672.0>--<755.0,617.0>>

	* four (U+0034): L<<410.0,204.0>--<410.0,546.0>> -> L<<410.0,546.0>--<415.0,724.0>>

	* four (U+0034): L<<420.0,716.0>--<415.0,546.0>> -> L<<415.0,546.0>--<415.0,8.0>>

	* onequarter (U+00BC): L<<392.0,93.0>--<392.0,230.0>> -> L<<392.0,230.0>--<395.0,302.0>>

	* t (U+0074): L<<114.0,640.0>--<110.0,490.0>> -> L<<110.0,490.0>--<110.0,61.0>>

	* tcaron (U+0165): L<<114.0,640.0>--<110.0,490.0>> -> L<<110.0,490.0>--<110.0,61.0>>

	* threequarters (U+00BE): L<<502.0,93.0>--<502.0,230.0>> -> L<<502.0,230.0>--<505.0,302.0>>

	* uni021B (U+021B): L<<114.0,640.0>--<110.0,490.0>> -> L<<110.0,490.0>--<110.0,61.0>> 

	* And uni2074 (U+2074): L<<171.0,509.0>--<171.0,646.0>> -> L<<171.0,646.0>--<174.0,718.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* AE (U+00C6): L<<664.0,360.0>--<668.0,288.0>>/L<<668.0,288.0>--<668.0,388.0>> = 3.1798301198641643

	* AE (U+00C6): L<<668.0,288.0>--<668.0,388.0>>/B<<668.0,388.0>-<667.0,381.0>-<666.0,374.0>> = 8.13010235415596

	* AE (U+00C6): L<<840.0,634.0>--<826.0,491.0>>/L<<826.0,491.0>--<858.0,701.0>> = 3.072577677350764

	* AE (U+00C6): L<<858.0,7.0>--<825.0,236.0>>/L<<825.0,236.0>--<846.0,84.0>> = 0.33407768660106585

	* AE (U+00C6): L<<90.0,5.0>--<168.0,5.0>>/B<<168.0,5.0>-<121.0,14.0>-<121.0,50.0>> = 10.840305454330565

	* Aacute (U+00C1): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* Abreve (U+0102): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* Acircumflex (U+00C2): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* Adieresis (U+00C4): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792 

	* And 579 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* seven (U+0037): L<<85.0,708.0>--<84.0,592.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[8] Kalnia-Color-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-Bold.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* C (U+0043): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Cacute (U+0106): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Ccaron (U+010C): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Ccedilla (U+00C7): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Cdotaccent (U+010A): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Euro (U+20AC): L<<655.0,522.0>--<701.0,414.0>> -> L<<701.0,414.0>--<704.0,407.0>>

	* ampersand (U+0026): L<<440.0,164.0>--<439.0,165.0>> -> L<<439.0,165.0>--<232.0,380.0>>

	* g (U+0067): L<<193.0,113.0>--<148.0,82.0>> -> L<<148.0,82.0>--<133.0,71.0>>

	* gbreve (U+011F): L<<193.0,113.0>--<148.0,82.0>> -> L<<148.0,82.0>--<133.0,71.0>>

	* gdotaccent (U+0121): L<<193.0,113.0>--<148.0,82.0>> -> L<<148.0,82.0>--<133.0,71.0>> 

	* And uni0123 (U+0123): L<<193.0,113.0>--<148.0,82.0>> -> L<<148.0,82.0>--<133.0,71.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<198.0,297.0>-<199.0,308.0>-<201.0,320.0>>/L<<201.0,320.0>--<191.0,297.0>> = 14.036243467926457

	* Aacute (U+00C1): B<<198.0,297.0>-<199.0,308.0>-<201.0,320.0>>/L<<201.0,320.0>--<191.0,297.0>> = 14.036243467926457

	* Abreve (U+0102): B<<198.0,297.0>-<199.0,308.0>-<201.0,320.0>>/L<<201.0,320.0>--<191.0,297.0>> = 14.036243467926457

	* Acircumflex (U+00C2): B<<198.0,297.0>-<199.0,308.0>-<201.0,320.0>>/L<<201.0,320.0>--<191.0,297.0>> = 14.036243467926457

	* Adieresis (U+00C4): B<<198.0,297.0>-<199.0,308.0>-<201.0,320.0>>/L<<201.0,320.0>--<191.0,297.0>> = 14.036243467926457

	* Agrave (U+00C0): B<<198.0,297.0>-<199.0,308.0>-<201.0,320.0>>/L<<201.0,320.0>--<191.0,297.0>> = 14.036243467926457

	* Amacron (U+0100): B<<198.0,297.0>-<199.0,308.0>-<201.0,320.0>>/L<<201.0,320.0>--<191.0,297.0>> = 14.036243467926457

	* Aogonek (U+0104): B<<198.0,297.0>-<199.0,308.0>-<201.0,320.0>>/L<<201.0,320.0>--<191.0,297.0>> = 14.036243467926457

	* Aring (U+00C5): B<<198.0,297.0>-<199.0,308.0>-<201.0,320.0>>/L<<201.0,320.0>--<191.0,297.0>> = 14.036243467926457

	* Atilde (U+00C3): B<<198.0,297.0>-<199.0,308.0>-<201.0,320.0>>/L<<201.0,320.0>--<191.0,297.0>> = 14.036243467926457 

	* And 26 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[9] Kalnia-Color-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


* 🔥 **FAIL** Style name used in "fonts/ttf/Kalnia-Color-SemiBold.ttf" is not canonical. You should rebuild the font using any of the following style names: "Thin", "ExtraLight", "Light", "Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black", "Thin Italic", "ExtraLight Italic", "Light Italic", "Italic", "Medium Italic", "SemiBold Italic", "Bold Italic", "ExtraBold Italic", "Black Italic". [code: bad-static-filename]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
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
 FONT_FAMILY_NAME = 'Kalnia-Color SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- a.color1

	- O.color1

	- AE.color1

	- b.color1

	- dotlessi.color0

	- z.color1

	- s.color0

	- G.color0

	- E.color1

	- comma.color1 

	- And 130 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 4	Expected: 1, 3 or 5

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: zero	Contours detected: 4	Expected: 2 or 3

	- Glyph name: one	Contours detected: 2	Expected: 1

	- Glyph name: two	Contours detected: 5	Expected: 1

	- Glyph name: three	Contours detected: 5	Expected: 1

	- Glyph name: four	Contours detected: 3	Expected: 1 or 2 

	- And 490 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Euro (U+20AC): L<<660.0,522.0>--<693.0,409.0>> -> L<<693.0,409.0>--<695.0,404.0>>

	* Y (U+0059): L<<459.0,17.0>--<459.0,283.0>> -> L<<459.0,283.0>--<461.0,335.0>>

	* Yacute (U+00DD): L<<459.0,17.0>--<459.0,283.0>> -> L<<459.0,283.0>--<461.0,335.0>>

	* Ycircumflex (U+0176): L<<459.0,17.0>--<459.0,283.0>> -> L<<459.0,283.0>--<461.0,335.0>>

	* Ydieresis (U+0178): L<<459.0,17.0>--<459.0,283.0>> -> L<<459.0,283.0>--<461.0,335.0>>

	* Ygrave (U+1EF2): L<<459.0,17.0>--<459.0,283.0>> -> L<<459.0,283.0>--<461.0,335.0>>

	* g (U+0067): L<<175.0,110.0>--<135.0,81.0>> -> L<<135.0,81.0>--<123.0,71.0>>

	* gbreve (U+011F): L<<175.0,110.0>--<135.0,81.0>> -> L<<135.0,81.0>--<123.0,71.0>>

	* gdotaccent (U+0121): L<<175.0,110.0>--<135.0,81.0>> -> L<<135.0,81.0>--<123.0,71.0>>

	* uni0123 (U+0123): L<<175.0,110.0>--<135.0,81.0>> -> L<<135.0,81.0>--<123.0,71.0>> 

	* And 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<176.0,187.0>-<176.0,226.0>-<186.0,276.0>>/L<<186.0,276.0>--<79.0,17.0>> = 11.136928999068989

	* Aacute (U+00C1): B<<176.0,187.0>-<176.0,226.0>-<186.0,276.0>>/L<<186.0,276.0>--<79.0,17.0>> = 11.136928999068989

	* Abreve (U+0102): B<<176.0,187.0>-<176.0,226.0>-<186.0,276.0>>/L<<186.0,276.0>--<79.0,17.0>> = 11.136928999068989

	* Acircumflex (U+00C2): B<<176.0,187.0>-<176.0,226.0>-<186.0,276.0>>/L<<186.0,276.0>--<79.0,17.0>> = 11.136928999068989

	* Adieresis (U+00C4): B<<176.0,187.0>-<176.0,226.0>-<186.0,276.0>>/L<<186.0,276.0>--<79.0,17.0>> = 11.136928999068989

	* Agrave (U+00C0): B<<176.0,187.0>-<176.0,226.0>-<186.0,276.0>>/L<<186.0,276.0>--<79.0,17.0>> = 11.136928999068989

	* Amacron (U+0100): B<<176.0,187.0>-<176.0,226.0>-<186.0,276.0>>/L<<186.0,276.0>--<79.0,17.0>> = 11.136928999068989

	* Aogonek (U+0104): B<<176.0,187.0>-<176.0,226.0>-<186.0,276.0>>/L<<186.0,276.0>--<79.0,17.0>> = 11.136928999068989

	* Aring (U+00C5): B<<176.0,187.0>-<176.0,226.0>-<186.0,276.0>>/L<<186.0,276.0>--<79.0,17.0>> = 11.136928999068989

	* Atilde (U+00C3): B<<176.0,187.0>-<176.0,226.0>-<186.0,276.0>>/L<<186.0,276.0>--<79.0,17.0>> = 11.136928999068989 

	* And 58 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 7 | 108 | 1647 | 92 | 1241 | 0 |
| 0% | 0% | 3% | 53% | 3% | 40% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
