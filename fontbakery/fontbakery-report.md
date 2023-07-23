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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 5	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fi (U+FB01): L<<580.0,500.0>--<697.0,495.0>> -> L<<697.0,495.0>--<1318.0,515.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* C (U+0043): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Cacute (U+0106): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Ccaron (U+010C): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Ccedilla (U+00C7): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Cdotaccent (U+010A): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Euro (U+20AC): B<<987.0,24.5>-<1092.0,42.0>-<1184.0,83.0>>/B<<1184.0,83.0>-<1115.0,71.0>-<1041.0,71.0>> = 14.154439854180508

	* a (U+0061): B<<467.0,20.0>-<540.0,33.0>-<578.0,58.0>>/B<<578.0,58.0>-<568.0,53.0>-<558.0,53.0>> = 6.775656169398931

	* aacute (U+00E1): B<<467.0,20.0>-<540.0,33.0>-<578.0,58.0>>/B<<578.0,58.0>-<568.0,53.0>-<558.0,53.0>> = 6.775656169398931

	* abreve (U+0103): B<<467.0,20.0>-<540.0,33.0>-<578.0,58.0>>/B<<578.0,58.0>-<568.0,53.0>-<558.0,53.0>> = 6.775656169398931

	* acircumflex (U+00E2): B<<467.0,20.0>-<540.0,33.0>-<578.0,58.0>>/B<<578.0,58.0>-<568.0,53.0>-<558.0,53.0>> = 6.775656169398931 

	* And 16 more.

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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fi (U+FB01): L<<442.0,500.0>--<623.0,492.0>> -> L<<623.0,492.0>--<1086.0,515.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Aacute (U+00C1): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Abreve (U+0102): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Acircumflex (U+00C2): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Adieresis (U+00C4): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Agrave (U+00C0): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Amacron (U+0100): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Aogonek (U+0104): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Aring (U+00C5): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491

	* Atilde (U+00C3): B<<236.0,154.0>-<236.0,192.0>-<253.0,240.0>>/L<<253.0,240.0>--<107.0,14.0>> = 13.360727038045491 

	* And 67 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* four (U+0034): L<<973.0,201.0>--<1107.0,202.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] KalniaExtended-ExtraLight.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* W (U+0057): L<<816.0,471.0>--<831.0,494.0>> -> L<<831.0,494.0>--<865.0,555.0>>

	* Wacute (U+1E82): L<<816.0,471.0>--<831.0,494.0>> -> L<<831.0,494.0>--<865.0,555.0>>

	* Wcircumflex (U+0174): L<<816.0,471.0>--<831.0,494.0>> -> L<<831.0,494.0>--<865.0,555.0>>

	* Wdieresis (U+1E84): L<<816.0,471.0>--<831.0,494.0>> -> L<<831.0,494.0>--<865.0,555.0>> 

	* And Wgrave (U+1E80): L<<816.0,471.0>--<831.0,494.0>> -> L<<831.0,494.0>--<865.0,555.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<190.0,72.0>-<190.0,97.0>-<209.0,131.0>>/L<<209.0,131.0>--<134.0,7.0>> = 1.9696866000377569

	* A (U+0041): L<<134.0,7.0>--<268.0,7.0>>/B<<268.0,7.0>-<228.0,14.0>-<209.0,29.0>> = 9.926245506651705

	* Aacute (U+00C1): B<<190.0,72.0>-<190.0,97.0>-<209.0,131.0>>/L<<209.0,131.0>--<134.0,7.0>> = 1.9696866000377569

	* Aacute (U+00C1): L<<134.0,7.0>--<268.0,7.0>>/B<<268.0,7.0>-<228.0,14.0>-<209.0,29.0>> = 9.926245506651705

	* Abreve (U+0102): B<<190.0,72.0>-<190.0,97.0>-<209.0,131.0>>/L<<209.0,131.0>--<134.0,7.0>> = 1.9696866000377569

	* Abreve (U+0102): L<<134.0,7.0>--<268.0,7.0>>/B<<268.0,7.0>-<228.0,14.0>-<209.0,29.0>> = 9.926245506651705

	* Acircumflex (U+00C2): B<<190.0,72.0>-<190.0,97.0>-<209.0,131.0>>/L<<209.0,131.0>--<134.0,7.0>> = 1.9696866000377569

	* Acircumflex (U+00C2): L<<134.0,7.0>--<268.0,7.0>>/B<<268.0,7.0>-<228.0,14.0>-<209.0,29.0>> = 9.926245506651705

	* Adieresis (U+00C4): B<<190.0,72.0>-<190.0,97.0>-<209.0,131.0>>/L<<209.0,131.0>--<134.0,7.0>> = 1.9696866000377569

	* Adieresis (U+00C4): L<<134.0,7.0>--<268.0,7.0>>/B<<268.0,7.0>-<228.0,14.0>-<209.0,29.0>> = 9.926245506651705 

	* And 160 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<1354.0,97.0>--<1353.0,248.0>>

	* B (U+0042): L<<557.0,362.0>--<267.0,364.0>>

	* OE (U+0152): L<<1537.0,97.0>--<1536.0,248.0>>

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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fi (U+FB01): L<<514.0,500.0>--<662.0,494.0>> -> L<<662.0,494.0>--<1208.0,515.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* C (U+0043): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* Cacute (U+0106): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* Ccaron (U+010C): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* Ccedilla (U+00C7): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* Cdotaccent (U+010A): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* E (U+0045): B<<1039.0,117.0>-<980.0,40.0>-<882.0,17.0>>/L<<882.0,17.0>--<1192.0,17.0>> = 13.207928462779101

	* E (U+0045): L<<1192.0,691.0>--<866.0,691.0>>/B<<866.0,691.0>-<955.0,671.0>-<1014.0,602.0>> = 12.665063765042364

	* Eacute (U+00C9): B<<1039.0,117.0>-<980.0,40.0>-<882.0,17.0>>/L<<882.0,17.0>--<1192.0,17.0>> = 13.207928462779101

	* Eacute (U+00C9): L<<1192.0,691.0>--<866.0,691.0>>/B<<866.0,691.0>-<955.0,671.0>-<1014.0,602.0>> = 12.665063765042364

	* Ecaron (U+011A): B<<1039.0,117.0>-<980.0,40.0>-<882.0,17.0>>/L<<882.0,17.0>--<1192.0,17.0>> = 13.207928462779101 

	* And 39 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* B (U+0042): L<<632.0,366.0>--<515.0,367.0>> [code: found-semi-vertical]
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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* Aacute (U+00C1): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* Abreve (U+0102): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* Acircumflex (U+00C2): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* Adieresis (U+00C4): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* Agrave (U+00C0): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* Amacron (U+0100): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* Aogonek (U+0104): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* Aring (U+00C5): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424

	* Atilde (U+00C3): B<<122.0,70.0>-<122.0,93.0>-<135.0,129.0>>/L<<135.0,129.0>--<88.0,7.0>> = 1.2137605626098424 

	* And 148 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* seven (U+0037): L<<81.0,708.0>--<80.0,588.0>> [code: found-semi-vertical]
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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Aacute (U+00C1): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Abreve (U+0102): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Acircumflex (U+00C2): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Adieresis (U+00C4): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Agrave (U+00C0): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Amacron (U+0100): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Aogonek (U+0104): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Aring (U+00C5): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688

	* Atilde (U+00C3): B<<129.0,86.0>-<129.0,111.0>-<142.0,148.0>>/L<<142.0,148.0>--<87.0,8.0>> = 2.088742151410688 

	* And 130 more.

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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* cent (U+00A2): L<<324.0,541.0>--<324.0,541.0>> -> L<<324.0,541.0>--<324.0,541.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Aacute (U+00C1): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Abreve (U+0102): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Abreve (U+0102): B<<379.0,862.0>-<388.0,862.0>-<400.0,916.0>>/L<<400.0,916.0>--<398.0,906.0>> = 1.2188752351313326

	* Abreve (U+0102): L<<360.0,906.0>--<358.0,916.0>>/B<<358.0,916.0>-<370.0,862.0>-<379.0,862.0>> = 1.2188752351313326

	* Acircumflex (U+00C2): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Adieresis (U+00C4): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Agrave (U+00C0): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Amacron (U+0100): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Aogonek (U+0104): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386 

	* And 111 more.

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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 184 more.

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

	* And 55 more.

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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<199.0,88.0>-<199.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 4.360204305907731

	* A (U+0041): L<<129.0,8.0>--<284.0,8.0>>/B<<284.0,8.0>-<240.0,18.0>-<219.5,36.5>> = 12.80426606528674

	* Aacute (U+00C1): B<<199.0,88.0>-<199.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 4.360204305907731

	* Aacute (U+00C1): L<<129.0,8.0>--<284.0,8.0>>/B<<284.0,8.0>-<240.0,18.0>-<219.5,36.5>> = 12.80426606528674

	* Abreve (U+0102): B<<199.0,88.0>-<199.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 4.360204305907731

	* Abreve (U+0102): L<<129.0,8.0>--<284.0,8.0>>/B<<284.0,8.0>-<240.0,18.0>-<219.5,36.5>> = 12.80426606528674

	* Acircumflex (U+00C2): B<<199.0,88.0>-<199.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 4.360204305907731

	* Acircumflex (U+00C2): L<<129.0,8.0>--<284.0,8.0>>/B<<284.0,8.0>-<240.0,18.0>-<219.5,36.5>> = 12.80426606528674

	* Adieresis (U+00C4): B<<199.0,88.0>-<199.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 4.360204305907731

	* Adieresis (U+00C4): L<<129.0,8.0>--<284.0,8.0>>/B<<284.0,8.0>-<240.0,18.0>-<219.5,36.5>> = 12.80426606528674 

	* And 140 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* four (U+0034): L<<822.0,203.0>--<982.0,204.0>>

	* four (U+0034): L<<83.0,196.0>--<704.0,201.0>> 

	* And seven (U+0037): L<<97.0,708.0>--<96.0,586.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] KalniaExtended-Thin.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 5	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* ampersand (U+0026): X=1071.0,Y=2.0 (should be at baseline 0?)

	* ampersand (U+0026): X=950.0,Y=1.5 (should be at baseline 0?)

	* parenleft (U+0028): X=264.5,Y=-0.5 (should be at baseline 0?)

	* parenright (U+0029): X=294.5,Y=-0.5 (should be at baseline 0?)

	* two (U+0032): X=329.5,Y=710.0 (should be at cap-height 708?)

	* three (U+0033): X=300.5,Y=2.0 (should be at baseline 0?)

	* three (U+0033): X=305.5,Y=706.0 (should be at cap-height 708?)

	* five (U+0035): X=326.5,Y=2.0 (should be at baseline 0?)

	* seven (U+0037): X=884.5,Y=706.0 (should be at cap-height 708?)

	* G (U+0047): X=777.5,Y=0.5 (should be at baseline 0?) 

	* And 89 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* four (U+0034): L<<720.0,204.0>--<720.0,546.0>> -> L<<720.0,546.0>--<725.0,724.0>>

	* onequarter (U+00BC): L<<566.0,93.0>--<566.0,230.0>> -> L<<566.0,230.0>--<567.0,302.0>>

	* threequarters (U+00BE): L<<697.0,93.0>--<697.0,230.0>> -> L<<697.0,230.0>--<698.0,302.0>> 

	* And uni2074 (U+2074): L<<293.0,509.0>--<293.0,646.0>> -> L<<293.0,646.0>--<294.0,718.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<178.0,50.0>-<178.0,68.0>-<190.0,91.0>>/L<<190.0,91.0>--<141.0,5.0>> = 2.12027053535989

	* A (U+0041): L<<141.0,5.0>--<247.0,5.0>>/B<<247.0,5.0>-<178.0,14.0>-<178.0,50.0>> = 7.431407971172489

	* Aacute (U+00C1): B<<178.0,50.0>-<178.0,68.0>-<190.0,91.0>>/L<<190.0,91.0>--<141.0,5.0>> = 2.12027053535989

	* Aacute (U+00C1): L<<141.0,5.0>--<247.0,5.0>>/B<<247.0,5.0>-<178.0,14.0>-<178.0,50.0>> = 7.431407971172489

	* Abreve (U+0102): B<<178.0,50.0>-<178.0,68.0>-<190.0,91.0>>/L<<190.0,91.0>--<141.0,5.0>> = 2.12027053535989

	* Abreve (U+0102): L<<141.0,5.0>--<247.0,5.0>>/B<<247.0,5.0>-<178.0,14.0>-<178.0,50.0>> = 7.431407971172489

	* Acircumflex (U+00C2): B<<178.0,50.0>-<178.0,68.0>-<190.0,91.0>>/L<<190.0,91.0>--<141.0,5.0>> = 2.12027053535989

	* Acircumflex (U+00C2): L<<141.0,5.0>--<247.0,5.0>>/B<<247.0,5.0>-<178.0,14.0>-<178.0,50.0>> = 7.431407971172489

	* Adieresis (U+00C4): B<<178.0,50.0>-<178.0,68.0>-<190.0,91.0>>/L<<190.0,91.0>--<141.0,5.0>> = 2.12027053535989

	* Adieresis (U+00C4): L<<141.0,5.0>--<247.0,5.0>>/B<<247.0,5.0>-<178.0,14.0>-<178.0,50.0>> = 7.431407971172489 

	* And 162 more.

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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fi (U+FB01): L<<398.0,500.0>--<599.0,492.0>> -> L<<599.0,492.0>--<1013.0,515.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Aacute (U+00C1): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Abreve (U+0102): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Acircumflex (U+00C2): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Adieresis (U+00C4): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Agrave (U+00C0): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Amacron (U+0100): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Aogonek (U+0104): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Aring (U+00C5): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657

	* Atilde (U+00C3): B<<222.0,129.0>-<222.0,164.0>-<240.0,207.0>>/L<<240.0,207.0>--<115.0,12.0>> = 9.94650036850657 

	* And 93 more.

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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 5	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* ampersand (U+0026): X=640.5,Y=1.5 (should be at baseline 0?)

	* comma (U+002C): X=68.0,Y=-2.0 (should be at baseline 0?)

	* two (U+0032): X=87.5,Y=-2.0 (should be at baseline 0?)

	* two (U+0032): X=202.0,Y=706.0 (should be at cap-height 708?)

	* three (U+0033): X=192.0,Y=2.0 (should be at baseline 0?)

	* three (U+0033): X=195.0,Y=706.0 (should be at cap-height 708?)

	* five (U+0035): X=207.0,Y=2.0 (should be at baseline 0?)

	* seven (U+0037): X=544.5,Y=706.0 (should be at cap-height 708?)

	* semicolon (U+003B): X=68.0,Y=-2.0 (should be at baseline 0?)

	* G (U+0047): X=511.0,Y=2.0 (should be at baseline 0?) 

	* And 45 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* four (U+0034): L<<410.0,204.0>--<410.0,546.0>> -> L<<410.0,546.0>--<415.0,724.0>>

	* onequarter (U+00BC): L<<392.0,93.0>--<392.0,230.0>> -> L<<392.0,230.0>--<395.0,302.0>>

	* threequarters (U+00BE): L<<502.0,93.0>--<502.0,230.0>> -> L<<502.0,230.0>--<505.0,302.0>> 

	* And uni2074 (U+2074): L<<171.0,509.0>--<171.0,646.0>> -> L<<171.0,646.0>--<174.0,718.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* Aacute (U+00C1): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* Abreve (U+0102): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* Acircumflex (U+00C2): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* Adieresis (U+00C4): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* Agrave (U+00C0): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* Amacron (U+0100): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* Aogonek (U+0104): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* Aring (U+00C5): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792

	* Atilde (U+00C3): B<<113.0,50.0>-<113.0,68.0>-<123.0,94.0>>/L<<123.0,94.0>--<89.0,5.0>> = 0.12953055440981792 

	* And 152 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* seven (U+0037): L<<85.0,708.0>--<84.0,592.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] Kalnia-Color-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>


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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 5	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* dollar (U+0024): X=168.5,Y=2.0 (should be at baseline 0?)

	* dollar (U+0024): X=469.5,Y=2.0 (should be at baseline 0?)

	* ampersand (U+0026): X=622.0,Y=1.0 (should be at baseline 0?)

	* three (U+0033): X=238.0,Y=706.0 (should be at cap-height 708?)

	* G (U+0047): X=516.5,Y=-1.5 (should be at baseline 0?)

	* a (U+0061): X=218.5,Y=502.0 (should be at x-height 500?)

	* a (U+0061): X=311.0,Y=501.0 (should be at x-height 500?)

	* a (U+0061): X=387.0,Y=498.0 (should be at x-height 500?)

	* a (U+0061): X=311.0,Y=501.0 (should be at x-height 500?)

	* b (U+0062): X=420.0,Y=502.0 (should be at x-height 500?) 

	* And 84 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* C (U+0043): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Cacute (U+0106): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Ccaron (U+010C): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Ccedilla (U+00C7): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Cdotaccent (U+010A): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Euro (U+20AC): L<<655.0,522.0>--<701.0,414.0>> -> L<<701.0,414.0>--<704.0,407.0>> 

	* And ampersand (U+0026): L<<440.0,164.0>--<439.0,165.0>> -> L<<439.0,165.0>--<232.0,380.0>> [code: found-colinear-vectors]
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

	* And 22 more.

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

	- H.color1

	- n.color0

	- period.color1

	- r.color0

	- period.color0

	- I.color0

	- a.color1

	- C.color1

	- I.color1

	- A.color1 

	- And 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 3	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2

	- Glyph name: E	Contours detected: 5	Expected: 1 

	- And 182 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Euro (U+20AC): L<<660.0,522.0>--<693.0,409.0>> -> L<<693.0,409.0>--<695.0,404.0>> [code: found-colinear-vectors]
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

	* And 27 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 7 | 111 | 1647 | 92 | 1238 | 0 |
| 0% | 0% | 4% | 53% | 3% | 40% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
