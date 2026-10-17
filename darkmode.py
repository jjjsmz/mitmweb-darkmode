"""mitmweb dark mode: `mitmweb -s darkmode.py`"""

from mitmproxy.tools.web import app

STYLE = b"""<style>
html { background: #fff; filter: invert(1) hue-rotate(180deg) url(#soft-dark); }
img, video { filter: invert(1) hue-rotate(180deg); }
</style>"""

SVG = b"""<svg width="0" height="0" style="position:absolute">
<filter id="soft-dark" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="
0.545 0 0 0 0.133
0 0.576 0 0 0.153
0 0 0.600 0 0.180
0 0 0 1 0"/></filter></svg>"""


# get を差し替えると mitmweb の認証ラッパーが外れるので render_string をフックする
def render_string(self, template_name, **kwargs):
    html = super(app.IndexHandler, self).render_string(template_name, **kwargs)
    return html.replace(b"</head>", STYLE + b"</head>", 1).replace(b"</body>", SVG + b"</body>", 1)


app.IndexHandler.render_string = render_string
