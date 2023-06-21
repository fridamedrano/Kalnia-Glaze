## Fontbakery report

Fontbakery version: 0.8.9

<details><summary><b>[7] Kalnia-ExtraLight.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

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

	* And 170 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* seven (U+0037): L<<81.0,708.0>--<80.0,588.0>> [code: found-semi-vertical]
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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

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

	* A (U+0041): B<<191.0,72.0>-<191.0,97.0>-<210.0,131.0>>/L<<210.0,131.0>--<135.0,7.0>> = 1.9696866000377569

	* A (U+0041): L<<135.0,7.0>--<269.0,7.0>>/B<<269.0,7.0>-<229.0,14.0>-<210.0,29.0>> = 9.926245506651705

	* Aacute (U+00C1): B<<191.0,72.0>-<191.0,97.0>-<210.0,131.0>>/L<<210.0,131.0>--<135.0,7.0>> = 1.9696866000377569

	* Aacute (U+00C1): L<<135.0,7.0>--<269.0,7.0>>/B<<269.0,7.0>-<229.0,14.0>-<210.0,29.0>> = 9.926245506651705

	* Abreve (U+0102): B<<191.0,72.0>-<191.0,97.0>-<210.0,131.0>>/L<<210.0,131.0>--<135.0,7.0>> = 1.9696866000377569

	* Abreve (U+0102): L<<135.0,7.0>--<269.0,7.0>>/B<<269.0,7.0>-<229.0,14.0>-<210.0,29.0>> = 9.926245506651705

	* Acircumflex (U+00C2): B<<191.0,72.0>-<191.0,97.0>-<210.0,131.0>>/L<<210.0,131.0>--<135.0,7.0>> = 1.9696866000377569

	* Acircumflex (U+00C2): L<<135.0,7.0>--<269.0,7.0>>/B<<269.0,7.0>-<229.0,14.0>-<210.0,29.0>> = 9.926245506651705

	* Adieresis (U+00C4): B<<191.0,72.0>-<191.0,97.0>-<210.0,131.0>>/L<<210.0,131.0>--<135.0,7.0>> = 1.9696866000377569

	* Adieresis (U+00C4): L<<135.0,7.0>--<269.0,7.0>>/B<<269.0,7.0>-<229.0,14.0>-<210.0,29.0>> = 9.926245506651705 

	* And 185 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<1354.0,97.0>--<1353.0,248.0>>

	* B (U+0042): L<<557.0,362.0>--<267.0,364.0>>

	* OE (U+0152): L<<1537.0,97.0>--<1536.0,248.0>>

	* four (U+0034): L<<784.0,203.0>--<951.0,204.0>>

	* four (U+0034): L<<83.0,198.0>--<711.0,202.0>> 

	* And seven (U+0037): L<<101.0,708.0>--<100.0,588.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[7] Kalnia-Bold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Acircumflex (U+00C2): L<<361.0,862.0>--<506.0,790.0>> -> L<<506.0,790.0>--<510.0,788.0>>

	* C (U+0043): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Cacute (U+0106): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Ccaron (U+010C): L<<443.0,807.0>--<298.0,879.0>> -> L<<298.0,879.0>--<294.0,881.0>>

	* Ccaron (U+010C): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Ccedilla (U+00C7): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Cdotaccent (U+010A): L<<578.0,522.0>--<624.0,414.0>> -> L<<624.0,414.0>--<627.0,407.0>>

	* Dcaron (U+010E): L<<436.0,807.0>--<291.0,879.0>> -> L<<291.0,879.0>--<287.0,881.0>>

	* Dcroat (U+0110): L<<436.0,807.0>--<291.0,879.0>> -> L<<291.0,879.0>--<287.0,881.0>>

	* Ecaron (U+011A): L<<400.0,807.0>--<255.0,879.0>> -> L<<255.0,879.0>--<251.0,881.0>> 

	* And 29 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Aacute (U+00C1): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Abreve (U+0102): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Acircumflex (U+00C2): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Adieresis (U+00C4): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Agrave (U+00C0): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Amacron (U+0100): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Aogonek (U+0104): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Aring (U+00C5): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483

	* Atilde (U+00C3): B<<192.0,222.0>-<192.0,266.0>-<201.0,320.0>>/L<<201.0,320.0>--<77.0,20.0>> = 12.994616791916483 

	* And 22 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[7] KalniaExtended-Bold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 5	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Aacute (U+00C1): L<<662.0,778.0>--<665.0,779.0>> -> L<<665.0,779.0>--<978.0,861.0>>

	* Acircumflex (U+00C2): L<<500.0,864.0>--<876.0,779.0>> -> L<<876.0,779.0>--<880.0,778.0>>

	* Agrave (U+00C0): L<<284.0,861.0>--<597.0,779.0>> -> L<<597.0,779.0>--<600.0,778.0>>

	* Cacute (U+0106): L<<717.0,778.0>--<720.0,779.0>> -> L<<720.0,779.0>--<1033.0,861.0>>

	* Ccaron (U+010C): L<<807.0,805.0>--<431.0,890.0>> -> L<<431.0,890.0>--<427.0,891.0>>

	* Dcaron (U+010E): L<<748.0,805.0>--<372.0,890.0>> -> L<<372.0,890.0>--<368.0,891.0>>

	* Dcroat (U+0110): L<<748.0,805.0>--<372.0,890.0>> -> L<<372.0,890.0>--<368.0,891.0>>

	* Eacute (U+00C9): L<<694.0,778.0>--<697.0,779.0>> -> L<<697.0,779.0>--<1010.0,861.0>>

	* Ecaron (U+011A): L<<784.0,805.0>--<408.0,890.0>> -> L<<408.0,890.0>--<404.0,891.0>>

	* Ecircumflex (U+00CA): L<<532.0,864.0>--<908.0,779.0>> -> L<<908.0,779.0>--<912.0,778.0>> 

	* And 66 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* C (U+0043): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Cacute (U+0106): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Ccaron (U+010C): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Ccedilla (U+00C7): B<<701.5,-168.0>-<661.0,-186.0>-<602.0,-193.0>>/L<<602.0,-193.0>--<716.0,-193.0>> = 6.766174822553066

	* Ccedilla (U+00C7): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Cdotaccent (U+010A): B<<910.0,24.5>-<1015.0,42.0>-<1107.0,83.0>>/B<<1107.0,83.0>-<1038.0,71.0>-<964.0,71.0>> = 14.154439854180508

	* Scedilla (U+015E): B<<698.5,-168.0>-<658.0,-186.0>-<599.0,-193.0>>/L<<599.0,-193.0>--<713.0,-193.0>> = 6.766174822553066

	* a (U+0061): B<<467.0,20.0>-<540.0,33.0>-<578.0,58.0>>/B<<578.0,58.0>-<568.0,53.0>-<558.0,53.0>> = 6.775656169398931

	* aacute (U+00E1): B<<467.0,20.0>-<540.0,33.0>-<578.0,58.0>>/B<<578.0,58.0>-<568.0,53.0>-<558.0,53.0>> = 6.775656169398931

	* abreve (U+0103): B<<467.0,20.0>-<540.0,33.0>-<578.0,58.0>>/B<<578.0,58.0>-<568.0,53.0>-<558.0,53.0>> = 6.775656169398931 

	* And 20 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[6] Kalnia-SemiBold.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 5	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Acircumflex (U+00C2): L<<544.0,911.0>--<547.0,909.0>> -> L<<547.0,909.0>--<697.0,796.0>>

	* Ccaron (U+010C): L<<585.0,794.0>--<582.0,796.0>> -> L<<582.0,796.0>--<432.0,909.0>>

	* Dcaron (U+010E): L<<561.0,794.0>--<558.0,796.0>> -> L<<558.0,796.0>--<408.0,909.0>>

	* Dcroat (U+0110): L<<561.0,794.0>--<558.0,796.0>> -> L<<558.0,796.0>--<408.0,909.0>>

	* Ecaron (U+011A): L<<545.0,794.0>--<542.0,796.0>> -> L<<542.0,796.0>--<392.0,909.0>>

	* Ecircumflex (U+00CA): L<<550.0,911.0>--<553.0,909.0>> -> L<<553.0,909.0>--<703.0,796.0>>

	* Icircumflex (U+00CE): L<<219.0,911.0>--<222.0,909.0>> -> L<<222.0,909.0>--<372.0,796.0>>

	* Ncaron (U+0147): L<<576.0,794.0>--<573.0,796.0>> -> L<<573.0,796.0>--<423.0,909.0>>

	* Ocircumflex (U+00D4): L<<578.0,911.0>--<581.0,909.0>> -> L<<581.0,909.0>--<731.0,796.0>>

	* Rcaron (U+0158): L<<494.0,794.0>--<491.0,796.0>> -> L<<491.0,796.0>--<341.0,909.0>> 

	* And 27 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<179.0,50.0>-<179.0,68.0>-<191.0,91.0>>/L<<191.0,91.0>--<142.0,5.0>> = 2.12027053535989

	* A (U+0041): L<<142.0,5.0>--<248.0,5.0>>/B<<248.0,5.0>-<179.0,14.0>-<179.0,50.0>> = 7.431407971172489

	* Aacute (U+00C1): B<<179.0,50.0>-<179.0,68.0>-<191.0,91.0>>/L<<191.0,91.0>--<142.0,5.0>> = 2.12027053535989

	* Aacute (U+00C1): L<<142.0,5.0>--<248.0,5.0>>/B<<248.0,5.0>-<179.0,14.0>-<179.0,50.0>> = 7.431407971172489

	* Abreve (U+0102): B<<179.0,50.0>-<179.0,68.0>-<191.0,91.0>>/L<<191.0,91.0>--<142.0,5.0>> = 2.12027053535989

	* Abreve (U+0102): L<<142.0,5.0>--<248.0,5.0>>/B<<248.0,5.0>-<179.0,14.0>-<179.0,50.0>> = 7.431407971172489

	* Acircumflex (U+00C2): B<<179.0,50.0>-<179.0,68.0>-<191.0,91.0>>/L<<191.0,91.0>--<142.0,5.0>> = 2.12027053535989

	* Acircumflex (U+00C2): L<<142.0,5.0>--<248.0,5.0>>/B<<248.0,5.0>-<179.0,14.0>-<179.0,50.0>> = 7.431407971172489

	* Adieresis (U+00C4): B<<179.0,50.0>-<179.0,68.0>-<191.0,91.0>>/L<<191.0,91.0>--<142.0,5.0>> = 2.12027053535989

	* Adieresis (U+00C4): L<<142.0,5.0>--<248.0,5.0>>/B<<248.0,5.0>-<179.0,14.0>-<179.0,50.0>> = 7.431407971172489 

	* And 182 more.

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
</div></details><br></div></details><details><summary><b>[6] Kalnia-Regular.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* A (U+0041): L<<199.0,288.0>--<199.0,289.0>>/L<<199.0,289.0>--<198.0,285.0>> = 14.036243467926484

	* Aacute (U+00C1): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Aacute (U+00C1): L<<199.0,288.0>--<199.0,289.0>>/L<<199.0,289.0>--<198.0,285.0>> = 14.036243467926484

	* Abreve (U+0102): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Abreve (U+0102): B<<379.0,862.0>-<388.0,862.0>-<400.0,916.0>>/L<<400.0,916.0>--<398.0,906.0>> = 1.2188752351313326

	* Abreve (U+0102): L<<199.0,288.0>--<199.0,289.0>>/L<<199.0,289.0>--<198.0,285.0>> = 14.036243467926484

	* Abreve (U+0102): L<<360.0,906.0>--<358.0,916.0>>/B<<358.0,916.0>-<370.0,862.0>-<379.0,862.0>> = 1.2188752351313326

	* Acircumflex (U+00C2): B<<147.0,125.0>-<147.0,155.0>-<159.0,197.0>>/L<<159.0,197.0>--<84.0,12.0>> = 6.122503661487386

	* Acircumflex (U+00C2): L<<199.0,288.0>--<199.0,289.0>>/L<<199.0,289.0>--<198.0,285.0>> = 14.036243467926484 

	* And 136 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[6] Kalnia-Medium.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 348 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
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

	* And 58 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[6] Kalnia-Light.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

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

	* And 150 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[9] Kalnia-Thin.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 5	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

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

	* And 61 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Acircumflex (U+00C2): L<<357.0,911.0>--<359.0,909.0>> -> L<<359.0,909.0>--<482.0,795.0>>

	* Ccaron (U+010C): L<<385.0,794.0>--<383.0,796.0>> -> L<<383.0,796.0>--<260.0,910.0>>

	* Dcaron (U+010E): L<<344.0,794.0>--<342.0,796.0>> -> L<<342.0,796.0>--<219.0,910.0>>

	* Dcroat (U+0110): L<<344.0,794.0>--<342.0,796.0>> -> L<<342.0,796.0>--<219.0,910.0>>

	* Ecaron (U+011A): L<<352.0,794.0>--<350.0,796.0>> -> L<<350.0,796.0>--<227.0,910.0>>

	* Ecircumflex (U+00CA): L<<356.0,911.0>--<358.0,909.0>> -> L<<358.0,909.0>--<481.0,795.0>>

	* Icircumflex (U+00CE): L<<160.0,911.0>--<162.0,909.0>> -> L<<162.0,909.0>--<285.0,795.0>>

	* Ncaron (U+0147): L<<414.0,794.0>--<412.0,796.0>> -> L<<412.0,796.0>--<289.0,910.0>>

	* Ocircumflex (U+00D4): L<<373.0,911.0>--<375.0,909.0>> -> L<<375.0,909.0>--<498.0,795.0>>

	* Rcaron (U+0158): L<<331.0,794.0>--<329.0,796.0>> -> L<<329.0,796.0>--<206.0,910.0>> 

	* And 27 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
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

	* And 172 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* seven (U+0037): L<<85.0,708.0>--<84.0,592.0>> [code: found-semi-vertical]
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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fi (U+FB01): L<<442.0,500.0>--<623.0,492.0>> -> L<<623.0,492.0>--<1086.0,515.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<237.0,154.0>-<237.0,192.0>-<254.0,240.0>>/L<<254.0,240.0>--<107.0,14.0>> = 13.539237670706779

	* Aacute (U+00C1): B<<237.0,154.0>-<237.0,192.0>-<254.0,240.0>>/L<<254.0,240.0>--<107.0,14.0>> = 13.539237670706779

	* Abreve (U+0102): B<<237.0,154.0>-<237.0,192.0>-<254.0,240.0>>/L<<254.0,240.0>--<107.0,14.0>> = 13.539237670706779

	* Acircumflex (U+00C2): B<<237.0,154.0>-<237.0,192.0>-<254.0,240.0>>/L<<254.0,240.0>--<107.0,14.0>> = 13.539237670706779

	* Adieresis (U+00C4): B<<237.0,154.0>-<237.0,192.0>-<254.0,240.0>>/L<<254.0,240.0>--<107.0,14.0>> = 13.539237670706779

	* Agrave (U+00C0): B<<237.0,154.0>-<237.0,192.0>-<254.0,240.0>>/L<<254.0,240.0>--<107.0,14.0>> = 13.539237670706779

	* Amacron (U+0100): B<<237.0,154.0>-<237.0,192.0>-<254.0,240.0>>/L<<254.0,240.0>--<107.0,14.0>> = 13.539237670706779

	* Aogonek (U+0104): B<<237.0,154.0>-<237.0,192.0>-<254.0,240.0>>/L<<254.0,240.0>--<107.0,14.0>> = 13.539237670706779

	* Aring (U+00C5): B<<237.0,154.0>-<237.0,192.0>-<254.0,240.0>>/L<<254.0,240.0>--<107.0,14.0>> = 13.539237670706779

	* Atilde (U+00C3): B<<237.0,154.0>-<237.0,192.0>-<254.0,240.0>>/L<<254.0,240.0>--<107.0,14.0>> = 13.539237670706779 

	* And 79 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* four (U+0034): L<<973.0,201.0>--<1107.0,202.0>> [code: found-semi-vertical]
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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<200.0,88.0>-<200.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 5.599019901513194

	* A (U+0041): L<<129.0,8.0>--<285.0,8.0>>/B<<285.0,8.0>-<241.0,18.0>-<220.5,36.5>> = 12.80426606528674

	* Aacute (U+00C1): B<<200.0,88.0>-<200.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 5.599019901513194

	* Aacute (U+00C1): L<<129.0,8.0>--<285.0,8.0>>/B<<285.0,8.0>-<241.0,18.0>-<220.5,36.5>> = 12.80426606528674

	* Abreve (U+0102): B<<200.0,88.0>-<200.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 5.599019901513194

	* Abreve (U+0102): L<<129.0,8.0>--<285.0,8.0>>/B<<285.0,8.0>-<241.0,18.0>-<220.5,36.5>> = 12.80426606528674

	* Acircumflex (U+00C2): B<<200.0,88.0>-<200.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 5.599019901513194

	* Acircumflex (U+00C2): L<<129.0,8.0>--<285.0,8.0>>/B<<285.0,8.0>-<241.0,18.0>-<220.5,36.5>> = 12.80426606528674

	* Adieresis (U+00C4): B<<200.0,88.0>-<200.0,116.0>-<218.0,153.0>>/L<<218.0,153.0>--<129.0,8.0>> = 5.599019901513194

	* Adieresis (U+00C4): L<<129.0,8.0>--<285.0,8.0>>/B<<285.0,8.0>-<241.0,18.0>-<220.5,36.5>> = 12.80426606528674 

	* And 160 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* four (U+0034): L<<822.0,203.0>--<982.0,204.0>>

	* four (U+0034): L<<83.0,196.0>--<704.0,201.0>> 

	* And seven (U+0037): L<<97.0,708.0>--<96.0,586.0>> [code: found-semi-vertical]
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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fi (U+FB01): L<<398.0,500.0>--<599.0,492.0>> -> L<<599.0,492.0>--<1013.0,515.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* A (U+0041): B<<223.0,129.0>-<223.0,164.0>-<241.0,207.0>>/L<<241.0,207.0>--<116.0,12.0>> = 9.94650036850657

	* Aacute (U+00C1): B<<223.0,129.0>-<223.0,164.0>-<241.0,207.0>>/L<<241.0,207.0>--<116.0,12.0>> = 9.94650036850657

	* Abreve (U+0102): B<<223.0,129.0>-<223.0,164.0>-<241.0,207.0>>/L<<241.0,207.0>--<116.0,12.0>> = 9.94650036850657

	* Acircumflex (U+00C2): B<<223.0,129.0>-<223.0,164.0>-<241.0,207.0>>/L<<241.0,207.0>--<116.0,12.0>> = 9.94650036850657

	* Adieresis (U+00C4): B<<223.0,129.0>-<223.0,164.0>-<241.0,207.0>>/L<<241.0,207.0>--<116.0,12.0>> = 9.94650036850657

	* Agrave (U+00C0): B<<223.0,129.0>-<223.0,164.0>-<241.0,207.0>>/L<<241.0,207.0>--<116.0,12.0>> = 9.94650036850657

	* Amacron (U+0100): B<<223.0,129.0>-<223.0,164.0>-<241.0,207.0>>/L<<241.0,207.0>--<116.0,12.0>> = 9.94650036850657

	* Aogonek (U+0104): B<<223.0,129.0>-<223.0,164.0>-<241.0,207.0>>/L<<241.0,207.0>--<116.0,12.0>> = 9.94650036850657

	* Aring (U+00C5): B<<223.0,129.0>-<223.0,164.0>-<241.0,207.0>>/L<<241.0,207.0>--<116.0,12.0>> = 9.94650036850657

	* Atilde (U+00C3): B<<223.0,129.0>-<223.0,164.0>-<241.0,207.0>>/L<<241.0,207.0>--<116.0,12.0>> = 9.94650036850657 

	* And 104 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
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

	- A.color1

	- F.color2

	- acutecomb.color1

	- uni030C.alt.color0

	- G.color2

	- e.color0

	- acutecomb.color0

	- uni030C.color1

	- I.color0

	- l.color0 

	- And 67 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: NULL	Contours detected: 3	Expected: 0

	- Glyph name: exclam	Contours detected: 3	Expected: 2

	- Glyph name: comma	Contours detected: 2	Expected: 1

	- Glyph name: period	Contours detected: 2	Expected: 1

	- Glyph name: colon	Contours detected: 4	Expected: 2

	- Glyph name: semicolon	Contours detected: 4	Expected: 2

	- Glyph name: question	Contours detected: 3	Expected: 2

	- Glyph name: A	Contours detected: 4	Expected: 2

	- Glyph name: C	Contours detected: 3	Expected: 1

	- Glyph name: D	Contours detected: 4	Expected: 2 

	- And 346 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* Aacute (U+00C1): L<<640.0,778.0>--<643.0,779.0>> -> L<<643.0,779.0>--<925.0,871.0>>

	* Agrave (U+00C0): L<<304.0,871.0>--<586.0,779.0>> -> L<<586.0,779.0>--<589.0,778.0>>

	* Cacute (U+0106): L<<693.0,778.0>--<696.0,779.0>> -> L<<696.0,779.0>--<978.0,871.0>>

	* Eacute (U+00C9): L<<667.0,778.0>--<670.0,779.0>> -> L<<670.0,779.0>--<952.0,871.0>>

	* Egrave (U+00C8): L<<331.0,871.0>--<613.0,779.0>> -> L<<613.0,779.0>--<616.0,778.0>>

	* Iacute (U+00CD): L<<338.0,778.0>--<341.0,779.0>> -> L<<341.0,779.0>--<623.0,871.0>>

	* Igrave (U+00CC): L<<2.0,871.0>--<284.0,779.0>> -> L<<284.0,779.0>--<287.0,778.0>>

	* Lacute (U+0139): L<<341.0,778.0>--<344.0,779.0>> -> L<<344.0,779.0>--<626.0,871.0>>

	* Nacute (U+0143): L<<672.0,778.0>--<675.0,779.0>> -> L<<675.0,779.0>--<957.0,871.0>>

	* Oacute (U+00D3): L<<695.0,778.0>--<698.0,779.0>> -> L<<698.0,779.0>--<980.0,871.0>> 

	* And 33 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* C (U+0043): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* Cacute (U+0106): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* Ccaron (U+010C): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* Ccedilla (U+00C7): B<<698.5,-172.0>-<658.0,-191.0>-<598.0,-196.0>>/B<<598.0,-196.0>-<619.0,-196.0>-<643.0,-196.0>> = 4.763641690726143

	* Ccedilla (U+00C7): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* Cdotaccent (U+010A): B<<875.5,21.0>-<975.0,38.0>-<1060.0,77.0>>/B<<1060.0,77.0>-<978.0,56.0>-<885.0,56.0>> = 10.282188402233944

	* E (U+0045): B<<1039.0,117.0>-<980.0,40.0>-<882.0,17.0>>/L<<882.0,17.0>--<1192.0,17.0>> = 13.207928462779101

	* E (U+0045): L<<1192.0,691.0>--<866.0,691.0>>/B<<866.0,691.0>-<955.0,671.0>-<1014.0,602.0>> = 12.665063765042364

	* Eacute (U+00C9): B<<1039.0,117.0>-<980.0,40.0>-<882.0,17.0>>/L<<882.0,17.0>--<1192.0,17.0>> = 13.207928462779101

	* Eacute (U+00C9): L<<1192.0,691.0>--<866.0,691.0>>/B<<866.0,691.0>-<955.0,671.0>-<1014.0,602.0>> = 12.665063765042364 

	* And 44 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* B (U+0042): L<<632.0,366.0>--<515.0,367.0>> [code: found-semi-vertical]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 0 | 104 | 1570 | 85 | 1336 | 0 |
| 0% | 0% | 3% | 51% | 3% | 43% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
