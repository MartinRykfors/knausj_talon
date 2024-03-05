from talon import Context, Module

mod = Module()
ctx = Context()

mod.list("css_property", desc="CSS properties")

ctx.lists["self.css_property"] = {
    "webkit line clamp": "-webkit-line-clamp",
    "accent color": "accent-color",
    "align content": "align-content",
    "align items": "align-items",
    "align self": "align-self",
    "alignment baseline": "alignment-baseline",
    "all": "all",
    "anchor default": "anchor-default",
    "anchor name": "anchor-name",
    "anchor scroll": "anchor-scroll",
    "animation": "animation",
    "animation composition": "animation-composition",
    "animation delay": "animation-delay",
    "animation direction": "animation-direction",
    "animation duration": "animation-duration",
    "animation fill mode": "animation-fill-mode",
    "animation iteration count": "animation-iteration-count",
    "animation name": "animation-name",
    "animation play state": "animation-play-state",
    "animation range": "animation-range",
    "animation range end": "animation-range-end",
    "animation range start": "animation-range-start",
    "animation timeline": "animation-timeline",
    "animation timing function": "animation-timing-function",
    "appearance": "appearance",
    "aspect ratio": "aspect-ratio",
    "azimuth": "azimuth",
    "backface visibility": "backface-visibility",
    "background": "background",
    "background attachment": "background-attachment",
    "background blend mode": "background-blend-mode",
    "background clip": "background-clip",
    "background color": "background-color",
    "background image": "background-image",
    "background origin": "background-origin",
    "background position": "background-position",
    "background repeat": "background-repeat",
    "background size": "background-size",
    "baseline shift": "baseline-shift",
    "baseline source": "baseline-source",
    "block ellipsis": "block-ellipsis",
    "block size": "block-size",
    "block step": "block-step",
    "block step align": "block-step-align",
    "block step insert": "block-step-insert",
    "block step round": "block-step-round",
    "block step size": "block-step-size",
    "bookmark label": "bookmark-label",
    "bookmark level": "bookmark-level",
    "bookmark state": "bookmark-state",
    "border": "border",
    "border block": "border-block",
    "border block color": "border-block-color",
    "border block end": "border-block-end",
    "border block end color": "border-block-end-color",
    "border block end style": "border-block-end-style",
    "border block end width": "border-block-end-width",
    "border block start": "border-block-start",
    "border block start color": "border-block-start-color",
    "border block start style": "border-block-start-style",
    "border block start width": "border-block-start-width",
    "border block style": "border-block-style",
    "border block width": "border-block-width",
    "border bottom": "border-bottom",
    "border bottom color": "border-bottom-color",
    "border bottom left radius": "border-bottom-left-radius",
    "border bottom right radius": "border-bottom-right-radius",
    "border bottom style": "border-bottom-style",
    "border bottom width": "border-bottom-width",
    "border boundary": "border-boundary",
    "border collapse": "border-collapse",
    "border color": "border-color",
    "border end end radius": "border-end-end-radius",
    "border end start radius": "border-end-start-radius",
    "border image": "border-image",
    "border image outset": "border-image-outset",
    "border image repeat": "border-image-repeat",
    "border image slice": "border-image-slice",
    "border image source": "border-image-source",
    "border image width": "border-image-width",
    "border inline": "border-inline",
    "border inline color": "border-inline-color",
    "border inline end": "border-inline-end",
    "border inline end color": "border-inline-end-color",
    "border inline end style": "border-inline-end-style",
    "border inline end width": "border-inline-end-width",
    "border inline start": "border-inline-start",
    "border inline start color": "border-inline-start-color",
    "border inline start style": "border-inline-start-style",
    "border inline start width": "border-inline-start-width",
    "border inline style": "border-inline-style",
    "border inline width": "border-inline-width",
    "border left": "border-left",
    "border left color": "border-left-color",
    "border left style": "border-left-style",
    "border left width": "border-left-width",
    "border radius": "border-radius",
    "border right": "border-right",
    "border right color": "border-right-color",
    "border right style": "border-right-style",
    "border right width": "border-right-width",
    "border spacing": "border-spacing",
    "border start end radius": "border-start-end-radius",
    "border start start radius": "border-start-start-radius",
    "border style": "border-style",
    "border top": "border-top",
    "border top color": "border-top-color",
    "border top left radius": "border-top-left-radius",
    "border top right radius": "border-top-right-radius",
    "border top style": "border-top-style",
    "border top width": "border-top-width",
    "border width": "border-width",
    "bottom": "bottom",
    "box decoration break": "box-decoration-break",
    "box shadow": "box-shadow",
    "box sizing": "box-sizing",
    "box snap": "box-snap",
    "break after": "break-after",
    "break before": "break-before",
    "break inside": "break-inside",
    "caption side": "caption-side",
    "caret": "caret",
    "caret color": "caret-color",
    "caret shape": "caret-shape",
    "chains": "chains",
    "clear": "clear",
    "clip": "clip",
    "clip path": "clip-path",
    "clip rule": "clip-rule",
    "color": "color",
    "color adjust": "color-adjust",
    "color interpolation filters": "color-interpolation-filters",
    "color scheme": "color-scheme",
    "column count": "column-count",
    "column fill": "column-fill",
    "column gap": "column-gap",
    "column rule": "column-rule",
    "column rule color": "column-rule-color",
    "column rule style": "column-rule-style",
    "column rule width": "column-rule-width",
    "column span": "column-span",
    "column width": "column-width",
    "columns": "columns",
    "contain": "contain",
    "contain intrinsic block size": "contain-intrinsic-block-size",
    "contain intrinsic height": "contain-intrinsic-height",
    "contain intrinsic inline size": "contain-intrinsic-inline-size",
    "contain intrinsic size": "contain-intrinsic-size",
    "contain intrinsic width": "contain-intrinsic-width",
    "container": "container",
    "container name": "container-name",
    "container type": "container-type",
    "content": "content",
    "content visibility": "content-visibility",
    "continue": "continue",
    "counter increment": "counter-increment",
    "counter reset": "counter-reset",
    "counter set": "counter-set",
    "cue": "cue",
    "cue after": "cue-after",
    "cue before": "cue-before",
    "cursor": "cursor",
    "direction": "direction",
    "display": "display",
    "dominant baseline": "dominant-baseline",
    "elevation": "elevation",
    "empty cells": "empty-cells",
    "fill": "fill",
    "fill break": "fill-break",
    "fill color": "fill-color",
    "fill image": "fill-image",
    "fill opacity": "fill-opacity",
    "fill origin": "fill-origin",
    "fill position": "fill-position",
    "fill repeat": "fill-repeat",
    "fill rule": "fill-rule",
    "fill size": "fill-size",
    "filter": "filter",
    "flex": "flex",
    "flex basis": "flex-basis",
    "flex direction": "flex-direction",
    "flex flow": "flex-flow",
    "flex grow": "flex-grow",
    "flex shrink": "flex-shrink",
    "flex wrap": "flex-wrap",
    "float": "float",
    "float defer": "float-defer",
    "float offset": "float-offset",
    "float reference": "float-reference",
    "flood color": "flood-color",
    "flood opacity": "flood-opacity",
    "flow": "flow",
    "flow from": "flow-from",
    "flow into": "flow-into",
    "font": "font",
    "font family": "font-family",
    "font feature settings": "font-feature-settings",
    "font kerning": "font-kerning",
    "font language override": "font-language-override",
    "font optical sizing": "font-optical-sizing",
    "font palette": "font-palette",
    "font size": "font-size",
    "font size adjust": "font-size-adjust",
    "font stretch": "font-stretch",
    "font style": "font-style",
    "font synthesis": "font-synthesis",
    "font synthesis position": "font-synthesis-position",
    "font synthesis small caps": "font-synthesis-small-caps",
    "font synthesis style": "font-synthesis-style",
    "font synthesis weight": "font-synthesis-weight",
    "font variant": "font-variant",
    "font variant alternates": "font-variant-alternates",
    "font variant caps": "font-variant-caps",
    "font variant east asian": "font-variant-east-asian",
    "font variant emoji": "font-variant-emoji",
    "font variant ligatures": "font-variant-ligatures",
    "font variant numeric": "font-variant-numeric",
    "font variant position": "font-variant-position",
    "font variation settings": "font-variation-settings",
    "font weight": "font-weight",
    "footnote display": "footnote-display",
    "footnote policy": "footnote-policy",
    "forced color adjust": "forced-color-adjust",
    "gap": "gap",
    "glyph orientation vertical": "glyph-orientation-vertical",
    "grid": "grid",
    "grid area": "grid-area",
    "grid auto columns": "grid-auto-columns",
    "grid auto flow": "grid-auto-flow",
    "grid auto rows": "grid-auto-rows",
    "grid column": "grid-column",
    "grid column end": "grid-column-end",
    "grid column start": "grid-column-start",
    "grid row": "grid-row",
    "grid row end": "grid-row-end",
    "grid row start": "grid-row-start",
    "grid template": "grid-template",
    "grid template areas": "grid-template-areas",
    "grid template columns": "grid-template-columns",
    "grid template rows": "grid-template-rows",
    "hanging punctuation": "hanging-punctuation",
    "height": "height",
    "hyphenate character": "hyphenate-character",
    "hyphenate limit chars": "hyphenate-limit-chars",
    "hyphenate limit last": "hyphenate-limit-last",
    "hyphenate limit lines": "hyphenate-limit-lines",
    "hyphenate limit zone": "hyphenate-limit-zone",
    "hyphens": "hyphens",
    "image orientation": "image-orientation",
    "image rendering": "image-rendering",
    "image resolution": "image-resolution",
    "initial letter": "initial-letter",
    "initial letter align": "initial-letter-align",
    "initial letter wrap": "initial-letter-wrap",
    "inline size": "inline-size",
    "inline sizing": "inline-sizing",
    "input security": "input-security",
    "inset": "inset",
    "inset block": "inset-block",
    "inset block end": "inset-block-end",
    "inset block start": "inset-block-start",
    "inset inline": "inset-inline",
    "inset inline end": "inset-inline-end",
    "inset inline start": "inset-inline-start",
    "isolation": "isolation",
    "justify content": "justify-content",
    "justify items": "justify-items",
    "justify self": "justify-self",
    "left": "left",
    "letter spacing": "letter-spacing",
    "lighting color": "lighting-color",
    "line break": "line-break",
    "line clamp": "line-clamp",
    "line grid": "line-grid",
    "line height": "line-height",
    "line height step": "line-height-step",
    "line padding": "line-padding",
    "line snap": "line-snap",
    "list style": "list-style",
    "list style image": "list-style-image",
    "list style position": "list-style-position",
    "list style type": "list-style-type",
    "margin": "margin",
    "margin block": "margin-block",
    "margin block end": "margin-block-end",
    "margin block start": "margin-block-start",
    "margin bottom": "margin-bottom",
    "margin break": "margin-break",
    "margin inline": "margin-inline",
    "margin inline end": "margin-inline-end",
    "margin inline start": "margin-inline-start",
    "margin left": "margin-left",
    "margin right": "margin-right",
    "margin top": "margin-top",
    "margin trim": "margin-trim",
    "marker": "marker",
    "marker end": "marker-end",
    "marker knockout left": "marker-knockout-left",
    "marker knockout right": "marker-knockout-right",
    "marker mid": "marker-mid",
    "marker pattern": "marker-pattern",
    "marker segment": "marker-segment",
    "marker side": "marker-side",
    "marker start": "marker-start",
    "mask": "mask",
    "mask border": "mask-border",
    "mask border mode": "mask-border-mode",
    "mask border outset": "mask-border-outset",
    "mask border repeat": "mask-border-repeat",
    "mask border slice": "mask-border-slice",
    "mask border source": "mask-border-source",
    "mask border width": "mask-border-width",
    "mask clip": "mask-clip",
    "mask composite": "mask-composite",
    "mask image": "mask-image",
    "mask mode": "mask-mode",
    "mask origin": "mask-origin",
    "mask position": "mask-position",
    "mask repeat": "mask-repeat",
    "mask size": "mask-size",
    "mask type": "mask-type",
    "max block size": "max-block-size",
    "max height": "max-height",
    "max inline size": "max-inline-size",
    "max lines": "max-lines",
    "max width": "max-width",
    "min block size": "min-block-size",
    "min height": "min-height",
    "min inline size": "min-inline-size",
    "min intrinsic sizing": "min-intrinsic-sizing",
    "min width": "min-width",
    "mix blend mode": "mix-blend-mode",
    "nav down": "nav-down",
    "nav left": "nav-left",
    "nav right": "nav-right",
    "nav up": "nav-up",
    "object fit": "object-fit",
    "object position": "object-position",
    "offset": "offset",
    "offset anchor": "offset-anchor",
    "offset distance": "offset-distance",
    "offset path": "offset-path",
    "offset position": "offset-position",
    "offset rotate": "offset-rotate",
    "opacity": "opacity",
    "order": "order",
    "orphans": "orphans",
    "outline": "outline",
    "outline color": "outline-color",
    "outline offset": "outline-offset",
    "outline style": "outline-style",
    "outline width": "outline-width",
    "overflow": "overflow",
    "overflow anchor": "overflow-anchor",
    "overflow block": "overflow-block",
    "overflow clip margin": "overflow-clip-margin",
    "overflow clip margin block": "overflow-clip-margin-block",
    "overflow clip margin block end": "overflow-clip-margin-block-end",
    "overflow clip margin block start": "overflow-clip-margin-block-start",
    "overflow clip margin bottom": "overflow-clip-margin-bottom",
    "overflow clip margin inline": "overflow-clip-margin-inline",
    "overflow clip margin inline end": "overflow-clip-margin-inline-end",
    "overflow clip margin inline start": "overflow-clip-margin-inline-start",
    "overflow clip margin left": "overflow-clip-margin-left",
    "overflow clip margin right": "overflow-clip-margin-right",
    "overflow clip margin top": "overflow-clip-margin-top",
    "overflow inline": "overflow-inline",
    "overflow wrap": "overflow-wrap",
    "overflow x": "overflow-x",
    "overflow y": "overflow-y",
    "overscroll behavior": "overscroll-behavior",
    "overscroll behavior block": "overscroll-behavior-block",
    "overscroll behavior inline": "overscroll-behavior-inline",
    "overscroll behavior x": "overscroll-behavior-x",
    "overscroll behavior y": "overscroll-behavior-y",
    "padding": "padding",
    "padding block": "padding-block",
    "padding block end": "padding-block-end",
    "padding block start": "padding-block-start",
    "padding bottom": "padding-bottom",
    "padding inline": "padding-inline",
    "padding inline end": "padding-inline-end",
    "padding inline start": "padding-inline-start",
    "padding left": "padding-left",
    "padding right": "padding-right",
    "padding top": "padding-top",
    "page": "page",
    "page break after": "page-break-after",
    "page break before": "page-break-before",
    "page break inside": "page-break-inside",
    "pause": "pause",
    "pause after": "pause-after",
    "pause before": "pause-before",
    "perspective": "perspective",
    "perspective origin": "perspective-origin",
    "pitch": "pitch",
    "pitch range": "pitch-range",
    "place content": "place-content",
    "place items": "place-items",
    "place self": "place-self",
    "play during": "play-during",
    "pointer events": "pointer-events",
    "position": "position",
    "position fallback": "position-fallback",
    "position fallback bounds": "position-fallback-bounds",
    "print color adjust": "print-color-adjust",
    "property name": "property-name",
    "quotes": "quotes",
    "region fragment": "region-fragment",
    "resize": "resize",
    "rest": "rest",
    "rest after": "rest-after",
    "rest before": "rest-before",
    "richness": "richness",
    "right": "right",
    "rotate": "rotate",
    "row gap": "row-gap",
    "ruby align": "ruby-align",
    "ruby merge": "ruby-merge",
    "ruby overhang": "ruby-overhang",
    "ruby position": "ruby-position",
    "running": "running",
    "scale": "scale",
    "scroll behavior": "scroll-behavior",
    "scroll margin": "scroll-margin",
    "scroll margin block": "scroll-margin-block",
    "scroll margin block end": "scroll-margin-block-end",
    "scroll margin block start": "scroll-margin-block-start",
    "scroll margin bottom": "scroll-margin-bottom",
    "scroll margin inline": "scroll-margin-inline",
    "scroll margin inline end": "scroll-margin-inline-end",
    "scroll margin inline start": "scroll-margin-inline-start",
    "scroll margin left": "scroll-margin-left",
    "scroll margin right": "scroll-margin-right",
    "scroll margin top": "scroll-margin-top",
    "scroll padding": "scroll-padding",
    "scroll padding block": "scroll-padding-block",
    "scroll padding block end": "scroll-padding-block-end",
    "scroll padding block start": "scroll-padding-block-start",
    "scroll padding bottom": "scroll-padding-bottom",
    "scroll padding inline": "scroll-padding-inline",
    "scroll padding inline end": "scroll-padding-inline-end",
    "scroll padding inline start": "scroll-padding-inline-start",
    "scroll padding left": "scroll-padding-left",
    "scroll padding right": "scroll-padding-right",
    "scroll padding top": "scroll-padding-top",
    "scroll snap align": "scroll-snap-align",
    "scroll snap stop": "scroll-snap-stop",
    "scroll snap type": "scroll-snap-type",
    "scroll timeline": "scroll-timeline",
    "scroll timeline axis": "scroll-timeline-axis",
    "scroll timeline name": "scroll-timeline-name",
    "scrollbar color": "scrollbar-color",
    "scrollbar gutter": "scrollbar-gutter",
    "scrollbar width": "scrollbar-width",
    "shape image threshold": "shape-image-threshold",
    "shape inside": "shape-inside",
    "shape margin": "shape-margin",
    "shape outside": "shape-outside",
    "spatial navigation action": "spatial-navigation-action",
    "spatial navigation contain": "spatial-navigation-contain",
    "spatial navigation function": "spatial-navigation-function",
    "speak": "speak",
    "speak as": "speak-as",
    "speak header": "speak-header",
    "speak numeral": "speak-numeral",
    "speak punctuation": "speak-punctuation",
    "speech rate": "speech-rate",
    "stress": "stress",
    "string set": "string-set",
    "stroke": "stroke",
    "stroke align": "stroke-align",
    "stroke alignment": "stroke-alignment",
    "stroke break": "stroke-break",
    "stroke color": "stroke-color",
    "stroke dash corner": "stroke-dash-corner",
    "stroke dash justify": "stroke-dash-justify",
    "stroke dashadjust": "stroke-dashadjust",
    "stroke dasharray": "stroke-dasharray",
    "stroke dashcorner": "stroke-dashcorner",
    "stroke dashoffset": "stroke-dashoffset",
    "stroke image": "stroke-image",
    "stroke linecap": "stroke-linecap",
    "stroke linejoin": "stroke-linejoin",
    "stroke miterlimit": "stroke-miterlimit",
    "stroke opacity": "stroke-opacity",
    "stroke origin": "stroke-origin",
    "stroke position": "stroke-position",
    "stroke repeat": "stroke-repeat",
    "stroke size": "stroke-size",
    "stroke width": "stroke-width",
    "tab size": "tab-size",
    "table layout": "table-layout",
    "text align": "text-align",
    "text align all": "text-align-all",
    "text align last": "text-align-last",
    "text autospace": "text-autospace",
    "text box edge": "text-box-edge",
    "text box trim": "text-box-trim",
    "text combine upright": "text-combine-upright",
    "text decoration": "text-decoration",
    "text decoration color": "text-decoration-color",
    "text decoration line": "text-decoration-line",
    "text decoration skip": "text-decoration-skip",
    "text decoration skip box": "text-decoration-skip-box",
    "text decoration skip ink": "text-decoration-skip-ink",
    "text decoration skip inset": "text-decoration-skip-inset",
    "text decoration skip self": "text-decoration-skip-self",
    "text decoration skip spaces": "text-decoration-skip-spaces",
    "text decoration style": "text-decoration-style",
    "text decoration thickness": "text-decoration-thickness",
    "text decoration trim": "text-decoration-trim",
    "text emphasis": "text-emphasis",
    "text emphasis color": "text-emphasis-color",
    "text emphasis position": "text-emphasis-position",
    "text emphasis skip": "text-emphasis-skip",
    "text emphasis style": "text-emphasis-style",
    "text group align": "text-group-align",
    "text indent": "text-indent",
    "text justify": "text-justify",
    "text orientation": "text-orientation",
    "text overflow": "text-overflow",
    "text shadow": "text-shadow",
    "text spacing": "text-spacing",
    "text spacing trim": "text-spacing-trim",
    "text transform": "text-transform",
    "text underline offset": "text-underline-offset",
    "text underline position": "text-underline-position",
    "text wrap": "text-wrap",
    "text wrap mode": "text-wrap-mode",
    "text wrap style": "text-wrap-style",
    "timeline scope": "timeline-scope",
    "top": "top",
    "transform": "transform",
    "transform box": "transform-box",
    "transform origin": "transform-origin",
    "transform style": "transform-style",
    "transition": "transition",
    "transition behavior": "transition-behavior",
    "transition delay": "transition-delay",
    "transition duration": "transition-duration",
    "transition property": "transition-property",
    "transition timing function": "transition-timing-function",
    "translate": "translate",
    "unicode bidi": "unicode-bidi",
    "user select": "user-select",
    "vertical align": "vertical-align",
    "view timeline": "view-timeline",
    "view timeline axis": "view-timeline-axis",
    "view timeline inset": "view-timeline-inset",
    "view timeline name": "view-timeline-name",
    "view transition name": "view-transition-name",
    "visibility": "visibility",
    "voice balance": "voice-balance",
    "voice duration": "voice-duration",
    "voice family": "voice-family",
    "voice pitch": "voice-pitch",
    "voice range": "voice-range",
    "voice rate": "voice-rate",
    "voice stress": "voice-stress",
    "voice volume": "voice-volume",
    "volume": "volume",
    "white space": "white-space",
    "white space collapse": "white-space-collapse",
    "white space trim": "white-space-trim",
    "widows": "widows",
    "width": "width",
    "will change": "will-change",
    "word boundary detection": "word-boundary-detection",
    "word boundary expansion": "word-boundary-expansion",
    "word break": "word-break",
    "word space transform": "word-space-transform",
    "word spacing": "word-spacing",
    "word wrap": "word-wrap",
    "wrap after": "wrap-after",
    "wrap before": "wrap-before",
    "wrap flow": "wrap-flow",
    "wrap inside": "wrap-inside",
    "wrap through": "wrap-through",
    "writing mode": "writing-mode",
    "z index": "z-index",
}

mod.list("css_value", desc="CSS values")
ctx.lists["self.css_value"] = {
    "absolute": "absolute",
    "alias": "alias",
    "all": "all",
    "all petite caps": "all-petite-caps",
    "all scroll": "all-scroll",
    "all small caps": "all-small-caps",
    "allow end": "allow-end",
    "alpha": "alpha",
    "alternate": "alternate",
    "alternate reverse": "alternate-reverse",
    "always": "always",
    "armenian": "armenian",
    "auto": "auto",
    "avoid": "avoid",
    "avoid column": "avoid-column",
    "avoid page": "avoid-page",
    "backwards": "backwards",
    "baseline": "baseline",
    "below left": "below left",
    "below right": "below right",
    "bidi override": "bidi-override",
    "blink": "blink",
    "block": "block",
    "bold": "bold",
    "bolder": "bolder",
    "border box": "border-box",
    "both": "both",
    "bottom": "bottom",
    "box decoration": "box-decoration",
    "break all": "break-all",
    "break word": "break-word",
    "capitalize": "capitalize",
    "cell": "cell",
    "center": "center",
    "center center": "center center",
    "circle": "circle",
    "clone": "clone",
    "close quote": "close-quote",
    "col resize": "col-resize",
    "collapse": "collapse",
    "color": "color",
    "color burn": "color-burn",
    "color dodge": "color-dodge",
    "column": "column",
    "column reverse": "column-reverse",
    "compact": "compact",
    "condensed": "condensed",
    "contain": "contain",
    "container": "container",
    "content box": "content-box",
    "contents": "contents",
    "context menu": "context-menu",
    "copy": "copy",
    "cover": "cover",
    "crisp edges": "crisp-edges",
    "crosshair": "crosshair",
    "darken": "darken",
    "dashed": "dashed",
    "decimal": "decimal",
    "decimal leading zero": "decimal-leading-zero",
    "default": "default",
    "descendants": "descendants",
    "difference": "difference",
    "distribute": "distribute",
    "dot": "dot",
    "dotted": "dotted",
    "double": "double",
    "double circle": "double-circle",
    "e resize": "e-resize",
    "ease in": "ease-in",
    "ease in out": "ease-in-out",
    "ease out": "ease-out",
    "edges": "edges",
    "ellipsis": "ellipsis",
    "embed": "embed",
    "end": "end",
    "ew resize": "ew-resize",
    "exclusion": "exclusion",
    "expanded": "expanded",
    "extra condensed": "extra-condensed",
    "extra expanded": "extra-expanded",
    "fill box": "fill-box",
    "filled": "filled",
    "first": "first",
    "first allow end": "first allow-end",
    "first force end": "first force-end",
    "fixed": "fixed",
    "flex": "flex",
    "flex end": "flex-end",
    "flex start": "flex-start",
    "force end": "force-end",
    "forwards": "forwards",
    "from image": "from-image",
    "full width": "full-width",
    "geometric precision": "geometricPrecision",
    "georgian": "georgian",
    "groove": "groove",
    "hard light": "hard-light",
    "help": "help",
    "hidden": "hidden",
    "hide": "hide",
    "horizontal": "horizontal",
    "hue": "hue",
    "icon": "icon",
    "infinite": "infinite",
    "inherit": "inherit",
    "initial": "initial",
    "ink": "ink",
    "inline block": "inline-block",
    "inline flex": "inline-flex",
    "inline table": "inline-table",
    "inset": "inset",
    "inside": "inside",
    "inter word": "inter-word",
    "isolate": "isolate",
    "italic": "italic",
    "justify": "justify",
    "keep all": "keep-all",
    "large": "large",
    "larger": "larger",
    "last": "last",
    "last allow end": "last allow-end",
    "last force end": "last force-end",
    "left": "left",
    "left center": "left center",
    "left right": "left right",
    "left top": "left top",
    "lighten": "lighten",
    "lighter": "lighter",
    "line through": "line-through",
    "linear": "linear",
    "list item": "list-item",
    "local": "local",
    "loose": "loose",
    "lower alpha": "lower-alpha",
    "lower greek": "lower-greek",
    "lower latin": "lower-latin",
    "lower roman": "lower-roman",
    "lowercase": "lowercase",
    "luminosity": "luminosity",
    "mandatory": "mandatory",
    "manipulation": "manipulation",
    "margin box": "margin-box",
    "match parent": "match-parent",
    "middle": "middle",
    "move": "move",
    "multiply": "multiply",
    "n resize": "n-resize",
    "ne resize": "ne-resize",
    "nesw resize": "nesw-resize",
    "no close quote": "no-close-quote",
    "no drop": "no-drop",
    "no open quote": "no-open-quote",
    "no repeat": "no-repeat",
    "none": "none",
    "normal": "normal",
    "not allowed": "not-allowed",
    "nowrap": "nowrap",
    "ns resize": "ns-resize",
    "nw resize": "nw-resize",
    "nwse resize": "nwse-resize",
    "objects": "objects",
    "oblique": "oblique",
    "open": "open",
    "open quote": "open-quote",
    "optimize legibility": "optimizeLegibility",
    "optimize speed": "optimizeSpeed",
    "outset": "outset",
    "outside": "outside",
    "over left": "over left",
    "overlay": "overlay",
    "overline": "overline",
    "padding box": "padding-box",
    "page": "page",
    "pan down": "pan-down",
    "pan left": "pan-left",
    "pan right": "pan-right",
    "pan up": "pan-up",
    "pan x": "pan-x",
    "pan y": "pan-y",
    "paused": "paused",
    "petite caps": "petite-caps",
    "pixelated": "pixelated",
    "pointer": "pointer",
    "pre": "pre",
    "pre line": "pre-line",
    "pre wrap": "pre-wrap",
    "preserve three d": "preserve-3d",
    "progress": "progress",
    "proximity": "proximity",
    "relative": "relative",
    "repeat": "repeat",
    "repeat no repeat": "repeat no-repeat",
    "repeat x": "repeat-x",
    "repeat y": "repeat-y",
    "reverse": "reverse",
    "ridge": "ridge",
    "right": "right",
    "right bottom": "right bottom",
    "round": "round",
    "row resize": "row-resize",
    "row reverse": "row-reverse",
    "rtl": "rtl",
    "run in": "run-in",
    "s resize": "s-resize",
    "saturation": "saturation",
    "scale down": "scale-down",
    "screen": "screen",
    "scroll": "scroll",
    "scroll position": "scroll-position",
    "se resize": "se-resize",
    "semi condensed": "semi-condensed",
    "semi expanded": "semi-expanded",
    "sesame": "sesame",
    "sideways": "sideways",
    "sideways left": "sideways-left",
    "sideways right": "sideways-right",
    "small": "small",
    "small caps": "small-caps",
    "smaller": "smaller",
    "smooth": "smooth",
    "snap": "snap",
    "soft light": "soft-light",
    "solid": "solid",
    "space": "space",
    "space around": "space-around",
    "space between": "space-between",
    "spaces": "spaces",
    "square": "square",
    "start": "start",
    "start end": "start end",
    "step end": "step-end",
    "step start": "step-start",
    "sticky": "sticky",
    "stretch": "stretch",
    "strict": "strict",
    "stroke box": "stroke-box",
    "style": "style",
    "sub": "sub",
    "super": "super",
    "sw resize": "sw-resize",
    "table": "table",
    "table caption": "table-caption",
    "table cell": "table-cell",
    "table column": "table-column",
    "table column group": "table-column-group",
    "table footer group": "table-footer-group",
    "table header group": "table-header-group",
    "table row": "table-row",
    "table row group": "table-row-group",
    "text": "text",
    "text bottom": "text-bottom",
    "text top": "text-top",
    "thick": "thick",
    "thin": "thin",
    "titling caps": "titling-caps",
    "top": "top",
    "top bottom": "top bottom",
    "transparent": "transparent",
    "triangle": "triangle",
    "ultra condensed": "ultra-condensed",
    "ultra expanded": "ultra-expanded",
    "under": "under",
    "under left": "under left",
    "under right": "under right",
    "underline": "underline",
    "unicase": "unicase",
    "unset": "unset",
    "upper alpha": "upper-alpha",
    "upper latin": "upper-latin",
    "upper roman": "upper-roman",
    "uppercase": "uppercase",
    "upright": "upright",
    "use glyph orientation": "use-glyph-orientation",
    "vertical": "vertical",
    "vertical lr": "vertical-lr",
    "vertical rl": "vertical-rl",
    "vertical text": "vertical-text",
    "view box": "view-box",
    "w resize": "w-resize",
    "wait": "wait",
    "wavy": "wavy",
    "weight": "weight",
    "wrap": "wrap",
    "wrap reverse": "wrap-reverse",
    "x large": "x-large",
    "x small": "x-small",
    "xx large": "xx-large",
    "xx small": "xx-small",
    "zoom in": "zoom-in",
    "zoom out": "zoom-out",
}

mod.list("css_function", desc="CSS functions")
ctx.lists["self.css_function"] = {
    "attr" : "attr",
    "calc" : "calc",
    "circle" : "circle",
    "ellipse" : "ellipse",
    "hsl" : "hsl",
    "hsla" : "hsla",
    "inset" : "inset",
    "linear gradient" : "linear-gradient",
    "matrix" : "matrix",
    "matrix thtree d" : "matrix3d",
    "polygon" : "polygon",
    "radial gradient" : "radial-gradient",
    "repeating linear gradient" : "repeating-linear-gradient",
    "repeating radial gradient" : "repeating-radial-gradient",
    "repeating conic gradient" : "repeating-conic-gradient",
    "rgb" : "rgb",
    "rgba" : "rgba",
    "rotate" : "rotate",
    "rotate three d" : "rotate3d",
    "rotate x" : "rotateX",
    "rotate y" : "rotateY",
    "rotate z" : "rotateZ",
    "scale" : "scale",
    "scale three d" : "scale3d",
    "scale x" : "scaleX",
    "scale y" : "scaleY",
    "scale z" : "scaleZ",
    "skew" : "skew",
    "skew x" : "skewX",
    "skew y" : "skewY",
    "translate" : "translate",
    "translate three d" : "translate3d",
    "translate x" : "translateX",
    "translate y" : "translateY",
    "translate z" : "translateZ",
}