"""Embed the reviewed boundary asset in the HTML; no runtime fetch is needed."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
asset = json.loads((ROOT / 'assets/africa-countries.geojson').read_text(encoding='utf-8'))
payload = json.dumps(asset, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
block = '<script id="africa-basemap" type="application/json">' + payload + '</script>'
page = ROOT / 'index.html'
html = page.read_text(encoding='utf-8')
pattern = r'<script id="africa-basemap" type="application/json">.*?</script>'
if re.search(pattern, html, flags=re.S):
    html = re.sub(pattern, lambda match: block, html, count=1, flags=re.S)
else:
    anchor = '    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>'
    if anchor not in html:
        raise ValueError('Leaflet script anchor not found; HTML was not changed.')
    html = html.replace(anchor, '    ' + block + '\n' + anchor, 1)
page.write_text(html, encoding='utf-8')
print(f'Embedded {len(asset["features"])} country features into {page.name}.')
